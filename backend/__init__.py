# backend package
import os
from common import paths
from dotenv import load_dotenv

print("Initializing backend package")
# Load environment variables
RUNNING_IN_DOCKER = os.environ.get('RUNNING_IN_DOCKER', 'false').lower() == 'true'

if not RUNNING_IN_DOCKER:
    print("Loading .env file")
    load_dotenv()
else:
    print(f"RUNNING_IN_DOCKER = {os.environ.get('RUNNING_IN_DOCKER')}")

# List of directories to ensure exist
required_directories = [
    paths.data_dir
]

# Create directories if they do not exist
for directory in required_directories:
    if not os.path.exists(directory):
        os.makedirs(directory)
