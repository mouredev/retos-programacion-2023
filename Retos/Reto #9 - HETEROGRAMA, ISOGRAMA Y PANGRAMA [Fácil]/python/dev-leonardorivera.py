## Autor: Leonardo Rivera
## Portafolio: https://dev-leonardorivera.github.io/portafolio/
## GitHub: https://github.com/dev-leonardorivera
## linkedin: https://www.linkedin.com/in/leonardo-rivera-a83040250



##         Reto #9: HETEROGRAMA, ISOGRAMA Y PANGRAMA
## Crea 3 funciones, cada una encargada de detectar si una cadena de
## texto es un heterograma, un isograma o un pangrama.
## - Debes buscar la definición de cada uno de estos términos.



from os import system ## importamos os de la libreria system para poder utilizar comando de consolas par limpiar la consola o hacer pausas 

abc = [] ## array de abecedario en miniscula
ABC = [] ## array de abecedario en mayuscula

for i in range(26):
    abc.append( chr(ord('a') + i)) ## llenamos el array de abecedario en miniscula
    abc.append('ñ')

for i in abc:
    ABC.append(i.upper()) ## llenamos el array de abecedario en mayuscula
    ABC.append('Ñ')

#Un heterograma es una palabra o frase que no contiene ninguna letra repetida.​ 
def heterograma(texto):
    texto = texto.lower()
    contador = 0 # variable contador
    respuesta = True ## cariable respuesta
    if(len(texto)<1): ## validamos si el teccto esta vacio tomando el largo de la variable y si es menor que 1 es por que no hay caracteres
        print('El exto introducido esta vacio')
        system('PAUSE')
        system('CLS')
        respuesta = False
    else:
        for letra1 in texto: # bucles for anidados
            for letra2 in texto:
                if(letra1 == letra2): ## si la letra coicide mas de una ves hamos un break y le decimos que es falso que es un heterograma
                    contador= contador+1
                    if(contador>1):
                        respuesta = False
                        break
            contador = 0            
    return respuesta        


# Todas las letras deben contener la misma cantidad en la palabra
def isograma(texto):
    texto = texto.lower()
    letras = {}
    respuesta = False ## cariable respuesta
    if(len(texto)<1): ## validamos si el teccto esta vacio tomando el largo de la variable y si es menor que 1 es por que no hay caracteres
         print('El exto introducido esta vacio')
         system('PAUSE')
         system('CLS')
    else:
        for letra in texto:
            if letra.isalpha():
                if letra in letras:
                    letras[letra] += 1
                else:
                    letras[letra] = 1

        if all(valor == list(letras.values())[0] for valor in letras.values()):
            respuesta = True
        else:
            respuesta = False
    return respuesta


## Es un texto que usa todas las letras posibles del alfabeto de un idioma.
def pangrama(texto):
    count = 0 ## cantidad de letras del abecedario que se encuentran en el texto
    countMax = len(abc) ## total de letras del abecedario
    porcentaje = 0 ## variable para calcular porcentaje 
    respuesta = False ## respuesta de la funcion inicia en falso 
    if(len(texto)<1): ## validamos si el teccto esta vacio tomando el largo de la variable y si es menor que 1 es por que no hay caracteres
        print('El exto introducido esta vacio')
        system('PAUSE')
        system('CLS')
    else:
        for caracter in abc: ## for que recorre el array de abecedarioen minuscula 
            if(caracter in texto): ## su el caracter se encuentra dentro de tecto aumenta el contador en uno  NOTA: esto es con letras en minuscula
                count = count+1
        for caracter in ABC: ## su el caracter se encuentra dentro de tecto aumenta el contador en uno  NOTA: esto es con letras en MAYUSCULA
            if(caracter in texto):
                count = count+1

        porcentaje = (100*count)/countMax ## sacamos un porcentaje de cuentas letras del abecedario se encuentran dentro del texto
        # print('cantidad de letras encontradas: '+str(count))
        # print('cantidad de letras: '+ str(countMax))
        # print('porcentaje: '+str(porcentaje))
        if(porcentaje>95): respuesta = True ## si el porcentaje es mayor a 95% entonces si es un pangram ya que la teoria dice que
                                            ## un texto pangrama es cuando la mayoria de las letras del avc se encuentran dentro del texto  este porcentaje se puede modificar si quieres que sea mayor o menos

    return respuesta

    

## funcion principal 
def main():
    opcion = '' ### variable para las opciones del menu
    while True:
        ## pintamos el menu
        print('  Reto #9: HETEROGRAMA, ISOGRAMA Y PANGRAMA  ')
        print('-------------------- MENU --------------------')
        
        print('- 1.- Validar HETEROGRAMA                    -')
        print('- 2.- Validar ISOGRAMA                       -')
        print('- 3.- Validar PANGRAMA                       -')
        print('- 0.- SALIR                                  -')
        opcion = input('opcion: ') ## leemos por consola
        if(opcion == '1'):
            ## opcion uno validar si es un HETEROGRAMA
            system('cls') ## limpiamos consola
            print('Heterograma es una palabra o frase que no contiene ninguna letra repetida')
            texto= input('ingrese texto:')## input de texto
            if(heterograma(texto)): ## validamos con las funciones antes creadas
                print('Heterograma: Si')
            else:
                print('Heterograma: No')
            system('PAUSE')
            system('cls')

        elif(opcion == '2'):
            ## opcion uno validar si es un ISOGRAMA
            system('cls') 
            print('Una palabra isograma es donde todas las letras deben contener la misma cantidad en la palabra')
            texto= input('ingrese texto:')## input de texto
            if(isograma(texto)):
                print('Isograma: Si')
            else:
                print('Isograma: No')
            system('PAUSE')
            system('cls')
        elif(opcion == '3'):
            ## opcion uno validar si es un PANGRAMA
            system('cls') 
            print('PANGRAMA es un texto que usa todas las letras posibles del alfabeto de un idioma.')
            texto= input('ingrese texto:')## input de texto
            if(pangrama(texto)):
                print('Pangrama: Si')
            else:
                print('Pangrama: No')
            system('PAUSE')
            system('cls')
        elif(opcion == '0'):
            break
        else:
            ## En caso de que la opcion que elija no exita se mostrara esta opcion.
            system('cls')
            print('Opcion no encontrada, intente de nuevo')
            system('PAUSE')
            system('cls')


system('cls')
main()