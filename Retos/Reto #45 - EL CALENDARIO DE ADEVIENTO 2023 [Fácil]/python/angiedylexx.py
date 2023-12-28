import random 

class calendarioAdvento: 
    def __init__(self):
        self.participantes = []     
    def mostrar_menu(self): 
        print("1. Añadir participante")
        print("2. Mostrar participantes")
        print("3. Eliminar participante")
        print("4. Realizar sorteo")
        print("5. SALIR")
    
    def añadirParticipante(self, nombre):
        nombre = nombre.lower()
        if nombre not in self.participantes: 
            self.participantes.append(nombre) 
            print (f"Participante {nombre} añadido")
        else :
            print ("El participante ya existe")

    def mostrarParticipantes(self):
        print("Participantes:")
        print("\n".join(self.participantes)) #Join(), concatena los nobres con una salto de linea

    def eliminarParticipante(self, nombre):
        if nombre in self.participantes: 
            self.participantes.remove(nombre) 
            print (f"Participante {nombre} eliminado")
        else :
            print ("El participante no encontrado")

    def realizarSorteo(self):
        if not self.participantes:
            print("No hay participantes para realizar el sorteo")
        else:
            random.shuffle(self.participantes)
            ganador = self.participantes.pop()
            print(f"¡El participante ganador es: {ganador}!")
 
calendario = calendarioAdvento()

while True: #puesto solo se sale , al oprimir salir

    calendario.mostrar_menu()
    seleccion = input("Selecciona una opción (1-5):")

    if seleccion == "1":
        calendario.añadirParticipante(input("Introduce el nombre del participante: "))
    elif seleccion == "2":
        calendario.mostrarParticipantes()
    elif seleccion == "3":
        calendario.eliminarParticipante(input("Introduce el nombre del participante a eliminar: "))
    elif seleccion == "4":
        calendario.realizarSorteo()
    elif seleccion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Intentalo de nuevo")