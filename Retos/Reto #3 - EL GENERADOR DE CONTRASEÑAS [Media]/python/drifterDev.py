from random import randint
numeros=["1","2","3","4","5","6","7","8","9","0"]
letras1=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
letras2=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
simbolos=["@","?","'","¿","¡","|","{","[",",","]","}","+","-",",",".",";",":","*","~"]
listaCompleta=numeros+letras1+letras2+simbolos
tamano=randint(8,16)
contrasena=""
for i in range(tamano):
  numeroAleatorio=randint(0, (len(listaCompleta)-1))
  contrasena+=listaCompleta[numeroAleatorio]
print("Tu nueva contraseña es: "+contrasena)
