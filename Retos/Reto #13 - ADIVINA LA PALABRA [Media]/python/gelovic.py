from random import choice, randrange

intentos = 3
palabras = 'melifluo,inefable,etereo,limerencia,serendipia,arrebol,iridiscencia,elocuencia,efimero,inmarcesible,perenne,ojala,luminiscencia,compasion,infinito,soledad,resilencia,melancolia,efervescencia,alba,aurora,honestidad,inexorable,madre,reciprocidad,saudade,esperanza,mondo,ademan,bonhomia,nefelibata,ataraxia,tiquismiquis,osculo,trapisonda,acme,jipiar,uebos,agibilibus'.split(',')

def genera():
    global palabra, oculta
    
    palabra = choice(palabras) # elegimos una palabra al azar
    oculta = list(palabra) # convertimos la palabra en una lista de letras para poder modificarla
    
    for i in range(int(len(palabra)*.6)): # ocultamos como máximo el 60% de las letras (pueden repetirse algunas)
        oculta[randrange(len(palabra))] = '_'

    oculta = ''.join(oculta) # convertimos la lista de letras en una cadena de texto

def comprueba():
    global palabra, oculta, intentos
    
    intento = input('introduce una letra o la solución: ').lower() # pedimos una letra al usuario

    # comprobamos si la letra está en la palabra o si ha acertado la palabra entera
    if len(intento) == 1 and intento in palabra:      
        oculta = ''.join([intento if intento == palabra[i] else oculta[i] for i in range(len(palabra))])
        return
    elif intento == palabra:
        oculta = palabra
        return
    intentos -= 1 # si no ha acertado, restamos un intento

def main():
    genera() # generamos la palabra y ocultamos algunas letras

    # mientras queden intentos y no se haya acertado la palabra, pedimos una letra
    while intentos > 0 and oculta != palabra:
        print(oculta, f'\nintentos: {intentos}')
        comprueba() # comprobamos el intento del usuario
    
    final = 'ganado' if oculta == palabra else 'perdido'
    print(f'¡Has {final}!\nLa palabra era "{palabra}"')

if __name__ == '__main__':
    main()
    




    