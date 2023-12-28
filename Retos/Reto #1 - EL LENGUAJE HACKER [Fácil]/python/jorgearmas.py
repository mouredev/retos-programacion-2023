"""
Write a program that receives a text and transforms natural language to
"hacker language" (actually known as "leet" or "1337"). This language
is characterized by substituting alphanumeric characters.
- Use this table (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
with the alphabet and numbers in "leet".
(Use the first option of each transformation, for example "4" for "a")
"""
word = input("Enter a random word or phrase: ")

print(word)
#String is converted into a list
x = list(word)
nw_lst = []
strg = ""

#translate
for i in x:
    if i == "a":
        nw_lst.append("4")
    elif i == "b":
        nw_lst.append("I3")
    elif i == "c":
        nw_lst.append("[")
    elif i == "d":
        nw_lst.append(")")
    elif i == "e":
        nw_lst.append("3")
    elif i == "f":
        nw_lst.append("|=")
    elif i == "g":
        nw_lst.append("&")
    elif i == "h":
        nw_lst.append("#")
    elif i == "i":
        nw_lst.append("1")
    elif i == "j":
        nw_lst.append(",_|")
    elif i == "k":
        nw_lst.append(">|")
    elif i == "l":
        nw_lst.append("£")
    elif i == "m":
        nw_lst.append("JVI")
    elif i == "n":
        nw_lst.append("^/")
    elif i == "o":
        nw_lst.append("()")
    elif i == "p":
        nw_lst.append("|*")
    elif i == "q":
        nw_lst.append("(_,)")
    elif i == "r":
        nw_lst.append("I2")
    elif i == "s":
        nw_lst.append("5")
    elif i == "t":
        nw_lst.append("-|-")
    elif i == "u":
        nw_lst.append("µ")
    elif i == "v":
        nw_lst.append("|/")
    elif i == "w":
        nw_lst.append("'//")
    elif i == "x":
        nw_lst.append("Ж")
    elif i == "y":
        nw_lst.append("¥")
    elif i == "z":
        nw_lst.append("%")
    elif i == " ":
        nw_lst.append(" ")

#convert list to string
for ele in nw_lst:
    strg += ele

print(f"Translate => {strg}")
