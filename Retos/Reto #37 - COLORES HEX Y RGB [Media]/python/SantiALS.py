'''
/*
 * Crea las funciones capaces de transformar colores HEX
 * a RGB y viceversa.
 * Ejemplos:
 * RGB a HEX: r: 0, g: 0, b: 0 -> #000000
 * HEX a RGB: hex: #000000 -> (r: 0, g: 0, b: 0)
 */
 '''

def rgb(r, g, b):

    correction = [r,g,b]
    
    for x in range(len(correction)):
        if correction[x] < 0:
            correction[x] = 0
        elif correction[x] > 255:
            correction[x] = 255
        

    return ('#{:02X}{:02X}{:02X}'.format(correction[0],correction[1],correction[2]))

def hex(number: str):

    number = number.replace('#','')
    
    new_list = [number[index:index+2] for index in range(0, len(number), 2)]
        

    return ('r: {:n}, g: {:n}, b: {:n}'.format(int(new_list[0],16),int(new_list[1],16),int(new_list[2],16)))

if __name__ in '__main__':
    
    print('FORMATO RGB:',rgb(0, 0, 0))
    print('FORMATO HEXADECIMAL:',hex('#000000'))
    print('FORMATO RGB:',rgb(255, 255, 255))
    print('FORMATO HEXADECIMAL:',hex('#FFFFFF'))
    print('FORMATO RGB:',rgb(254, 253, 252))
    print('FORMATO HEXADECIMAL:',hex('#FEFDFC'))
    print('FORMATO RGB:',rgb(-20, 275, 125))
    print('FORMATO HEXADECIMAL:',hex('#00FF7D'))

