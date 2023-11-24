# """
#  * ¿Conoces el calendario de aDEViento de la comunidad (https://adviento.dev)?
#  * 24 días, 24 regalos sorpresa relacionados con desarrollo de software.
#  * Desde el 1 al 24 de diciembre.
#  *
#  * Crea un programa que simule el mecanismo de participación:
#  * - Mediante la terminal, el programa te preguntará si quieres añadir y borrar
#  *   participantes, mostrarlos, lanzar el sorteo o salir.
#  * - Si seleccionas añadir un participante, podrás escribir su nombre y pulsar enter.
#  * - Si seleccionas añadir un participante, y este ya existe, avisarás de ello.
#  *   (Y no lo duplicarás)
#  * - Si seleccionas mostrar los participantes, se listarán todos.
#  * - Si seleccionas eliminar un participante, podrás escribir su nombre y pulsar enter.
#  *   (Avisando de si lo has eliminado o el nombre no existe)
#  * - Si seleccionas realizar el sorteo, elegirás una persona al azar 
#  *   y se eliminará del listado.
#  * - Si seleccionas salir, el programa finalizará.
# """

import sqlite3
import random

#CREAR BASE DE DATOS
# Conectar a base de datos o crear si no existe
conn = sqlite3.connect('participantes.db')
# Crear un cursor
cursor = conn.cursor()
# Crear una tabla
cursor.execute('''CREATE TABLE IF NOT EXISTS participantes (nombre VARCHAR(50))''')


#FUNCIONES READ/UPDATE/DELETE
# Insertar participante
def a_participante(nombre):
    # Comprobar si el participante ya existe
    cursor.execute("SELECT * FROM participantes WHERE nombre=?", (nombre,))
    if cursor.fetchone() is not None:
        print("Ya existe el participante")
    # Si no existe, añadirlo
    else:
        cursor.execute("INSERT INTO participantes VALUES (?)", (nombre,))
        print("Participante añadido")
# Eliminar participante
def rm_participante(nombre):
    # Comprobar si el participante existe
    cursor.execute("SELECT * FROM participantes WHERE nombre=?", (nombre,))
    if cursor.fetchone() is not None:
        cursor.execute("DELETE FROM participantes WHERE nombre=?", (nombre,))
        print("Participante eliminado")
    # Si no existe, mostrar mensaje
    else:
        print("No existe el participante")
# Mostrar participantes
def m_participante():
    # Comprobar si hay participantes
    cursor.execute("SELECT * FROM participantes")
    participants = cursor.fetchall()
    if participants:
        print("Participantes:")
        for participant in participants:
            print(participant[0])
    else:
        print("No hay participantes")
# Elegir participante ganador
def get_ganador():
    cursor.execute("SELECT * FROM participantes")
    participantes = cursor.fetchall()
    # Si hay participantes, elegir uno al azar y eliminarlo
    if participantes:
        winner = random.choice(participantes)
        cursor.execute("DELETE FROM participantes WHERE nombre=?", (winner[0],))
        print("El ganador:", winner[0])
    # Si no hay participantes, mostrar mensaje
    else:
        print("No hay participantes")

while True:
    print("\n--- Menú ---")
    print("1. Agregar participante")
    print("2. Remover participante")
    print("3. Mostrar participantes")
    print("4. Elegir ganador")
    print("5. Salir")
    print("------------")
    el = input("Elige opción (1-5): ")

    if el == "1":
        nombre = input("Ingresa nombre del participante a añadir: ")
        a_participante(nombre)
    elif el == "2":
        nombre = input("Ingresa nombre del participante a eliminar: ")
        rm_participante(nombre)
    elif el == "3":
        m_participante()
    elif el == "4":
        get_ganador()
    elif el == "5":
        break
    else:
        print("Elije una opción válida")

# Cerrar conexión
conn.commit()
conn.close()


