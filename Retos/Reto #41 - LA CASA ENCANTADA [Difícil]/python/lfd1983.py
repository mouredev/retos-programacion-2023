# /* RETO #41:  LA CASA ENCANTADA DE MOUREDEV
#  * Este es un reto especial por Halloween.
#  * Te encuentras explorando una mansión abandonada llena de habitaciones.
#  * En cada habitación tendrás que resolver un acertijo para poder avanzar a la siguiente.
#  * Tu misión es encontrar la habitación de los dulces.
#  *
#  * Se trata de implementar un juego interactivo de preguntas y respuestas por terminal.
#  * (Tienes total libertad para ser creativo con los textos)
#  *
#  * - 🏰 Casa: La mansión se corresponde con una estructura cuadrada 4 x 4
#  *   que deberás modelar. Las habitaciones de puerta y dulces no tienen enigma.
#  *   (16 habitaciones, siendo una de entrada y otra donde están los dulces)
#  *   Esta podría ser una representación:
#  *   🚪⬜️⬜️⬜️
#  *   ⬜️👻⬜️⬜️
#  *   ⬜️⬜️⬜️👻
#  *   ⬜️⬜️🍭⬜️
#  * - ❓ Enigmas: Cada habitación propone un enigma aleatorio que deberás responder con texto.
#  *   Si no lo aciertas no podrás desplazarte.
#  * - 🧭 Movimiento: Si resuelves el enigma se te preguntará a donde quieres desplazarte.
#  *   (Ejemplo: norte/sur/este/oeste. Sólo deben proporcionarse las opciones posibles)
#  * - 🍭 Salida: Sales de la casa si encuentras la habitación de los dulces.
#  * - 👻 (Bonus) Fantasmas: Existe un 10% de que en una habitación aparezca un fantasma y
#  *   tengas que responder dos preguntas para salir de ella.
#  */

def generarMansion():
    #devuelve una lista con 16 elementos de la mansion: habitaciones vacías, fantasmas random 
    #puerta de entrada y habitación de los dulces

    import random    

    vectorMansion = list('⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜')

    # vector posiciones mantiene las posiciones no asignadas
    posiciones = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    
    posicionEntrada = posiciones[random.randint(0,len(posiciones)-1)]
    # elimino las posiciones ya sorteadas, para no sobreescribir
    posiciones.remove(posicionEntrada)

    posicionDulces = posiciones[random.randint(0,len(posiciones)-1)]
    posiciones.remove(posicionDulces)
    
    vectorMansion[posicionEntrada]="🚪" #genero entrada en posicion random
    vectorMansion[posicionDulces]="🍭"    

    for pos in posiciones: #10% de probabilidad de encontrar un fantasma en los cuartos restantes
        if random.randint(0,9) == 0:
            vectorMansion[pos] = "👻"
    return vectorMansion

    
def mostrarMansionCompleta(vectorMansion):
    #función para prueba, muestra la mansion completa
    #  
    mansion = [vectorMansion[0:4],vectorMansion[4:8],vectorMansion[8:12],vectorMansion[12:16]]
    for m in mansion:
        print(m)

def mostrarMansion(vectorMansion,posicionActual,juegoTerminado):
   
    copiaMansion = vectorMansion.copy()
    print("\nEste es el plano de la Mansión Embrujada:")
    for i in range(0,len(copiaMansion)):
        if copiaMansion[i] != "🚪" :
            copiaMansion[i] = "⬜"

    copiaMansion[posicionActual]= "🧑"
    if juegoTerminado: #en caso de juegoTerminado reemplazo la persona por la habitación de los dulces
        copiaMansion[posicionActual]="🍭" 

    mansionMatriz = [copiaMansion[0:4],copiaMansion[4:8],copiaMansion[8:12],copiaMansion[12:16]]
    for m in mansionMatriz:
        print(" ".join(m))
    print("")

def obtenerMovimientosPosibles(posicionActual):
    direcciones = {
        "N":["Norte",True],
        "S":["Sur",True],
        "E":["Este",True],
        "O":["Oeste",True]
    }
    if posicionActual in [0,1,2,3]:
        direcciones["N"] = ["Norte",False]
    if posicionActual in [12,13,14,15]:
        direcciones["S"] = ["Sur",False]
    if posicionActual in [0,4,8,12]:
        direcciones["O"] = ["Oeste",False]
    if posicionActual in [3,7,11,15]:
        direcciones["E"] = ["Este",False]
    
    return direcciones #retorna diccionario con las direcciones 

def obtenerDireccion(posicionActual):
    #muestra las opciones posibles de dirección y obtiene la elección del usuario

    print("¿En qué dirección quieres desplazarte?")
    direcciones = obtenerMovimientosPosibles(posicionActual)
    opcionesDisponibles=[]

    for clave,valor in direcciones.items():
        if valor[1]:
            print(f'Ingresa {clave} para desplazarte al {valor[0]}')
            opcionesDisponibles.append(clave)    

    direccionElegida = input("-->").upper()

    if not direccionElegida in opcionesDisponibles:
        print("Opción Incorrecta")
        
    else:
        return direccionElegida


def desplazar(posicionActual,direccionElegida):
    #retorna nueva posición según la dirección elegida
    
    if direccionElegida == "N":
        posicionActual -=4
    elif direccionElegida == "S":
        posicionActual += 4
    elif direccionElegida == "E":
        posicionActual += 1
    elif direccionElegida == "O":
        posicionActual -= 1
    
    return posicionActual

def generarEnigmasPorHabitacion(mansion):
    #construye un diccionario con el nro de habitación como clave y los acertijos como valor

    import random 

    enigmas = [["5-2= ","3"],["17-7= ","10"],["98-18= ","80"],["25-20= ","5"],["50*4= ","200"],["5-2= ","3"],["17-7= ","10"],["98-18= ","80"],["25-20= ","5"],["50*4= ","200"],["5-2= ","3"],["17-7= ","10"],["98-18= ","80"],["25-20= ","5"],["50*4= ","200"],["5-2= ","3"],["17-7= ","10"],["98-18= ","80"],["25-20= ","5"],["50*4= ","200"],["5-2= ","3"],["17-7= ","10"],["98-18= ","80"],["25-20= ","5"],["50*4= ","200"],["5-2= ","3"],["17-7= ","10"],["98-18= ","80"],["25-20= ","5"],["50*4= ","200"]]

    enigmasPorHabitación = {}

    for i in range(0,len(mansion)):         
        if mansion[i] == "👻": #la habitación del fantasma tiene 2 enigmas            
            aleatorio = random.randint(0,len(enigmas)-1)            
            enigma1 =  enigmas[aleatorio]         
            del(enigmas[aleatorio]) # los enigmas utilizados se van eliminando

            aleatorio = random.randint(0,len(enigmas)-1)
            enigma2 = enigmas[aleatorio]
            del(enigmas[aleatorio])

            enigmasPorHabitación[i] = [enigma1, enigma2]
           
        elif  mansion[i] == "🚪" or mansion[i]== "🍭": #la puerta no tiene enigma
            enigmasPorHabitación[i] = []

        elif mansion[i]== "⬜": #la habitación vacía tiene un enigma
            aleatorio = random.randint(0,len(enigmas)-1)            
            enigmasPorHabitación[i] = [enigmas[aleatorio]]
            del(enigmas[aleatorio])

    return enigmasPorHabitación             


def resolverEnigmas(habitacion,mansion,enigmasPorHabitacion):
    
     
    if mansion[habitacion] == "👻" or mansion[habitacion] == "⬜": 
      #en estos casos debe responder preguntas
      
      pregunta="pregunta" #para mostrar "pregunta" o "preguntas" según corresponda
      if mansion[habitacion] == "👻":
          pregunta="preguntas"

      print(f'Para salir de esta habitación: {mansion[habitacion]} debes responder {len(enigmasPorHabitacion[habitacion])} {pregunta}')

      for i in enigmasPorHabitacion[habitacion]:
          respuesta = input(f'Responde: {i[0]}')
          if respuesta == i[1]:
              print("Respuesta correcta")
              continue
          else:
              print("Respuesta incorrecta, no puedes salir de esta habitación")
              return False #al responder incorrectamente una de las preguntas de la habitación retorna False
    return True

def juego():
    import os
    mansion = generarMansion()       
    enigmasPorHabitacion = generarEnigmasPorHabitacion(mansion)

    posicionActual = mansion.index("🚪")
    
    print("*****  Bienvenido al Juego de la Mansión Embrujada  ******")
    print("Debes moverte por las habitaciones de la Mansión Embrujada hasta encontrar la Habitación de los Dulces \nPara salir de una habitación vacía debes resolver un enigma\nPara salir de una habitación con fastasma debes resolver dos enigmas\n M ¡Mucha Suerte!!!")
    # mostrarMansionCompleta(mansion)

    while True:
        
        mostrarMansion(mansion,posicionActual,False)

        if mansion[posicionActual] == "🍭": # el juego ha terminado
            break
        
        elif resolverEnigmas(posicionActual,mansion,enigmasPorHabitacion): #si ha resuelto los enigmas
            direccionElegida = obtenerDireccion(posicionActual)                    
            if direccionElegida:
              posicionActual = desplazar(posicionActual,direccionElegida)

        else: #si no ha resuelto los enigmas
            input("Presiona una tecla para continuar")
        os.system('cls')
    
    os.system('cls')
    print("********** GANASTE!!! \n\nEncontraste la habitación de los dulces\ny lograrse salir de la Mansión Embrujada")
    mostrarMansion(mansion,posicionActual,True)
    input("Presiona una tecla para Salir")

juego()


