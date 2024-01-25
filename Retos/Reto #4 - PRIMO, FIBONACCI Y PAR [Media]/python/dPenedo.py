# # Reto #4: PRIMO, FIBONACCI Y PAR
# #### Dificultad: Media | Publicación: 23/01/23 | Corrección: 30/01/23

# ## Enunciado

# ```
# /*
#  * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
#  * Ejemplos:
#  * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
#  * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
#  */
# ```
# #### Tienes toda la información extendida sobre los retos de programación semanales en **[retosdeprogramacion.com/semanales2023](https://retosdeprogramacion.com/semanales2023)**.

# Sigue las **[instrucciones](../../README.md)**, consulta las correcciones y aporta la tuya propia utilizando el lenguaje de programación que quieras.

# > Recuerda que cada semana se publica un nuevo ejercicio y se corrige el de la semana anterior en directo desde **[Twitch](https://twitch.tv/mouredev)**. Tienes el horario en la sección "eventos" del servidor de **[Discord](https://discord.gg/mouredev)**.
import math

def es_primo(numero):
    for n in range (2, numero):
        if numero % n == 0:
            return False
    return True

def es_fibonacci(numero):
    phi = 0.5 + 0.5 * math.sqrt(5.0)
    a = phi * numero
    return numero == 0 or abs(round(a) - a) < 1.0 / numero


while True:
    numero_introducido = int(input("Introduzca un número para realizar comprobaciones \n"))
    caracteristicas = []

    if (numero_introducido % 2 == 0):
        caracteristicas.append("Par")
    else:
        caracteristicas.append("Impar")
    if (es_fibonacci(numero_introducido)):
        caracteristicas.append("Fibonacci")
    else:
        caracteristicas.append("No Fibonacci")
    if (es_primo(numero_introducido)):
        caracteristicas.append("Primo")
    else:
        caracteristicas.append("No Primo")
    print(f"el número {numero_introducido} es: {caracteristicas[0]}, {caracteristicas[1]} y {caracteristicas[2]}")
    caracteristicas = []


