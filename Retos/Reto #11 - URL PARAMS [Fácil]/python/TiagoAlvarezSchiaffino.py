import re

def ask_url():
    """
    Prompt the user to enter a URL.

    Returns:
        str: The entered URL.
    """
    return input("URL: ")

def extract_parameters(url):
    """
    Extract parameters from the given URL using regular expressions.

    Args:
        url (str): The URL with parameters.

    Returns:
        list: A list containing the extracted parameter values.
    """
    regex = r"([a-zA-Z0-9._%-]+)"
    params = re.findall(regex, url)
    return params

def main():
    """
    Main function to execute the program.
    """
    url = ask_url()
    parameters = extract_parameters(url)

    print(f"The parameters from the URL are: {parameters}")

if __name__ == "__main__":
    main()
