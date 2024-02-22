
sum = 0
palabra = input("Ingrese palabra:").upper()

if palabra.isalpha():
  while True:
    for letra in palabra:
      sum+=ord(letra)-64

    print("La suma es:",sum)

    if sum==100:
      break
    else:
      palabra = input("Ingrese otra palabra").upper()
      sum = 0
else:
  print("No son solo letras")
