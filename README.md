# website_content
testing deployment with content only website

act --input ACT=true --container-options "-v ~/dist:/mnt/act_dist"
act --input-file .env --container-options "-v ~/dist:/mnt/act_dist"
