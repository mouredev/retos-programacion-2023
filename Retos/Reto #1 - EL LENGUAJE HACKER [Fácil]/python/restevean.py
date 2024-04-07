"""
Write a program that receives a text and transforms natural language to
    "hacker language" (known really as "leet" or "1337"). This language
    is characterized by replacing alphanumeric characters.
- Use this table (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
    with the alphabet and numbers in "leet".
    (Use the first option of each transformation. For example "4" for the "a")
"""


LEET_DICT = {'A': '4', 'B': 'I3',
             'C': '[', 'D': ')', 'E': '3',
             'F': '|=', 'G': '&', 'H': '#',
             'I': '1', 'J': ',_|', 'K': '>|',
             'L': '1', 'M': '/\/\/', 'N': '^/',
             'O': '0', 'P': '|*', 'Q': '(_,)',
             'R': 'I2', 'S': '5', 'T': '7',
             'U': '(_)', 'V': '\/', 'W': '\/\/',
             'X': '><', 'Y': 'j', 'Z': '2',
             '1': 'L', '2': 'R', '3': 'E',
             '4': 'A', '5': 'S', '6': 'b',
             '7': 'T', '8': 'B', '9': 'G',
             '0': 'o'
             }


def leet(message):
    result = ""

    for character in message:
        if character == " ":
            result += "   "
        else:
            result += LEET_DICT[character.upper()] + " "

    return result[:-1]


if __name__ == "__main__":
    # Test the program
    text = "Hello World"
    print(leet(text))
