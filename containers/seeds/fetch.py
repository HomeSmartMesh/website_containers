import yaml
import requests
import sys

def fetch_and_save_dockerfiles(yaml_input):
    # Load the YAML data from string
    dockerfile_mappings = yaml.safe_load(yaml_input)
    
    for item in dockerfile_mappings:
        for key, url in item.items():
            # Fetch the Dockerfile from the URL
            response = requests.get(url)
            if response.status_code == 200:
                # Save the Dockerfile content to a file named <key>.Dockerfile
                filename = f"/dockerfiles/{key}.Dockerfile"
                with open(filename, 'w') as file:
                    file.write(response.text)
                print(f"Saved {filename}")
            else:
                print(f"Failed to fetch {url} with status code {response.status_code}")

if __name__ == "__main__":
    # Assume the YAML data is passed as a command line argument
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as file:
            yaml_input = file.read()
        fetch_and_save_dockerfiles(yaml_input)
    else:
        print("Please provide a file path to the YAML input as an argument.")
