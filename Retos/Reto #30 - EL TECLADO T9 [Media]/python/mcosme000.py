def keyboard(str):
    sequence = {
        2: ["a", "b", "c"],
        3: ["d", "e", "f"],
        4: ["g", "h", "i"],
        5: ["j", "k", "l"],
        6: ["m", "n", "o"],
        7: ["p", "q", "r", "s"],
        8: ["t", "u", "v"],
        9: ["w", "x", "y", "z"],
        0: [" "]
    }
    msg = ''
    if str == "": return "no message"
    for n in str.split("-"):
        if n == 0:
            msg += " "
        else:
            msg += sequence[int(n[0])][len(n) - 1]
    return msg.upper()

print(keyboard("6-666-88-777-33-3-33-888"))
print(keyboard("6-666-88-777-33-0-3-33-888"))
print(keyboard("6-676-88-777-33-3-33-888"))
print(keyboard("6-6a6-88-777-33-3-33-888"))
