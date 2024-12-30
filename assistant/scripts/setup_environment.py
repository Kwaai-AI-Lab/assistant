#!/usr/bin/env python3
import subprocess
import sys
import os
import shutil
from pathlib import Path

import logging

# Ensure the parent directory is in sys.path so relative imports work.
base_dir = Path(__file__).parent.parent
if base_dir not in sys.path:
    sys.path.append(str(base_dir))

from common.paths import base_dir, backend_dir, frontend_dir, env_file

def setup_backend():
    # Directly install Python dependencies globally within the container
    subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"], check=True)
    subprocess.run([sys.executable, "-m", "pip", "install", "-r", str(backend_dir / "requirements.txt")], check=True)
    
    logging.info("<------Backend setup complete.------>")


def build_frontend():
    print("Setting up the frontend environment...")
    npm_path = shutil.which("npm")
    if npm_path:
        current_dir = os.getcwd()
        os.chdir(frontend_dir)
        subprocess.run([npm_path, "install"], check=True)
        subprocess.run([npm_path, "run", "build"], check=True)
        os.chdir(current_dir)

        logging.info("<------Frontend built successfully.------>")
    else:
        print("Skipped as npm command not found.")
        print("Download Node.js to build the frontend or use a prebuilt version (e.g. canary branch): https://nodejs.org/en/download")

def setup_vscode():
    print("Setting up VSCode configuration...")
    vscode_dir = base_dir / '.vscode'
    vscode_dir.mkdir(exist_ok=True)

    sample_files = list(vscode_dir.glob('*.sample'))
    for sample_file in sample_files:
        target_file = vscode_dir / sample_file.stem
        if not target_file.exists():
            shutil.copy(sample_file, target_file)
            print(f"Copied {sample_file} to {target_file}")

    logging.info("<------VSCode configuration setup complete.------>")

def main():
    setup_backend()
    build_frontend()
    setup_vscode()

    print("Setup complete.")

if __name__ == "__main__":
    main()