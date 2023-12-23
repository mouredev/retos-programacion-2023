"""
 Crea una función que encuentre todos los triples pitagóricos
 (ternas) menores o iguales a un número dado.
 - Debes buscar información sobre qué es un triple pitagórico.
 - La función únicamente recibe el número máximo que puede
   aparecer en el triple.
 - Ejemplo: Los triples menores o iguales a 10 están
   formados por (3, 4, 5) y (6, 8, 10).
"""

def get_pythagorean_triples(max_n: int) -> list:
    """Devuelve los triples pitagóricos con valores menores al número dado

    Args:
        max_n (int): valor máximo posible dentro de un triple pitagórico

    Returns:
        list: lista de triples pitagóricos válidos
    """
    triples = []
    stop = False
    for i in range(3, max_n):
        for j in range(i + 1, max_n):
            result = (i**2 + j**2)**0.5
            # Si el resultado es mayor que el número máximo, salimos y seguimos
            # con el siguiente valor de "i", ya que a partir de aquí siempre nos
            # vamos a pasar del valor máximo
            if result > max_n:
                # Además, si el segundo número es justo el siguiente al primero,
                # entonces dejaremos de buscar más triples
                if j == i + 1:
                    stop = True
                break
            # Si el resultado es un número entero (no decimal) entonces estamos
            # ante una solución
            if result % int(result) == 0:
                triples.append((i, j, int(result)))

        if stop:
            break

    return triples

p_triples = get_pythagorean_triples(20)
print(p_triples)
print(len(p_triples))
