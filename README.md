# Github basic

# Creating a Repository
# dffgdfg

# Initialize a new Git repository:g
bash
git init

# Add files to the repository:
bash
git add .

# Commit the changes:
bash
git commit -m "Initial commit"

***Check branch name - master and change it:
git branch -m master main


# Create a new repository on GitHub and push your local repository:

bash
gh repo create [repository-name] --public

git remote add origin https://github.com/username/repository-name.git
git push -u origin main

# Creating Branches
Create and switch to a new branch:
bash
git checkout -b new-branch-name

# Push the new branch to GitHub:
bash
git push -u origin new-branch-name

# Forking a Repository
Fork an existing repository:
bash
gh repo fork owner/repository-name

# Clone the forked repository:
bash
git clone https://github.com/your-username/repository-name.git

# Add the original repository as an upstream remote:
bash
git remote add upstream https://github.com/original-owner/repository-name.git
****************************************************
If there are remote branches that no longer exist on GitHub but are still listed locally, you can prune your remote tracking branches:

bash
git remote prune origin
