import datetime
"""
 Crea un generador de números pseudoaleatorios entre 0 y 100.
 - No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
"""

def main():
    print(datetime.datetime.now().microsecond % 101)
    

if __name__ == '__main__':
    main()
