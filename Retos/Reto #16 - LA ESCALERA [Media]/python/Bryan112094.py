# Crea una función que dibuje una escalera según su número de escalones.
# - Si el número es positivo, será ascendente de izquiera a derecha.
# - Si el número es negativo, será descendente de izquiera a derecha.
# - Si el número es cero, se dibujarán dos guiones bajos (__).
# Ejemplo: 4
#         _
#       _|       
#     _|
#   _|
# _|

class createEscalera:
    def __init__(self) -> None:
        pass
    
    # Retorna el escalon, si es positivo es hacia arriba, si no, es hacia abajo
    def escalon(self, arriba: bool) -> str:
        return "_|" if arriba else "|_"
    
    # Retorna el espacio entre los escalones
    def espacio(self, num: int, val: bool):
        espacio = "  " * num
        return espacio if val else espacio[:-1]

    # Crea la escalera llamando a la funcion escalon y espacio 
    def escalera(self, numero: int, arriba: bool):
        numEspacio = numero if arriba else 0
        inicio = 0
        
        for inicio in range(numero + 1):
            espacio = self.espacio(numEspacio, arriba)
            escalon = "_" if inicio == 0 else self.escalon(arriba)
            print(f"{espacio}{escalon}")

            numEspacio = numEspacio - 1 if arriba else numEspacio + 1

    def star(self):
        print("Creacion de escalera:\n * Número positivo, escalones ascendentes\n * Número negativo, escalones descendentes")
        try:
            numero = int(input("Ingrese el número de escalones: "))
            if numero == 0:
                print("__")
            elif numero > 0:
                self.escalera(numero, True)
            else:
                self.escalera(abs(numero), False)
                
        except ValueError:
            print("Valor ingresado es incorrecto")

escalera = createEscalera()
escalera.star()
