import requests


class GithubService:
    def __init__(self, repo):
        self.repo = repo
        self.base_url = f"https://api.github.com/repos/{self.repo}"

    def get_commits(self, per_page=10):
        url = f"{self.base_url}/commits"
        params = {"per_page": per_page}
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err) from None
        return response.json()

    def print_commits(self, per_page=10):
        commits = self.get_commits()
        if not commits:
            return None
        for i, commit in enumerate(commits):
            sha = commit.get("sha")
            _commit = commit.get("commit")
            author = _commit.get("author").get("name")
            message = _commit.get("message").strip()
            date = _commit.get("committer").get("date")
            print(f"{i}. {sha} | {author} | {message} | {date}")
            print()


if __name__ == "__main__":
    url = "mouredev/retos-programacion-2023"
    github_service = GithubService(url)
    print(github_service.print_commits())
