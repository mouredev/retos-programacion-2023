import numpy as np
from rich import print
from rich.text import Text
from rich.panel import Panel

def toOctal(numeroDecimal: int):
    
    # Primero crearemos un arreglo de residuos para guardar cada residuo de la divison.
    residuos:list = []
    # Se crea la variable:str numeroOctal, que nos servira para almacenar y concatenar los valores.
    numeroOctal:str = ''
    
    # Definimos la potencia base en la que estaremos trabajando.
    potencia:int = 8
    # Se realiza la primera division del numero decimal que pasamos como parametro entre la variable potencia:int
    # la cual tiene el valor de 8 y la almacenamos en la variable resdivision.
    resdivision:int = int(np.divide(numeroDecimal, potencia))

    # Aqui obtenemos el residuo de la division actual, el cual almacenaremos en el arreglo de residuos. 
    residuo:int = int(np.remainder(numeroDecimal, potencia))
    residuos.append(residuo)

    # Se hace un ciclo while hasta que la division sea 0.
    while resdivision != 0:
        # El residuo sera igual al valor de residivison divido entre la potencia.
        residuo:int = int(np.remainder(resdivision, potencia))
        # resdivison ahora sera igual al valor actual de resdivison entre la potencia.
        resdivision:int = int(np.divide(resdivision, potencia))
        # se hace el append del residuo acutal en residuos.
        residuos.append(residuo)

    # Una vez que el ciclo while termino, ejectuaremos la funcion reverse sobre el arreglo de residuos, ya que
    # para la conversion de un numero octal, se puede leer simplemente los residuos de las divisiones al reves para obtener el valor octal.
    residuos.reverse()
    for e in residuos:
        # por ultimo concatenaremos cada residuo del arreglo a nuestra variable numeroOctal
        numeroOctal += str(e)

    print(f'[chartreuse3] El numero decimal [slate_blue1]{numeroDecimal}[/slate_blue1] en Octal es: [slate_blue3]{numeroOctal}[/slate_blue3] 🔢[/chartreuse3]')


def toHex(numeroDecimal: int):

    # Primero crearemos una variable:str inicializada con los caracteres '0x'
    numeroHex = '0x'
    
    # Crearemos un arreglo de residuos para guardar cada residuo de la divison.
    residuos = []

    # Crearemos un diccionario en el cual definiremos los valores numericos respectivos a cada letra.
    letterValues = {
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F',
    }
   
    # Definiremos la potencia base en la que se estara trabajando.
    potencia:int = 16

    # Se realiza la primera division del numero decimal que pasamos como parametro entre la variable potencia:int
    # la cual tiene el valor de 16 y la almacenamos en la variable resdivision.
    resdivision = int(np.divide(numeroDecimal, potencia))

    # Aqui obtenemos el residuo de la division actual, el cual almacenaremos en el arreglo de residuos. 
    residuo = int(np.remainder(numeroDecimal, potencia))
    residuos.append(residuo)
    
    # Se hace un ciclo while hasta que la division sea 0.
    while resdivision != 0:
        # El residuo sera igual al valor de residivison divido entre la potencia.
        residuo = int(np.remainder(resdivision, potencia))

        # En este paso verificaremos si el valor del residuo se encuentra dentro de nuestro diccionario que va del 10 al 15 
        if residuo in letterValues.keys():
        # Si se encuentra se almacenara el valor respectivo a la clave dentro del arreglo residuos  
            residuos.append(letterValues[residuo])
        else:
        # Si no se encuentra quiere decir que el residuo es un numero que va del 0 al 9 y haremos el append a nuestro arreglo residuos.
            residuos.append(residuo)

        # Resdivison ahora sera igual al valor actual de resdivison entre la potencia.
        resdivision = int(np.divide(resdivision, potencia))

    # Una vez que el ciclo while termino, ejectuaremos la funcion reverse sobre el arreglo de residuos, ya que
    # al igual que para los octales, en la conversion hexadecimal, tambien se pueden leer el valor hexadecimal con los residuos al reves. 
    residuos.reverse()
    for i in residuos:
        # por ultimo concatenaremos cada residuo del arreglo el nuestra variable numeroHex. Ej.Output: 0x****
        numeroHex += str(i)

    print(
        f'[chartreuse3] El numero decimal [slate_blue1]{numeroDecimal}[/slate_blue1] en Hexadecimal es: [slate_blue3]{numeroHex}[/slate_blue3] 🔢[/chartreuse3]')


def main(numeroDecimal: int):
    toOctal(numeroDecimal)
    toHex(numeroDecimal)

def onInput():
   error = Text(text='Error: Solo puedes ingresar valores numericos 🚫, intentalo de nuevo.', style='red')
   
   try:
      numeroDecimal = int(input());
      main(numeroDecimal);
   except:
      print(error);
      onInput();
       
if __name__ == "__main__":

    # * Reto *#
    # * Crea una función que reciba un número decimal y lo trasforme a Octal y Hexadecimal. *#
    # * No está permitido usar funciones propias del lenguaje de programación que *#
    # * realicen esas operaciones directamente. *#

    
    # variable para detener el programa. 
    run: bool = True
    
    # Diseño de terminal
    title = Text(text='- 🔢 Bienvenido al convertidor ! 🔢 -', style='bold purple4', justify='center')
    panel = Panel(title)
    print(panel)
    
    subtitle = Text(text='Ingresa el numero decimal que deseas convertir: ', style='dark_sea_green4')
    while run:
      print(subtitle)

      # Este es el punto de inicio del programa.
      onInput()

      print('[dark_sea_green4]¿Quieres convertir mas numeros? (y/N) [/dark_sea_green4]')
      repeat = input()
      if repeat == 'n' or repeat == 'N':
          print('[white]¡ Hasta Luego ! 👋[/white]')
          run = False
