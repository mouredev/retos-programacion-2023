

# * Crea un generador de números pseudoaleatorios entre 0 y 100.
# * - No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
# *
# * Es más complicado de lo que parece...


from datetime import datetime as dt


def random():
    # Generamos una semilla
    semilla = int(dt.now().microsecond)
    # Convertir para que nos de millares
    millar = int(semilla*(1/100))
    m = millar
    if m % 2 == 0:
        for i in range(m):
            adi = i*(1/100)
            sumar = int(adi+1)
    else:
        for i in range(m):
            adi = i*(1/100)
            sumar = int(adi+1)
    # Asegurar que es menor a cien
    if sumar <= 100:
        return sumar
    return random()


print(random())
