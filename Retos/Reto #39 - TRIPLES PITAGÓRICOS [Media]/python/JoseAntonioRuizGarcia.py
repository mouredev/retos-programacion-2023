def findPythagoreanTriple(number: int) -> list:
    range_a = range_b = range_c = range(1, number + 1)
    # Se crea validación y resultado, por simplificar la comprobación de los no repetidos
    validation = []
    result = []

    # Bucle para recorrer todas las opciones posibles
    for a in range_a:
        for b in range_b:
            for c in range_c:
                # Valida si existe combinación de triple pitagórico
                if a**2 + b**2 == c**2:
                    # En caso de haber encontrado uno, se valida que ya no esté ya dentro del resultado
                    r = [a, b, c]
                    r.sort()
                    if not r in validation:
                        validation.append(r)
                        result.append((a, b, c))

    print(f'Combinación de números pitagóricos para el valor {number}: {result}')

if __name__ == '__main__':
    run = True

    while run:
        n = input('Introduce un número entero: ')

        if n.isnumeric():
            n = int(n)
            run = False

    findPythagoreanTriple(n)
