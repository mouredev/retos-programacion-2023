

#Mapeo de letras en orden ascii desde el 32 al 122
codes = [' ','!','\"','#','$','%','&','\'','(',')','*','+','\`','-','.','/',
        'o','L','R','E','A','S','b','T','B','g',  ':',';','<','=','>','?','@',
         '4','I3','[',')','3','|=','&','#','1',',_|','>|','1','/\\/\\','^/','0','|*','(_,)','I2','5','7','(_)','\/','\/\/','><','j','2',
         '','','','','','',
         '4','I3','[',')','3','|=','&','#','1',',_|','>|','1','/\\/\\','^/','0','|*','(_,)','I2','5','7','(_)','\/','\/\/','><','j','2']

#Solicita texto a usuario
texto = input("\nEspecifique una frase a convertir: ")

#variables
hackercode = ""
x=0

#Ciclo para recorrer texto y convertirlo
for i in texto:
    hackercode = hackercode + codes[ord(texto[x])-32]
    x = x + 1

#Impresión de resultado
print("\nTexto convertido: " + hackercode)
