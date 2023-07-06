alphabet="abcdefghijklmnñopqrstuvwxyz"

def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s

options=[1,2]

sentido=input('Ingresa 1 para desplazar hacia la derecha o 2 para desplazar hacia la izquierda\n')

while int(sentido) not in options:
   sentido=input('Ingresa 1 para desplazar hacia la derecha o 2 para desplazar hacia la izquierda\n')

dezplazamiento=input('Ingresa la cantidad de desplazamientos\n')
texto=input('Ingresa el texto a cifrar\n')
cifrado=''
if int(sentido) == 1:
  for letra in normalize(texto.lower()):
      if letra in alphabet:
          index=alphabet.index(letra)
          cifrado+=alphabet[(index+int(dezplazamiento))%27]
      else:
          cifrado+=letra
elif int(sentido)==2:
  for letra in normalize(texto.lower()):
      if letra in alphabet:
          index=alphabet.index(letra)
          cifrado+=alphabet[(index-int(dezplazamiento))%27]
      else:
          cifrado+=letra
    
print(cifrado)


