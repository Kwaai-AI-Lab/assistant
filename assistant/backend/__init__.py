# backend package
import os
from common import paths
from dotenv import load_dotenv

print("Initializing backend package")
# Load environment variables
load_dotenv()

# List of directories to ensure exist
required_directories = [
    paths.data_dir
]

# Create directories if they do not exist
for directory in required_directories:
    if not os.path.exists(directory):
        os.makedirs(directory)
