
"""
/*
 * Crea las funciones capaces de transformar colores HEX
 * a RGB y viceversa.
 * Ejemplos:
 * RGB a HEX: r: 0, g: 0, b: 0 -> #000000
 * HEX a RGB: hex: #000000 -> (r: 0, g: 0, b: 0)
 */
"""

def hexToRgb (string):
    cleanString = string.removeprefix("#")
    lista = list(cleanString)
    r = lista[0:2]
    g = lista[2:4]
    b = lista[4:6]
    rstring = "".join(r)
    gstring = "".join(g)
    bstring = "".join(b)
    listRGB = [int(rstring,16),int(gstring,16),int(bstring,16)]
    for index,number in enumerate(listRGB):
        match index:
            case 0: 
                print("R:",number)
            case 1: 
                print("G:",number)
            case 2:
                print("B:",number)
def RgbToHex (lista):
    listahex = []
    for index,color in enumerate(lista):
        if (len(hex(color))==4):
            listahex.append(hex(color).removeprefix("0x"))
            print(hex(color))
        else:
            listahex.append("0"+hex(color).removeprefix("0x"))
    stringhex = "".join(listahex)
    stringhex = "#"+stringhex
    print(stringhex)
def showMenu():
    print("Opcion 1: Transformar HEX a RGB")
    print("Opcion 2: Transformar RGB a HEX")
    print("Opcion 3: Salir")

while True:
   showMenu()
   useroption = input("Introduzca Opcion: ")
   match useroption:
        case "3":
            break
        case "1":
            string = input("Introduzca el numero hexadecimal (ej. #090023): ")
            hexToRgb(string)
        case "2":
            listaRGB =[]
            R = int(input("Introduzca el valor de R: "))
            G = int(input("Introduzca el valor de G: "))
            B = int(input("Introduzca el valor de B: "))
            listaRGB.append(R)
            listaRGB.append(G)
            listaRGB.append(B)
            RgbToHex(listaRGB)
        case default:
            print("Elija una opcion correcta (1,2 o 3)")