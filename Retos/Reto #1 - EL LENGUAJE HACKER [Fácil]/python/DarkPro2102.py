def hacker_language(text:str) -> str:

    hacker_dict = {"A":"4","B":"8","E":"3","G":"6","I":"1","L":"1","O":"0","Q":"9","S":"5","T":"7","U":"_","Z":"2"}

    for char in hacker_dict:
        text = text.upper().replace(char, hacker_dict[char])

    return text
    

if __name__ == "__main__":
    text = "In that period leet speak existed only in small circles, and was only used when necessary"
    hacker_text = hacker_language(text)
    print(hacker_text) # Output : "1N 7H47 P3R10D 1337 5P34K 3X1573D 0N1Y 1N 5M411 C1RC135, 4ND W45 0N1Y _53D WH3N N3C3554RY"