#
#  Escribe un programa que reciba un texto y transforme lenguaje natural a
#  "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
#  se caracteriza por sustituir caracteres alfanuméricos.
#  - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
#   con el alfabeto y los números en "leet".
#   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
#
#----------------FUNCIONES-------------------------------
def hack_leitor(text_to_trans, hackcionario):          #Recibe la cadena de texto a traducir y el diccionario de equivalencia
    traduccion=""                                       #vaciamos la traduccion para evitar errores
    for letra in list(text_to_trans):                   #recorremos cada letra de la cadena de texto
        traduccion = traduccion + hackcionario[letra]
    print(traduccion)                                   #presento el resultado
        
hack_equivalencia = {"A":"4","B":"I3","C":"[","D":")","E":"3","F":"|=","G":"&","H":"#","I":"1","J":",_|","K":">|","L":"1","M":"JVI","N":"^/","Ñ":"^/|","O":"0","P":"|*","Q":"(_,)","R":"I2","S":"5","T":"7","U":"(_)","V":"|/","W":"\/\/","X":"><","Y":"j","Z":"2","1":"L","2":"R","3":"E","4":"A","5":"S","6":"b","7":"T","8":"B","9":"g","0":"o"," ":" ",}

#EMPIEZA LA TRADUCCION, PERO PRIMERO DAME  TEXTO    
print ("introduzca texto a convertir")              
texto=input().upper()                               #Forzamos todo el texto en MAYÚSCULAS
hack_leitor(texto, hack_cionario)                   #llamo a la función y le paso la cadena de texto y las equivalencias 
