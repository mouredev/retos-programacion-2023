import math

def cuadrado_perfecto(numero):
    try:
        sqrt = int(math.sqrt(numero))
        return sqrt * sqrt == numero
    except Exception as e:
        print(e)
        # pass

def comprobar(numero: int):

    resultado = f"({numero}) --> "

    # Comprobar si número es primo
    if numero < 2:
        resultado += "❌ No es primo, "
    else:
        limite = int(math.sqrt(numero)) + 1
        es_primo = True

        for divisor in range(2, limite):
            if numero % divisor == 0:
                resultado += "❌ No es primo, "
                es_primo = False
                break

        if es_primo:
            resultado += "✅ Es primo, "

    # Comprobar si número está en la secuencia Fibonacci
    if cuadrado_perfecto(5 * numero * numero - 4) or cuadrado_perfecto(5 * numero * numero + 4):
        resultado += "✅ Fibonacci"
    else:
        resultado += "❌ No Fibonacci"

    # Comprobar si número es par o impar
    resultado += ", ✅ Es par." if numero % 2 == 0 else ", ❌ Es impar."
    print(resultado)

if __name__ == "__main__":
    for i in range(0, 20):
        comprobar(i)
