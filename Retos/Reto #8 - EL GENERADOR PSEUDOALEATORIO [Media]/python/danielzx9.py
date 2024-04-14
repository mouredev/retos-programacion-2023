# # Reto #8: El generador pseudoaleatorio
# #### Dificultad: Media | Publicación: 20/02/23 | Corrección: 27/02/23

# ## Enunciado

# ```
# /*
#  * Crea un generador de números pseudoaleatorios entre 0 y 100.
#  * - No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
#  *
#  * Es más complicado de lo que parece...
#  */
# ```
# #### Tienes toda la información extendida sobre los retos de programación semanales en **[retosdeprogramacion.com/semanales2023](https://retosdeprogramacion.com/semanales2023)**.

# Sigue las **[instrucciones](../../README.md)**, consulta las correcciones y aporta la tuya propia utilizando el lenguaje de programación que quieras.

# > Recuerda que cada semana se publica un nuevo ejercicio y se corrige el de la semana anterior en directo desde **[Twitch](https://twitch.tv/mouredev)**. Tienes el horario en la sección "eventos" del servidor de **[Discord](https://discord.gg/mouredev)**.
class random:
    def __init__(self, semilla):
        self.semilla = semilla
    
    def generar(self, cantidad):
        numeros = []
        for _ in range(cantidad):
            # Aplicamos una serie de operaciones aritméticas para generar un número
            self.semilla = (self.semilla * 1664525 + 1013904223) % 2**32
            numero = (self.semilla % 101)
            numeros.append(numero)
        return numeros

# Creamos una instancia del generador con una semilla inicial arbitraria
generador = random(13579)

# Generamos y mostramos algunos números pseudoaleatorios
numeros_aleatorios = generador.generar(10)
print(numeros_aleatorios)
