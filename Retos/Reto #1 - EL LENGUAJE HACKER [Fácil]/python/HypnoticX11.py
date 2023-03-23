text = input("Dime un texto para traducirlo a Leet: ")
LeetDic = {"A":"4","B":"I3","C":"[","D":")","E":"3","F":"|=","G":"&","H":"#","I":"1","J":",_|","K":">|",
"L":"1","M":"/\/\\","N":"^/","O":"0","P":"|*","Q":"(_,)","R":"I2","S":"5","T":"7","U":"(_)","V":"\/",
"W":"\/\/","X":"><","Y":"j","Z":"2",}
LeetText = " "

text = text.upper()
for letter in text:
    if letter in LeetDic:
        LeetText += LeetDic[letter]
    else:
        LeetText += letter

print(LeetText)