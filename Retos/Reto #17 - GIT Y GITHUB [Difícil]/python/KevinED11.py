import requests


from typing import Generator


def get_repo_commits(repo: str) -> str:
    return f"https://api.github.com/repos/{repo}/commits"


def all_commits(repo_url: str) -> list[dict]:
    try:
        return requests.get(repo_url).json()
    except requests.exceptions.RequestException as err:
        print(err)


def format_commits(commits: list[dict]) -> Generator:
    return (f"commit #{str(i+1)} | hash={str(commit['sha'])} | Author={commit['commit']['author']['name']} | Message={commit['commit']['message']} | Date={commit['commit']['author']['date']}" for i, commit in enumerate(commits))


def commits_to_show(number: int = 10) -> int:
    try:
        return abs(int(number))
    except ValueError:
        print(ValueError(
            f"Invalid value for 'number': '{number}'. Please enter a valid integer."))


def generate_commits(commits: Generator, number: int = 10, mode="DESC") -> list[str]:
    mode = mode.upper()
    commit_mode: tuple[str, str] = ("ASC", "DESC")

    try:
        if mode not in commit_mode:
            raise ValueError(f"PLace a valide mode: {commit_mode}")
    except ValueError as err:
        print(err)

    if mode == commit_mode[0]:
        return [commit for commit in commits][:number]

    return [commit for commit in commits][-number:]


def main() -> None:
    repo_to_use = get_repo_commits(repo="mouredev/retos-programacion-2023")
    available_commits = all_commits(repo_url=repo_to_use)
    formatted_commits = format_commits(commits=available_commits)
    commits_number_to_show = commits_to_show(number="5")

    commits = generate_commits(
        formatted_commits, commits_number_to_show, mode="asc")
    print(commits)


if __name__ == "__main__":
    main()
