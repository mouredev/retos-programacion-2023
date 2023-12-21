import os
from github import Github

# Constants
MAX_COMMITS = 10
REPO_PATH = "mouredev/programming-challenges-2023"

def get_github_instance():
    """
    Creates and returns a GitHub instance using the access token from the environment.

    Returns:
        Github instance.
    """
    access_token = os.environ.get("GITHUB_ACCESS_TOKEN")
    if not access_token:
        raise ValueError("GitHub access token not found in environment variables. Please set GITHUB_ACCESS_TOKEN.")
    return Github(access_token)

def get_commit_info(commit):
    """
    Extracts and formats commit information.

    Args:
        commit: GitHub commit object.

    Returns:
        Tuple containing commit information (hash, author, message, date).
    """
    commit_hash = commit.sha[:6]
    author = commit.commit.author.name
    message = commit.commit.message
    date = commit.commit.author.date.strftime("%d/%m/%Y %H:%M")
    return commit_hash, author, message, date

def print_commits(repo):
    """
    Prints information for the last commits in the GitHub repository.

    Args:
        repo: GitHub repository object.
    """
    try:
        commits = repo.get_commits()[:MAX_COMMITS]
        for i, commit in enumerate(commits):
            commit_info = get_commit_info(commit)
            print(f"Commit {i+1} | {commit_info[0]} | {commit_info[1]} | {commit_info[2]} | {commit_info[3]}")
    except Exception as e:
        print(f"Error retrieving commits: {e}")

def main():
    """
    Main function to run the program.
    """
    try:
        github = get_github_instance()
        repo = github.get_repo(REPO_PATH)
        print_commits(repo)
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
