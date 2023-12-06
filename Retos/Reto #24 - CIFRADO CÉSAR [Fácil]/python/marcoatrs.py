from string import ascii_letters

def normal_a_cesar(texto: str, desplazamiento: int) -> str:
    cifrado = []
    for t in texto:
        if t not in ascii_letters:
            cifrado.append(t)
            continue
        limits = (65, 90) if t == t.capitalize() else (97, 122)
        num = (ord(t) + desplazamiento)
        if num > limits[1]:
            num = (num - limits[1] + 1) + limits[0]
        cifrado.append(chr(num))
    return "".join(cifrado)


def cesar_a_normal(texto: str, desplazamiento: int):
    normal = []
    for t in texto:
        if t not in ascii_letters:
            normal.append(t)
            continue
        limits = (65, 90) if t == t.capitalize() else (97, 122)
        num = (ord(t) - desplazamiento)
        if num < limits[0]:
            num = limits[1] - limits[0] - num
        normal.append(chr(num))
    return "".join(normal)


print(normal_a_cesar("Hola, no me entiendes muajaja!", 3))
print(cesar_a_normal(normal_a_cesar("Hola, no me entiendes muajaja!", 3), 3))