def t9_to_text (t9: str) -> str:
    teclado = [(" "), (".", ",", "?", "!"), ("A", "B", "C"), ("D", "E", "F"), 
               ("G", "H", "I"), ("J", "K", "L"), ("M", "N", "O"), 
               ("P", "Q", "R", "S"), ("T", "U", "V"), ("W", "X", "Y", "Z")]
    texto = ""
    caracteres = t9.split("-")
    for caracter in caracteres:
        cantidad = 0
        for number in caracter:
            if number == caracter[0]:
                cantidad += 1
            else:
                return "Cada bloque debe tener el mismo número"
        if len(teclado[int(caracter[0])]) < cantidad:
            return f"No existe ninguna letra que tenga tantos {caracter[0]}"
        texto += teclado[int(caracter[0])][cantidad - 1]
    return texto

print(t9_to_text("6-33-0-555-555-2-6-666-0-555-88-222-2-7777"))