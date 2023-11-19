"""
 * Este es un reto especial por Halloween.
 * Te encuentras explorando una mansión abandonada llena de habitaciones.
 * En cada habitación tendrás que resolver un acertijo para poder avanzar a la siguiente.
 * Tu misión es encontrar la habitación de los dulces.
 *
 * Se trata de implementar un juego interactivo de preguntas y respuestas por terminal.
 * (Tienes total libertad para ser creativo con los textos)
 *
 * - 🏰 Casa: La mansión se corresponde con una estructura cuadrada 4 x 4
 *   que deberás modelar. Las habitaciones de puerta y dulces no tienen enigma.
 *   (16 habitaciones, siendo una de entrada y otra donde están los dulces)
 *   Esta podría ser una representación:
 *   🚪⬜️⬜️⬜️
 *   ⬜️👻⬜️⬜️
 *   ⬜️⬜️⬜️👻
 *   ⬜️⬜️🍭⬜️
 * - ❓ Enigmas: Cada habitación propone un enigma aleatorio que deberás responder con texto.
 *   Si no lo aciertas no podrás desplazarte.
 * - 🧭 Movimiento: Si resuelves el enigma se te preguntará a donde quieres desplazarte.
 *   (Ejemplo: norte/sur/este/oeste. Sólo deben proporcionarse las opciones posibles)
 * - 🍭 Salida: Sales de la casa si encuentras la habitación de los dulces.
 * - 👻 (Bonus) Fantasmas: Existe un 10% de que en una habitación aparezca un fantasma y
 *   tengas que responder dos preguntas para salir de ella.
"""
import os, time, random
import numpy as np

#constantes
INGRESAR = 1
SALIR = 2

PROB_FANTASMA = 0.1

ARRIBA = 1
ABAJO = 2
IZQUIERDA = 3
DERECHA = 4

#enigmas y respuestas
ENIGMAS = np.array([['Casa con dos cuartos, nueva cada mes y otras veces llena: adivina quién es.','luna' ],
                    ['Tengo cabeza redonda, sin nariz, ojos, ni frente, y mi cuerpo se compone tan solo de blancos dientes.', 'ajo'],
                    ['Salgo de la habitación y entro en la cocina meneando la cola como una gallina.', 'escoba'],
                    ['Ya se fue el verano y otra estación llega: como lluvia de oro caen hojas secas.','Otoño'],
                    ['Estudiante que estudias a la luz de una vela, ¿qué animal no es un ave, tiene colmillo y como ella vuela?','murcielago'],
                    ['Duros como las piedras, para el perro un buen manjar, y sin ellos no podrías ni saltar ni caminar','hueso'],
                    ['Envuelta en vendas, camina con las patas tiesas. Y duerme en su tumba, rodeada de muchas ofrendas. La verás en los libros de historia, seguro que ya sabes que hablo de la …','momia'],
                    ['Mi madre prepara una crema naranja, pero hoy le ha dibujado una cara. Con cuidado, quítale la tapa y enciende una vela para ver la …','calabaza']])
#fin constantes

#clases
class Mansion:   
    dimension = {
        'salas': 4,
        'pisos': 4
    }       
    
    fantasma_1 = {
        'sala': 0,
        'piso': 0
    }
    
    fantasma_2 = {
        'sala' : 0,
        'piso' : 0
    }
    
    dulces = {
        'sala': 0,
        'piso': 0
    }
    
    def __init__(self):
        pass

    def dibujar_casa(self,jugador):
        #dibuja el mapa, no se incluyen los fantasmas ni el dulce
        for piso in range(1, self.dimension.get('pisos')+1):
            for sala in range(1, self.dimension.get('salas')+1):
                if (piso == 1) and (sala ==1):
                    print("🚪\t",end="")
                elif (piso == jugador.get('piso')) and (sala == jugador.get('sala')):
                    print("😊\t",end="")
                else:    
                    print("🟥\t", end="")
            print('')

    def dibujar_super_casa(self,jugador):
        #dibuja el mapa, no se incluyen los fantasmas ni el dulce
        for piso in range(1, self.dimension.get('pisos')+1):
            for sala in range(1, self.dimension.get('salas')+1):
                if (piso == 1) and (sala ==1):
                    print("🚪\t",end="")
                elif (piso == jugador.get('piso')) and (sala == jugador.get('sala')):
                    print("😊\t",end="")
                elif (piso == self.fantasma_1.get('piso')) and (sala == self.fantasma_1.get('sala')):  
                    print("👻\t",end="")   
                elif (piso == self.fantasma_2.get('piso')) and (sala == self.fantasma_2.get('sala')):  
                    print("👻\t",end="") 
                elif (piso == self.dulces.get('piso')) and (sala == self.dulces.get('sala')):  
                    print("🍬\t",end="")     
                else:    
                    print("🟥\t", end="")
            print('')
    
class Jugador:
    nombre = ''
    posicion = {
        'sala': 1,
        'piso': 1
    }   
    
    def __init__(self, nombre):
        self.nombre = nombre

    
    def actualizar_posicion(self, posicion): 
      self.posicion = posicion  

    def mover(self, movimiento):
        if movimiento == ARRIBA:
            self.posicion['piso'] = self.posicion.get('piso') - 1
        elif movimiento == ABAJO:
            self.posicion['piso'] = self.posicion.get('piso') + 1
        elif movimiento == IZQUIERDA:
            self.posicion['sala'] = self.posicion.get('sala') - 1
        elif movimiento == DERECHA:
            self.posicion['sala'] = self.posicion.get('sala') + 1
#fin clases  

#funciones
def opciones_movimiento(posicion_actual, dimension_mansion):
    arriba    = posicion_actual.get('piso') > 1
    abajo     = posicion_actual.get('piso') < dimension_mansion.get('pisos')
    izquierda = posicion_actual.get('sala') > 1
    derecha   = posicion_actual.get('sala') < dimension_mansion.get('salas')   
    
    print('En qué posición desea moverse?')
    opciones = []
    if arriba:
        print('{0}- Arriba ↑'.format(ARRIBA))
        opciones.append(ARRIBA)

    if abajo:
        print('{0}- Abajo ↓'.format(ABAJO))
        opciones.append(ABAJO)

    if izquierda:
        print('{0}- Izquierda ←'.format(IZQUIERDA))
        opciones.append(IZQUIERDA)
    
    if derecha:
        print('{0}- Derecha →'.format(DERECHA))
        opciones.append(DERECHA)
    
    opcion_valida = False
    fallas = 0
    while(not opcion_valida):
        fallas = fallas + 1
        
        if fallas == 4:
            imprimir_por_letra('La Mansión se ha derrumbado...')
            exit()
    
        try:
            opcion = int(input(':'))
            
            if opcion in opciones:
                opcion_valida = True
                return opcion
            else:
                print('Seleccoine una de las opciones')
        except:        
            print('Ingrese el número de una de las opciones')


def calcular_posi_fantasma(dimension_mansion):
    piso = random.randint(1,dimension_mansion.get('pisos'))
    if piso > 1:
        sala = random.randint(1, dimension_mansion.get('salas'))
    else:
      sala = random.randint(3, dimension_mansion.get('salas'))
    
    posicion = {
        'sala': sala,
        'piso': piso
    }
    
    return posicion
   

def calcular_posi_dulces(fantasma_1, fantasma_2, dimension_mansion):
    piso = random.randint(1,dimension_mansion.get('pisos'))
    if piso > 1:
        sala = random.randint(1, dimension_mansion.get('salas'))
    else:
      sala = random.randint(3, dimension_mansion.get('salas'))
    
    posicion = {
        'sala': sala,
        'piso': piso
    }
    
    if ((posicion.get('piso') == fantasma_1.get('piso') and posicion.get('sala') == fantasma_1.get('sala')) or (posicion.get('piso') == fantasma_2.get('piso') and posicion.get('sala') == fantasma_2.get('sala'))):      
        posicion = calcular_posi_dulces(fantasma_1, fantasma_2,dimension_mansion)
    
    return posicion
    
    
def imprimir_por_letra(mensaje):
    for letra in mensaje:
        print(letra, end='', flush=True)
        time.sleep(0.03) 
    print('\n')    
    
    
def hay_fantasma():   
    return PROB_FANTASMA >= round(random.random(),1)
    
    
def resolver_enigma():
    enigma_resuelto = False 
    enigma = random.randint(0, len(ENIGMAS)-1)

    while not enigma_resuelto:                         
        imprimir_por_letra('Para avanzar debes resolver el siguiente acertijo:')    
        imprimir_por_letra(ENIGMAS[enigma][0])        
        respuesta = input(': ')
        
        if ENIGMAS[enigma][1].upper() in respuesta.upper():
            enigma_resuelto = True
            imprimir_por_letra('Perfecto!')
        else:
            imprimir_por_letra('Tienes otra oportunidad.. Inténtalo de vuelta!')    
#fin funciones                      

def inciar_juego():
    os.system('cls')   
    imprimir_por_letra('Para poder interactuar con el juego ingrese el número de la opción que se le presenta...') 
    imprimir_por_letra('Esta a punto de ingresar a la Mansión...')

    try:
        opcion = int(input('Desea ingresar? \n {0}- Si \n {1}- No \n :'.format(INGRESAR,SALIR)))
    
        if opcion == INGRESAR:
            nombre = ''
            os.system('cls')
            while len(nombre) < 4:
                nombre = input('Ingresa tu nombre: ')
                if len(nombre) < 4:
                    print('El nombre debe tener al menos 4 letras')
            
            #carga la posicion de los fantasmas y la sala de dulces en la mansion
            mansion = Mansion()                                      
            mansion.fantasma_1 = calcular_posi_fantasma(mansion.dimension)
            mansion.fantasma_2 = calcular_posi_fantasma(mansion.dimension)
            mansion.dulces     = calcular_posi_dulces(mansion.fantasma_1, mansion.fantasma_2, mansion.dimension)         
            
            jugador = Jugador(nombre)        
            
            #parte principal del juego, el mismo se ejecuta hasta que el usuario encuentre la sala de dulces, no se agrega opción de interrumpir el juego
            while jugador.posicion != mansion.dulces: 
                os.system('cls')
                mansion.dibujar_casa(jugador.posicion)

                if jugador.nombre == '0000': #para verificacion de la funcionalidad puede ingresar el nombre de jugador como 0000
                    print('****************************************************')
                    print('Jugador: {0}'.format(jugador.posicion))
                    print('f1: {0}'.format(mansion.fantasma_1))
                    print('f2: {0}'.format(mansion.fantasma_2))
                    print('dulces: {0}'.format(mansion.dulces))
                    print('****************************************************')
                        
                resolver_enigma()

                #si el jugador va a la sala de un fantasma o aparece un fantasma en la sala, se debe resolver otro enigma
                if ( (jugador.posicion in [mansion.fantasma_1, mansion.fantasma_2]) or (hay_fantasma()) ):
                    imprimir_por_letra('{0}. Ha aparecido un fantasma!!!\nDebes resolver otro acertijo.'.format(jugador.nombre))
                    resolver_enigma()
                
                #actualiza la posicion del jugador en el mapa
                jugador.mover(opciones_movimiento(jugador.posicion, mansion.dimension))                

            #fin del juego =)
            if jugador.posicion == mansion.dulces: 
                os.system('cls')
                print('******************************************************************')
                print('    Muchas felicidades {0} ha encontrado la sala de dulces..!!!'.format(jugador.nombre))    
                print('******************************************************************')    

                mansion.dibujar_super_casa(jugador.posicion)       
        
        elif opcion == SALIR: 
            print('Vuelve pronto')
        else: 
            print('La opción que ingresaste no es válida')
    except:
        print('El juego se cerró.')

if __name__ == '__main__':
    inciar_juego()             