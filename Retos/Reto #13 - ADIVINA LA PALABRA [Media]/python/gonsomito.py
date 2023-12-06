"""
Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos:
 ! El juego comienza proponiendo una palabra aleatoria incompleta: Por ejemplo "m_ur_d_v", y el número de intentos que le quedan
 ! El usuario puede introducir únicamente una letra o una palabra (de la misma longitud que la palabra a adivinar)
 ! Si escribe una letra y acierta, se muestra esa letra en la palabra. Si falla, se resta uno al número de intentos
 ! Si escribe una resolución y acierta, finaliza el juego, en caso contrario, se resta uno al número de intentos
 ! Si el contador de intentos llega a 0, el jugador pierde
 ! La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar ocultando más del 60%
 ! Puedes utilizar las palabras que quieras y el número de intentos que consideres
"""
import random

def palabra_aleatoria(): #Parto de una tupla de 40 palabras de mínimo 5 letras. Escojo una al "azar" y se devuelve en minúsculas
    listado_palabras = ("Impactante", "Mental", "Menta", "Estrella", "Aterrador", "Pitón", "Pandilla", "Victima",
                        "Asqueroso", "Obtenible", "Empapado", "Distrito", "Terror", "Reproductor", "Hombre", "Glotón",
                        "Original", "Pelea", "Puños", "Furioso", "Frente", "Rodear", "Herencia", "Medición", "Elefante,",
                        "Bendecir", "Ilustración", "Delirante", "Mutación", "Clima",  "Explicación", "Aliento",
                        "Expiación", "Rehén", "Invitado", "Helado", "Soltar", "Nuclear", "Maldad", "Sustancial")
    return listado_palabras[random.randint(0, len(listado_palabras)-1)].lower()

def palabra_aleatoria_incompleta(palabra_a_trocear):            #coloca '_' al chou por la palabra recibida
    total_ocultar=int(len(palabra_a_trocear)*60/100)            #oculta no más del 60% de la palabra dada
    letras_que_saco={}                                          #me guardo diccionario para localizar las letras despues
    while total_ocultar > palabra_a_trocear.count("_"):
        index = random.randint(0, len(palabra_a_trocear)-1)     #lanzo el random para ver que indice guardo y sustituyo
        if palabra_a_trocear[index] != "_":
            letras_que_saco[index] = palabra_a_trocear[index]
            palabra_a_trocear=palabra_a_trocear.replace(palabra_a_trocear[index] , "_", 1)
    lista_palabra_adiv  = [palabra_a_trocear,letras_que_saco]
    return lista_palabra_adiv

def adivinar_palabra(palabra_ok, pal_b_a): #recibo la palabra buena y el array con los huecos y las letras por resolver
    intento = 5 
    while palabra_ok != pal_b_a[0] and intento>0:
       # print(pal_b_a)
        print(f"Te quedan {intento} intentos para adivinar.")
        letra=str(input("\nDame una letra o la palabra completa para resolver ").lower())
        if letra=="":                                          #control de ENTER / caracter vacío
            print("Debes dar al menos un carácter que comprobar. Te penalizo por no estar atento al juego.")
            intento = intento - 1 
        elif len(letra) == len(palabra_ok):                     #entro al meter palabra de longitudes iguales
            if letra == palabra_ok:
                print("PALABRA CORRECTA\n¡¡¡HAS GANADO!!!")
                return                                          #fin del juego por advinación de palabra completa
            else:
                print("SIGUE PROBANDO\n")
                intento = intento - 1                           #-----------------------------------------------
        else:
            if letra[0] in pal_b_a[1].values():                 #si meto varias letras cojo sólo la primera -> letra[0]
                for item in pal_b_a[1].items():
                    if item[1] == letra[0]:
                        posicion = item[0]
                print(f"LETRA {letra[0]} CORRECTA")             #si la letras es buena sale del array letras y vuelve al array palabra
                pal_b_a[0] = pal_b_a[0][:posicion] + letra[0] + pal_b_a[0][posicion+1:]
                del pal_b_a[1][posicion]                        #lo borro para que no lo vuelva a iterar
                print(pal_b_a[0])
            else:
                intento= intento-1
    if intento==0 and palabra_ok != pal_b_a:
        print("\n\n¡¡¡HAS PERDIDO!!!")                  #perder por agotar intentos
        print(f"LA PALABRA ES {palabra_ok}")
    elif palabra_ok == pal_b_a[0] and intento>0:
        print("\n\n¡¡¡HAS GANADO!!!")                   #ganar por adivinar todas letras
        print(f"LA PALABRA ES {palabra_ok}")
    return palabra_ok

#------------------------------------------------------ Lanzamos el main. Genera una palabra a resolver, 
palabra = palabra_aleatoria()
palabras_incompleta = palabra_aleatoria_incompleta(palabra)
print("LA PALABRA A RESOLVER ES: ", palabras_incompleta[0])
adivinar_palabra(palabra, palabras_incompleta)
