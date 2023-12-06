def encontrar_diferentes(cadena1, cadena2):
  if len(cadena1) != len(cadena2):
    raise ValueError("Las cadenas de texto deben tener la misma longitud")
  
  caracteres_diferentes = []
  
  for i in range(len(cadena1)):
    if cadena1[i] != cadena2[i]:
      caracteres_diferentes.append(cadena1[i])
  
  return caracteres_diferentes

# Ejemplos de uso
cadena1 = "Me llamo juanppdev"
cadena2 = "Me lleno juanppdev"
resultado1 = encontrar_diferentes(cadena1, cadena2)
print(resultado1)

cadena3 = "Me llamo Juan Pablo"
cadena4 = "Me lleno Juan Pablo"
resultado2 = encontrar_diferentes(cadena3, cadena4)
print(resultado2)