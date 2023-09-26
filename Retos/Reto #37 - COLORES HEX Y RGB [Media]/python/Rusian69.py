def rgb_a_hex(rgb:str):
    hexa_vaules = "0123456789ABCDEF"
    result = ""
    calculate = ""
    hexa_result = ""
    for index in rgb:
        if index != ",":
            calculate += index
        else:
            number_hexa = int(calculate)
            if number_hexa == 0:
                result += "00"
                calculate = ""
            else:
                while number_hexa > 0:
                    hexa_result += hexa_vaules[number_hexa % 16]
                    cociente_hexa = number_hexa // 16
                    number_hexa = cociente_hexa
                else:
                    hexa_reverse = "".join(reversed(hexa_result))
                    calculate = ""
                    result += hexa_reverse
                    hexa_result = ""
    number_hexa = int(calculate)
    hexa_reverse = ""
    if number_hexa == 0:
        result += "00"
    else:
        while number_hexa > 0:
            hexa_result += hexa_vaules[number_hexa % 16]
            cociente_hexa = number_hexa // 16
            number_hexa = cociente_hexa
        else:
            hexa_reverse = "".join(reversed(hexa_result))
    result += hexa_reverse
    print(f"#{result}")

def hex_a_rgb(hex:str):
    hexa_vaules = "0123456789ABCDEF"
    result = []
    count = 0
    values = ""
    num = 0
    for index in hex[1:]:
        values += index
        count += 1
        if count == 2:
            count = 0
            val =  (hexa_vaules.index(values[0]) * (len(hexa_vaules) ** 1))
            val_2 = (hexa_vaules.index(values[1]) * (len(hexa_vaules) ** 0))
            val_sum = val + val_2
            result.append(val_sum)
            values = ""
    print(result)

def main():
    print("desea convertir de RGB a HEX (1) o de HEX a RGB(2)")
    mand = input(":")
    if mand == "1":
        rgb_a_hex(input("escriba el codigo RGB: "))
    elif mand == "2":
        hex_a_rgb(input("escriba el codigo HEX: "))
    else:
        print("por favor coloque un valor valido:")
        main()

if __name__ == '__main__':
    main()
