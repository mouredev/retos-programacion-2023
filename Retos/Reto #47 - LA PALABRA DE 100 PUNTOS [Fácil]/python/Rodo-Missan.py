puntuacion = 0
puntuaciones = {
    'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,
    'k':11,'l':12,'m':13,'n':14,'ñ':15,'o':16,'p':17,'q':18,'r':19,
    's':20,'t':21,'u':22,'v':23,'w':24,'x':25,'y':26,'z':27
}

print("\nBienvenido al juego de la palabra de 100 puntos.")
print("\nIngrese una palabra para sumar puntos. Cada letra tiene un valor del 1 al 27.")
print("\nEl juego termina cuando una palabra alcanza 100 puntos.")
print("\n¡Buena suerte!")

def validar_palabra(palabra):
    return palabra.isalpha()

while puntuacion < 100:
    puntuacion = 0
    palabra = input("\nIngrese una palabra: ").lower()
    if validar_palabra(palabra) == False:
        print("Entrada inválida. Por favor, ingrese solo letras.")
        continue

    for letra in palabra:
        puntuacion += puntuaciones.get(letra, 0)

    print(f"La puntuación de la palabra '{palabra}' es: {puntuacion} puntos.")

print(f"¡Felicidades! Has alcanzado {puntuacion} puntos y ganado el juego.")