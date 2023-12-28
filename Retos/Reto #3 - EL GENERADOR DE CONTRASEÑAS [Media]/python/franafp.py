import os, random, string, time

print("#MoureDev te quiero :)")
time.sleep(0.5)

caracteres = input("Quieres usar mayusculas = 1 | minusculas = 2 | ambas = 3: (predeterminado `ambas`: ")
if caracteres == "1":
    caracteres = string.ascii_uppercase
elif caracteres == "2":
    caracteres = string.ascii_lowercase
elif caracteres == "3":
    caracteres = string.ascii_letters
else:
    caracteres = string.ascii_letters
digitos = input("Quieres usar digitos : si = 1 | no = 2: (predeterminado `si`: ")
if digitos == "1":
    digitos = string.digits
elif digitos == "2":
    digitos = ""
else:
    digitos = string.digits

simbolos = input("Quieres usar simbolos : si = 1 | no = 2: (predeterminado `si`: ")
if simbolos == "1":
    simbolos = string.punctuation
elif simbolos == "2":
    simbolos = ""
else:
    simbolos = string.punctuation
longitud = input("Longitud de la contraseña: (predeterminado `16`, minimo = 8 y máximo = 16): ")
if longitud >= "8" and longitud <= "16":
    longitud = int(longitud)
else:
    print("Has superador los limites de la longitud de la contraseña, se usara la longitud predeterminada")
    longitud = 16

print("Generando contraseña...")
os.system("cls")
password = random.choices(caracteres+ digitos+ simbolos, k = longitud)
password_final = "".join(password)
print(f"Tu contraseña es: {password_final}")

# github.com/franafp -- por si te apetece pasarte , un abrazo