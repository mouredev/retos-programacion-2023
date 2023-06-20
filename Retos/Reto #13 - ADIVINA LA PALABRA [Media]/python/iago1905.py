import random
intentos = 3
palabras = ["Invernar","Argentino","Magia","Modelar","Vigilar"]

def palabra_aleatoria_incompleta(palabra):
    num_letras_quitar = int(len(palabra)*40/100)
    letra_que_saco = []
    posicion = random.sample(range(0,len(palabra)),num_letras_quitar)
    for i in posicion:
        letra_que_saco.append(palabra[i].lower())
        palabra = palabra.replace(palabra[i],"_",1)
    return [palabra,letra_que_saco]

if __name__ == "__main__":
        palabra_elegida = random.choice(palabras)
        palabra_adivinar,letras_ocultas = palabra_aleatoria_incompleta(palabra_elegida)
        while intentos > 0 and len(letras_ocultas) > 0:
            
            print("Adivina la palabra: ", palabra_adivinar)
            seleccion = input("Queres adivinar la palabra o una letra? (p/l): ")
            if seleccion == "p":
                palabra = input("Ingrese una palabra: ").lower()
                if palabra == palabra_elegida.lower():
                    break
                else:
                    intentos -= 1
                    print("Te quedan ", intentos, " intentos")
            if seleccion == "l":
                letra = input("Ingrese una letra: ")
                if letra in letras_ocultas:
                    palabra_adivinar = palabra_adivinar.replace("_",letra,1)
                    letras_ocultas.remove(letra.lower())
                else:
                    intentos -= 1
                    print("Te quedan ", intentos, " intentos")
                
        if intentos == 0:
            print("Perdiste")
        else:
            print("Ganaste")


