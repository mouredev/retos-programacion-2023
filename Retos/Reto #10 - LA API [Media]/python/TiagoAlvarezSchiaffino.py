import requests

def get_random_quote():
    """
    Get a random anime quote from the AnimeChan API.

    Returns:
        dict: A dictionary containing information about the quote.
    """
    api_url = "https://animechan.xyz/api/random"
    response = requests.get(api_url)
    return response.json()

def get_quote_by_anime_title(title):
    """
    Get a random anime quote based on the provided anime title from the AnimeChan API.

    Args:
        title (str): The title of the anime.

    Returns:
        dict: A dictionary containing information about the quote.
    """
    api_url = f"https://animechan.xyz/api/random/anime?title={title}"
    response = requests.get(api_url)
    return response.json()

def get_quote_by_character(character_name):
    """
    Get a random anime quote based on the provided character name from the AnimeChan API.

    Args:
        character_name (str): The name of the anime character.

    Returns:
        dict: A dictionary containing information about the quote.
    """
    api_url = f"https://animechan.xyz/api/random/character?name={character_name}"
    response = requests.get(api_url)
    return response.json()

def get_quote(option):
    """
    Get a quote based on the user's choice.

    Args:
        option (str): The user's choice.

    Returns:
        dict: A dictionary containing information about the quote.
    """
    if option == "1":
        return get_random_quote()
    elif option == "2":
        anime_title = input("Enter the anime title: ")
        return get_quote_by_anime_title(anime_title)
    elif option == "3":
        character_name = input("Enter the character name: ")
        return get_quote_by_character(character_name)
    else:
        print("Invalid option")

while True:
    # Request user's choice
    print("Options:")
    print("1. Get a random quote")
    print("2. Get a random quote by anime title")
    print("3. Get a random quote by character name")
    print("4. Exit")

    option = input("Select an option (1, 2, 3, or 4): ")

    if option == "4":
        print("Exiting the program. Goodbye!")
        break

    # Display the result
    print("API Result:")
    result = get_quote(option)

    if result:
        print(f"Anime: {result['anime']}")
        print(f"Character: {result['character']}")
        print(f"Quote: {result['quote']}")
