from github import Github
from github.GithubException import UnknownObjectException


def list_users(repo_name):
    try:
        g = Github()
        repo = g.get_repo(repo_name)
        contributors = repo.get_contributors()

        users = []
        for contributor in contributors:
            users.append(
                {"User": contributor.login, "Contributions": contributor.contributions}
            )

        return users

    except UnknownObjectException as e:
        print(f"Error: {e}")
        return None


if __name__ == "__main__":
    repo_name = "MoureDev/retos-programacion-2023"

    users = list_users(repo_name)

    if users is not None:
        print(f"Contributors for {repo_name}:")
        for user in users:
            print(f"User: {user['User']}, Contributions: {user['Contributions']}")
