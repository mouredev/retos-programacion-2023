# /*
#  * Crea un generador de números pseudoaleatorios entre 0 y 100.
#  * - No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
#  *
#  * Es más complicado de lo que parece...
#  */



def pseudoaleatorio(n, j):

    modulo = 101  
    multiplicador = 37 
    incremento = 23  

    numero_aleatorio = (multiplicador * n + incremento * j) % modulo

    print(numero_aleatorio)
    


# Test

for i in range(0, 50):
    for j in range(0, 50):
        pseudoaleatorio(i, j)
