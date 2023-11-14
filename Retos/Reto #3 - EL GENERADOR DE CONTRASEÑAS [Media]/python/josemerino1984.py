"""/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */"""
import string
import secrets


def validarlogitid():
    
    while True:
        try:
            lonpass=int(input("defina la longitud de la contrasena entre 8 y 16 caracteres "))
            if lonpass<8 or lonpass>16:
                print("la longitud de contrasena debe estar entre 8 y 16 caracteres")
            else:
                 return(lonpass)
        except ValueError :
            print("debe ingresar un valor numerico entre 8 y 16")

      
def validacion(leer,string):
     ##validacion
     evaf=True
     while evaf==True:
        if leer.upper()=="SI"or leer.upper()=="NO" :
            return leer.upper()

        else:
            print("opcion invalida,responda SI/NO")
            leer=input(f"desea que la contrasena contenga {string} SI/NO :")
            print("valor de variable es ", leer)

letras="ABCDFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxy"
numero="12345678910"
especiales=string.punctuation
ctr=0

lonpa=validarlogitid()
rnum=input("desea que la contrasena contenga numeros SI/NO: ")
rnum=validacion(rnum,"numero")
rsimb=input("desea que la contrasena contenga simbolos SI/NO: ")
rsimb=validacion(rsimb,"simbolo")




if rnum=="SI" and rsimb=="SI":
    caracteres=letras+numero+especiales

elif rnum=="NO" and rsimb=="NO":
    caracteres=letras
elif rnum=="SI" and rsimb=="NO":
    caracteres=letras+numero
else:
    caracteres=letras+especiales


pw=""
i=0
while i< lonpa:
    pw+="".join(secrets.choice(caracteres))
    i=i+1


print(f"la contrasena es {pw} ")










