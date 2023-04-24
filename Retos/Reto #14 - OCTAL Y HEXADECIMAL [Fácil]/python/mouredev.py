def to_octal_and_hex(decimal: int):

    current_decimal = decimal

    # Octal
    octal = ""
    while current_decimal > 0:
        octal = str(current_decimal % 8) + octal
        current_decimal //= 8

    octal = 0 if octal == "" else octal
    print(f"{decimal} en octal es {octal}")

    current_decimal = decimal

    # Hex
    hex_values = "0123456789ABCDEF"
    hex = ""
    while current_decimal > 0:
        hex = hex_values[current_decimal % 16] + hex
        current_decimal //= 16

    hex = 0 if hex == "" else hex
    print(f"{decimal} en hexadecimal es {hex}")


to_octal_and_hex(0)
to_octal_and_hex(100)
to_octal_and_hex(1000)
