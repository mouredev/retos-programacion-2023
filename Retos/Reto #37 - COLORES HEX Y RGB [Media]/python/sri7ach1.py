'''
 * Crea las funciones capaces de transformar colores HEX
 * a RGB y viceversa.
 * Ejemplos:
 * RGB a HEX: r: 0, g: 0, b: 0 -> #000000
 * HEX a RGB: hex: #000000 -> (r: 0, g: 0, b: 0)
'''
def hexToRgb(hexString):
    try:
        # remove "#" if is present
        if hexString.startswith("#"):
            hexString=hexString[1:]
        # convert hex to rgb
        r=int(hexString[0:2],16)
        g=int(hexString[2:4],16)
        b=int(hexString[4:6],16)
        return(r,g,b)
    except ValueError:
        raise ValueError("Invalid input. Check HEX code.")

def rgbToHex(rgbString):
    try:
        if any(value < 0 or value > 255 for value in rgbString):
            raise ValueError("Invalid input. RGB values are between 0 and 255.")
        # convert rgb to hex
        hexString="#{:02X}{:02X}{:02X}".format(rgbString[0],rgbString[1],rgbString[2])
        return hexString
    except ValueError as error:
        raise ValueError(str(error))
    
def main():
    while True:
        # menu
        print("Options: ")
        print("1. Convert HEX to RGB")
        print("2. Convert RGB to HEX")
        print("3. Exit")
        option=input("Select 1/2/3: ")
        # start hex to rgb
        if option=='1':
            hexValue=input("Insert your HEX: ")
            try:
                rgb=hexToRgb(hexValue)
                print("RGB value is: ",rgb)
            except ValueError as error:
                print(str(error))
        # start rgb to hex
        elif option=='2':
            try:
                r=int(input("Insert your R value: "))
                g=int(input("Insert your G value: "))
                b=int(input("Insert your B value: "))
                rgb=(r,g,b)
                hexValue=rgbToHex(rgb)
                print("HEX value is: ",hexValue)
            except ValueError as error:
                print(str(error))
        # exit option
        elif option == '3':
            print("Exit done...")
            break
        else:
            print("Input not valid.")
if __name__ == "__main__":
    main()
