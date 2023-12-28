class encryptionCesar :
    def __init__(self, displace: int) :
        self.alfabeto = "abcdefghijklmnñopqrstuvwxyz"
        self.displace = displace

    def encodeC(self, text: str, option: int):
        texto = ''
        for letra in text:
            if letra in self.alfabeto:
                ubicacion = (self.alfabeto.index(letra) + (self.displace if option == 1 else - self.displace)) % len(self.alfabeto)
                texto += self.alfabeto[ubicacion]
            else:
                texto += letra
        return texto

    def main(self):
        close = True
        while close == True:
            print("Que desea realizar:\n1. Encriptar\n2. Desencriptar\n3. Salir")
            option = input("Escoja una opción (1, 2 ó 3): ")
            if int(option) == 1 or int(option) == 2 :
                text = input("Ingrese texto: ")
                rpta = self.encodeC(text.lower(), int(option))
                print(rpta)
                close = False
            if int(option) == 3 :
                close = False


if __name__ == '__main__':
    try:
        print("Bienvenido al Cifrador Cesar\nPara el desplazamiento de caracteres,")
        val = int(input("Ingrese un numero entero: "))
        if val > 0 :
            encoder = encryptionCesar(val)
            encoder.main()
        else:
            print('Valor incorrecto')
    except:
        print('Valor incorrecto')