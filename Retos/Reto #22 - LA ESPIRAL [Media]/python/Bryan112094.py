class spiral():
    def __init__(self, num: int):
        self.lado = ["═", "╗", "║", "╝", "╚", "╔"]
        self.num = num
        self.mitad = (self.num + 1) // 2

    def inicio(self):
        if self.num > 1:
            for x in range(self.mitad):
                if x == 0:
                    print(f"{self.lado[0] * (self.num - 1)}{self.lado[1]}")
                else:
                    print(f"{self.lado[2] * (x - 1)}{self.lado[5]}{self.lado[0] * (self.num - (x * 2) - 1)}{self.lado[1]}{self.lado[2] * x}")
            for y in range(self.mitad, self.num):
                print(f"{self.lado[2] * (self.num - (1 + y))}{self.lado[4]}{self.lado[0] * ((y * 2) - self.num)}{self.lado[3]}{self.lado[2] * (self.num - (1 + y))}")
        else:
            print("═")

def main():
    try:
        print("Dibujar Espiral")
        numero = int(input("Ingrese el tamaño del lado: "))
        if numero > 0:
            dibujo = spiral(numero)
            dibujo.inicio()
        else:
            print("Ingrese números mayores a 0")
    except:
        print('Ingreses solo números enteros')

if __name__=="__main__":
    main()
