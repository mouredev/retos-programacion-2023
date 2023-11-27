teclado_t9 = [" ", ",.?", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

def convertir_pulsaciones(texto: str) -> str:
    pulsaciones = texto.split("-")
    salida = ""
    for pulsacion in pulsaciones:
        if not pulsacion.isdigit():
            print("Formato incorrecto")
            return
        if not all([c == pulsacion[0] for c in pulsacion]):
            print(f"La pulsacion {pulsacion} no es igual")
        salida += teclado_t9[int(pulsacion[0])][len(pulsacion) - 1]
    return salida

print(convertir_pulsaciones("6-2-777-222-666-0-2-66-8-666-66-444-666"))
