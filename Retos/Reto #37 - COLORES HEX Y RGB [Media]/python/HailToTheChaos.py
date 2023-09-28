'''
 Crea las funciones capaces de transformar colores HEX
 a RGB y viceversa.
 Ejemplos:
 RGB a HEX: r: 0, g: 0, b: 0 -> #000000
 HEX a RGB: hex: #000000 -> (r: 0, g: 0, b: 0)
 '''

def hex2rgb(hex:str) -> dict:
    '''La función `hex2rgb` toma un código de color hexadecimal como entrada y devuelve un diccionario que
    contiene los valores RGB correspondientes.
    
    Parametros
    ----------
    hex : str
        El parámetro "hex" es una cadena que representa un código de color hexadecimal.
    
    Returns
    -------
        La función `hex2rgb` devuelve un diccionario con las claves 'r', 'g' y 'b' que representan los
    valores rojo, verde y azul respectivamente. Si hay un ValueError que indica un valor hexadecimal no
    válido, la función devuelve Ninguno.
    
    '''
    try:
        r = int(hex[1:3], 16)
        g = int(hex[3:5], 16)
        b = int(hex[5:8], 16)

        return {'r':r, 'g':g, 'b':b}
    
    except ValueError as error:
        print(f'Error: {error}')
        return None

def rgb2hex(r,g,b) -> str:
    '''La función `rgb2hex` convierte valores RGB a un código de color hexadecimal.
    
    Parametros
    ----------
    r
        El parámetro "r" representa el componente rojo del color RGB.
    g
        El parámetro `g` representa el componente verde del color RGB.
    b
        El parámetro "b" representa el componente azul del color RGB.
    
    Returns
    -------
        La función `rgb2hex` devuelve una cadena que representa el código de color hexadecimal en el
    formato "#RRGGBB", donde RR, GG y BB son los valores hexadecimales de los componentes rojo, verde y
    azul respectivamente.
    
    '''
    return f"#{hex(r)[2:]}{hex(g)[2:]}{hex(b)[2:]}".upper()

def main():
    opcion = int(input('1 - HEX to RGB, 2 - RGB to HEX: '))

    match opcion:
        case 1:
            hex_value = input('Hex color (E.g.: #3250A8): ')
            rgb = hex2rgb(hex_value)
            print(f'{hex_value} -> {rgb}')

        case 2:
            r = int(input('R (0-255): '))
            g = int(input('G (0-255): '))
            b = int(input('B (0-255): '))

            hex_value = rgb2hex(r, g, b)
            print(f'(r: {r}, g: {g}, {b}: 0) -> {hex_value}')

if __name__ == "__main__":
    main()
