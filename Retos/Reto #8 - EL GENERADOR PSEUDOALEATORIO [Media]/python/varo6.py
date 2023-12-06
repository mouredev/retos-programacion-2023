#Generador pseudoaleatorio entre 1 y 100 sin random module
import timeit

#Con la formula r = r % B donde B es el numero maximo que quiero, según como sea la semilla podré iterarlo tantas
# veces para mejorar su aleatoriedad. La eficacia depende de la semilla, así que usaré de referencia el tiempo exacto de timeit.

#Esta función devuelve el tiempo exacto multiplicado por 100000 para poder usarlo como entero
def get_exact_time():
    x = int(timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)*100000)
    print(f'La semilla usada será {x}')
    #en esta simulación, x=25561
    return x

#La función pseudorandom tomará un valor máximo y mínimo, e iterará la fórmula la misma cantidad del valor de la semilla. 
def pseudorandom(min_num, max_num):
    seed = get_exact_time()
    for i in range(seed):
        seed = (seed) % (max_num+1) 
    return seed + (min_num-1)

print(pseudorandom(1,100))
#Para comprobación de que funciona guardé en una lista todos los valores de 200 simulaciones. Con matplotlib y numpy se puede
#comprobar mediante una distribución normal. En este caso, salía prácticamente perfecta.