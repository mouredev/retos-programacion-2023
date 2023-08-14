def excel_column(cadena: str) -> int:
    cadena = cadena.upper()
    col = 0

    for i in cadena:
        col = col * 26 + (ord(i) - ord("A") + 1)
    
    return col


print(excel_column("z"))
