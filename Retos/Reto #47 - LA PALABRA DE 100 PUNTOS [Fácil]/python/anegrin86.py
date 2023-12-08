# Almaceno las letras del abecedario en la variable "letras":
letras = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
      
# Se crea un ciclo que termina si se alcanzan los 100 puntos:
while True:
    puntos = 0
    palabra = input("Escriba una palabra que llegue a 100 puntos: ")
    palabra = palabra.upper()
    for letra in palabra:
        puntos += letras.index(letra) + 1
    if puntos == 100:
        break
    print(f"Su palabra tiene un valor de {puntos} puntos")
print("ENHORABUENA, SU PALABRA INTRODUCIDA ALCANZÓ LOS 100 PUNTOS")        


    



