while True:
    try:
        number = int(input("El numero: "))
    except:
        print("ERROR")
    else:
        break


def octal(n):
    result_1 = ""
    d = n
    m = 0
    while d >= 8:
        m = d % 8
        d = d // 8
        result_1 = result_1 + str(m)
    result_1 = result_1 + str(d)
    result_1 = result_1[::-1]
    return result_1


def hexadecimal(n):
    hexadecimal_dict = {
        10:"A",
        11:"B",
        12:"C",
        13:"D",
        14:"E",
        15:"F"
    }
    result_2 = ""
    d = n
    m = 0
    while d >= 16:
        m = d % 16
        d = d // 16
        print(m)
        if m >= 10 and m < 16:
            result_2 = result_2 + hexadecimal_dict[m]
            print(f"if: {m}")
        else:
            result_2 = result_2 + str(m)
        
    else:
        if d >= 10 and d <= 15:
            result_2 = result_2 + hexadecimal_dict[d]
        else:
            result_2 = result_2 + str(d)
    result_2 = result_2[::-1]
    return result_2


print(f"El numero: {number}, su equivalente en base octal: {octal(number)}, en base hexadecimal: {hexadecimal(number)}")
