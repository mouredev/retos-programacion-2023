print("""
Que deseas convertir? elige una opción: 
1) Convertir a RGB.
2) Convertir a HEX.
""")

eligio = input("-Selecciona algo :")

if eligio=="1":
    txt = input("-escibe el codigo:")
    def hex_to_rgb(hex):
        rgb = []
        for i in (0, 2, 4):
            decimal = int(hex[i:i+2], 16)
            rgb.append(decimal)
  
        return tuple(rgb)

    print(hex_to_rgb(txt))
elif eligio=="2":
    def rgb_to_hex(r, g, b):
        return '#{0:02x}{1:02x}{2:02x}'.format(r, g, b)

    try:
        txt = input("Ingresa los valores RGB separados por comas (por ejemplo, 255,0,128): ")
        r, g, b = map(int, txt.split(','))  # Separa la entrada en valores enteros
        hex_code = rgb_to_hex(r, g, b)
        print(f"El código hexadecimal correspondiente es: {hex_code}")
    except ValueError:
        print("Entrada incorrecta. Asegúrate de ingresar tres valores separados por comas.")
else:
    print("Opción no válida")
