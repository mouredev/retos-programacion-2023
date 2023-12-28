hexa_dic = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}

def transform(number, base, result=[]):
    div = int(number / base)
    rest = number % base
    result.append(rest if rest < 10 else hexa_dic[rest])
    if div < 1:
        result.reverse()
        return "".join(map(str, result))
    return transform(div, base, result)

if __name__ == "__main__":
    number = None
    while type(number) != int:
        try:
            number = int(input("Introduce el número decimal: "))
        except:
            print("Error: el número debe ser entero")
    
    print("Número en octadecimal:", transform(number, 8, []))
    print("Número en hexadecimal:", transform(number, 16, []))