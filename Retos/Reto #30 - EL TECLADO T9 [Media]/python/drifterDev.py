def teclado_t9(input_nums: list[str]) -> str:
    letters = {
        "1": ",.?!",
        "2": "ABC",
        "3": "DEF",
        "4": "GHI",
        "5": "JKL",
        "6": "MNO",
        "7": "PQRS",
        "8": "TUV",
        "9": "WXYZ",
        "0": " ",
    }
    res = []
    for string in input_nums:
        res.append(letters[string[0]][len(string) - 1])
    return "".join(res)


if __name__ == "__main__":
    input_nums = input().split("-")
    print(teclado_t9(input_nums))
