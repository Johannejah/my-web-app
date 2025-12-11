#!/bin/bash

#Check if Git is installed
if ! command -v git &> /dev/null; then
	echo "Git is not installed. Installing Git..."
	sudo apt-get update
	sudo apt-get install -y git
fi

# Create a directory and navigate into it
repo_directory="my_repo"
if [ ! -d "$repo_directory" ]; then
	echo "Creating directory: $repo_directory"
	mkdir "$repo_directory"
fi
#
#//cd "$repo_directory" || exit
#
#          # Initialize a new Git repository
#          if [ ! -d ".git" ]; then
#            git init
#            fi
#
#            # Add a remote repository and fetch the latest changes
#            git_repo_url="https://github.com/example/example.git" # Replace with your Git repository URL
#            git remote add origin "$git_repo_url"
#            git fetch origin
#
#            echo "Repository setup complete. You can now start working in the $repo_directory directory."//
