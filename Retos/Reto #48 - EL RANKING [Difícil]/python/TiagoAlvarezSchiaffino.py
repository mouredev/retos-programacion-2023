from github import Github

REPOSITORY_NAME = 'MoureDev/retos-programacion-2023'

def get_contributions():
    """
    Get the list of contributors and their contributions from the GitHub repository.
    
    Returns:
    contributions_list (list): List of tuples (user, contributions).
    """
    try:
        # Initialize the GitHub instance
        g = Github()

        # Get the repository
        repo = g.get_repo(REPOSITORY_NAME)

        # Get the list of contributors
        contributors = repo.get_contributors()

        # Create a list of tuples (user, contributions)
        contributions_list = [(contributor.login, contributor.contributions) for contributor in contributors]

        return contributions_list

    except Exception as e:
        print(f"Error: {e}")
        return []

def show_sorted_contributions(contributions_list):
    """
    Sort and display the list of contributions.

    Args:
    contributions_list (list): List of tuples (user, contributions).
    """
    # Sort the list by the number of contributions (solved exercises)
    contributions_list.sort(key=lambda x: x[1], reverse=True)

    # Show the sorted information
    print("Ranking of Contributors:")
    print("------------------------")
    for idx, (user, contributions) in enumerate(contributions_list, start=1):
        print(f"{idx}. {user}: {contributions} contributions")

if __name__ == '__main__':
    # Get the list of contributions
    contributions = get_contributions()

    # Show the sorted information
    show_sorted_contributions(contributions)

    # Show the total number of users and contributions
    total_users = len(contributions)
    total_contributions = sum(contribution[1] for contribution in contributions)

    print(f"\nTotal users who have participated: {total_users}")
    print(f"Total corrections sent: {total_contributions}")