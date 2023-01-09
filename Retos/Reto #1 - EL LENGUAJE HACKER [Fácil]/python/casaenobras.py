from unicodedata import normalize

def hacker_text(text: str) -> str:

    leet = {"A":"4","B":"I3","C":"[","D":")","E":"3","F":"|=",
        "G":"&","H":"#","I":"1","J":",_|","K":">|","L":"1","M":"/\/\\","N":"^/",
        "O":"0","P":"|*","Q":"(_,)","R":"I2","S":"5","T":"7","U":"(_)","V":"\/",
        "W":"\/\/","X":"><","Y":"j","Z":"2"}

    text_hacked = ""
    
    text = normalize('NFC', text.upper())
    
    for char in text:
        if char in leet:
            text_hacked += leet[char]
        else:
            text_hacked += char

    return text_hacked



print(hacker_text("Descubrí buenas personas entre rejas"))