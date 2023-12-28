def conversor_language(text):
    conversor_dict = {"a" : "4",
                      "b" : "5",  
                      "c" : "[",
                      "d" :")",
                      "e" : "3",
                      "f" : "|=",
                      "g" : "&",
                      "h" : "#",
                      "i" : "1",
                      "j" : ",_|",
                       "k" : ">|",
                       "l" : "1",
                       "m" : "[v]",
                        "n": "^/",
                        "o": "0",
                        "p": "?",
                        "q": "9",
                        "r": "2",
                        "s": "5",
                        "t": "7",
                        "u": "(_)",
                        "v": "\/",
                        "w": "N/",
                        "x": "><",
                        "y": "\|/",
                        "z": "%",
                       }
    text_converted = ""
    for i in text.lower():
        text_converted += conversor_dict.get(i)
    return f"La palabra inicial {text} ha sido traducida a leet dando lugar a {text_converted}"

print(conversor_language("adios"))

