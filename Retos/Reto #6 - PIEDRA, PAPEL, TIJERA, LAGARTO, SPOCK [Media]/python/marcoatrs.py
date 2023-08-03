from typing import List

options = {
    "🗿": ("✂️", "🦎"),
    "📄": ("🗿", "🖖"),
    "✂️": ("📄", "🦎"),
    "🦎": ("📄", "🖖"),
    "🖖": ("🗿", "✂️"),
}

def check_round(p1: str, p2: str) -> tuple:
    if (p1 not in options.keys()) or (p2 not in options.keys()):
        print("Option invalida")
        return (0, 0)

    if p1 == p2:
        return (0, 0)

    if p2 in options[p1]:
        return (1, 0)
    
    return (0, 1)

def game(options_list: List[tuple]):
    p1, p2 = 0, 0
    for _p1, _p2 in options_list:
        round = check_round(_p1, _p2)
        p1 += round[0]
        p2 += round[1]
    
    if p1 == p2:
        print("Tie")
    elif p1 > p2:
        print("Player 1")
    else:
        print("Player 2")


game([("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")])
game([("🗿","🗿"), ("🖖","✂️"), ("🦎","📄")])