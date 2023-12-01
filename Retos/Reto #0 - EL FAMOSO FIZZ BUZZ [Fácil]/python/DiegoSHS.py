def eval_fzbz(n, ref1=3, ref2=5):
    """recibe un nuero y comprueba si es multiplo de 3, 5 o ambos y devuelve una palabra en cuestión"""
    return 'fizzbuzz' if not n % (ref1*ref2) else 'fizz' if not n % ref1 else 'buzz' if not n % ref2 else n


def fizz_buzz():
    """hace una lista de los numeros del 1 al 100 y los evalúa con la función eval_fzbz e imprimer el resultado"""
    count = list(range(1, 101))
    result = map(eval_fzbz, count)
    print(*result, sep='\n')


if __name__ == "__main__":
    fizz_buzz()
