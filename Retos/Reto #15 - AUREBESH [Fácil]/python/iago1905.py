'''
Crea una función que sea capaz de transformar Español al lenguaje básico del universo
Star Wars: el "Aurebesh".
Puedes dejar sin transformar los caracteres que no existan en "Aurebesh".
También tiene que ser capaz de traducir en sentido contrario.
 
Lo has conseguido? Nómbrame en twitter.com/mouredev y escríbeme algo en Aurebesh.
Que la fuerza os acompañe!
'''

diccionario = {
    "A": "Aurek", "B": "Besh", "C": "Cresh", "D": "Dorn", "E": "Esk", "F": "Forn", "G": "Grek", "H": "Herf", "I": "Isk",
    "J": "Jenth", "K": "Krill", "L": "Leth", "M": "Mern", "N": "Nern", "O": "Osk", "P": "Peth", "Q": "Qek", "R": "Resh",
    "S": "Senth", "T": "Trill", "U": "Usk", "V": "Vev", "W": "Wesk", "X": "Xesh", "Y": "Yirt", "Z": "Zerek"
}

diccionario_inverso = {valor: clave for clave, valor in diccionario.items()}

def traductor(texto):
    for palabra in texto.split():
        for letra in palabra:
            if letra in diccionario:
                print(diccionario[letra], end=" ")
            else:
                print(letra, end=" ")
        print(end=" ")

def traductor_inverso(texto):
    for palabra in texto.split(" "):
            prueba = str(palabra.capitalize())
            if prueba in diccionario_inverso:
                print(diccionario_inverso[prueba], end="")
            else:
                print(prueba, end="")
            print(end=" ")

if __name__ == '__main__':
    texto = input("Introduzca un texto: ")
    traductor(texto.upper())
    texto = input("\nIntroduzca un texto: ")
    traductor_inverso(texto)

    

