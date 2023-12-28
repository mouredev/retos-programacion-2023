def generador_pseudoaleatorio(numero, modulo_grande):
    numero = numero ** 3
    numero = numero // 100
    numero = numero % modulo_grande
    return numero

if __name__ == '__main__':
    numero = float(input("Ingrese un numero (grande) "))
    modulo_grande = float(input("Ingrese el modulo grande (+grande): "))
    print(f"El numero pseudoaleatorio es:{generador_pseudoaleatorio(numero, modulo_grande)}")
