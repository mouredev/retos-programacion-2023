"""
Create a program that calculates who wins more rock, paper, scissors, lizard, spock.
    - The result can be: "Player 1", "Player 2", "Tie" (tie)
    - The function receives a list of pairs, representing each game.
    - The pair can contain combinations of "🗿" (rock), "📄" (paper),
      "✂️" (scissors), "🦎" (lizard) or "🖖" (spock).
    - Example. Input: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Result: "Player 2".
    - You must find information about how these 5 possibilities play.
"""


def calculate_winner(jugadas):
    rules = {
        "🗿": ["✂️", "🦎"],
        "📄": ["🗿", "🖖"],
        "✂️": ["📄", "🦎"],
        "🦎": ["📄", "🖖"],
        "🖖": ["✂️", "🗿"]
    }

    points = {"Player 1": 0, "Player 2": 0}

    for play1, play2 in jugadas:
        if play2 in rules[play1]:
            points["Player 1"] += 1
        elif play1 in rules[play2]:
            points["Player 2"] += 1

    if points["Player 1"] > points["Player 2"]:
        return "Player 1"
    elif points["Player 1"] < points["Player 2"]:
        return "Player 2"
    else:
        return "Tie"


def main():

    play1 = [("🗿", "✂️"), ("✂️", "🗿"), ("📄", "✂️")]
    play2 = [("🗿", "📄"), ("📄", "🗿"), ("📄", "✂️")]
    play3 = [("🗿", "🗿"), ("📄", "📄"), ("✂️", "✂️")]
    play4 = [("🗿", "✂️"), ("✂️", "🗿"), ("📄", "✂️")]
    result = calculate_winner([("🗿", "✂️"), ("✂️", "🗿"), ("📄", "✂️")])
    print(f'{calculate_winner([("🗿", "✂️"), ("✂️", "🗿"), ("📄", "✂️")])} wins')  # "Player 2"
    print(f'{calculate_winner([("🗿", "📄"), ("📄", "🗿"), ("📄", "✂️")])} wins')  # "Player 1"
    print(f'{calculate_winner([("🗿", "🗿"), ("📄", "📄"), ("✂️", "✂️")])} wins')  # "Tie"
    print(f'{calculate_winner([("🗿", "✂️"), ("✂️", "🗿"), ("📄", "✂️")])} wins')  # "Player 2"


if __name__ == "__main__":
    main()