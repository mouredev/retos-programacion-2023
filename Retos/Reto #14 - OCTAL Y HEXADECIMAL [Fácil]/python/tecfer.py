'''decimal a octal  hexadecimal'''

def octal(numero):
    resultado=[]
    while numero>0:
        resultado.append(str(numero%8))
        numero=numero//8
    resultado.reverse()
    
    return "".join(resultado)

def hexadecimal(numero):
    resultado=[]
    while numero>0:
        modulo = numero%16

        if modulo==10: letra="A"
        elif modulo==11: letra="B"
        elif modulo==12: letra="C"
        elif modulo==13: letra="D"
        elif modulo==14: letra="E"
        elif modulo==15: letra="F"     
        else:
            letra = str(modulo)

        resultado.append(letra)
        numero=numero//16

    resultado.reverse()
    return "".join(resultado)

def main():
    teclado = input("Introduce un número: ")
    if teclado.isdigit:
        numero = int(teclado)
        print(f"el núemro {teclado} es {octal(numero)} en octal")
        print(f"el núemro {teclado} es {hexadecimal(numero)} en hexadecimal")


if __name__ == '__main__':
    main()