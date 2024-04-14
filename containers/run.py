import sys
import subprocess
import os

# Path to the directory containing docker-compose.yml
docker_compose_dir = os.path.join(os.path.dirname(__file__))

# Default command if no argument is provided
command = "build"

# Check if an argument is provided and use it as the command
if len(sys.argv) > 1:
    command = sys.argv[1]

# Change the working directory
os.chdir(docker_compose_dir)

if(command == "build"):
    subprocess.run(["docker-compose", "run", "--rm", "astro-big-doc", "build"])
elif(command == "init"):
    subprocess.run(["docker-compose", "run", "--rm", "seeds"])
elif(command == "apache"):
    subprocess.run("docker-compose up apache", shell=True, check=True)
elif(command == "server"):
    subprocess.run("docker-compose up nginx", shell=True, check=True)
