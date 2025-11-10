LEET = {
    "A":"4","B":"|3","C":"[","D":")","E":"3","F":"|=",
    "G":"&","H":"#","I":"1","J":",_|","K":">|","L":"1",
    "M":"/\/\\","N":"^/","O":"0","P":"|*","Q":"(_,)","R":"I2",
    "S":"5","T":"7","U":"(_)","V":"\/","W":"\/\/","X":"><",
    "Y":"j","Z":"2","1":"I","2":"Z","3":"E","4":"A","5":"S",
    "6":"G","7":"T","8":"B","9":"q","0":"()",
    }
texto = input("Ingrese texto: ")
texto2=[]
for c in texto.upper():
    if c in LEET:
        texto2.append(LEET[c])
    else:
        texto2.append(" ")
    resultado ="".join(texto2)
print(f"resultado: {resultado}")