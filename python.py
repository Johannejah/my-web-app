import os
import subprocess
from pathlib import Path

def install_git():
    try:
        subprocess.run(["git", "--version"], check=True)
    except subprocess.CalledProcessError:
        print("Git is not installed. Installing Git...")
        subprocess.run(["sudo", "apt-get", "update"])
        subprocess.run(["sudo", "apt-get", "install", "-y", "git"])

//def create_directory(directory):
    if not os.path.exists(directory):
        print(f"Creating directory: {directory}")
        os.makedirs(directory)

def setup_git_repository(directory, repo_url):
    os.chdir(directory)

    # Initialize a new Git repository if not already initialized
    if not Path(".git").is_dir():
        subprocess.run(["git", "init"])

    # Add a remote repository and fetch the latest changes
    subprocess.run(["git", "remote", "add", "origin", repo_url])
    subprocess.run(["git", "fetch", "origin"])

    print(f"Repository setup complete. You can now start working in the {directory} directory.")

if __name__ == "__main__":
    # Replace these values with your desired directory and Git repository URL
    repo_directory = "my_repo"
    git_repository_url = "https://github.com/example/example.git"

    install_git()
    create_directory(repo_directory)
    setup_git_repository(repo_directory, git_repository_url)//
