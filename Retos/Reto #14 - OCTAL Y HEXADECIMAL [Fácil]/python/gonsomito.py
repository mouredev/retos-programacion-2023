"""
 * Crea una función que reciba un número ENTERO y lo trasforme a Octal y Hexadecimal.
 * - No está permitido usar funciones propias del lenguaje de programación que
 * realicen esas operaciones directamente.
"""
def octa_y_hexa(num: int):
    #hagamos primero la conversión de ENTERO a OCTAL
    octa=""
    if num>=0 and num<8:                #Si es menor a 8 no necesita conversión
        octa = num
        print(f"El entero en base(10) {num} es en base(8) : {octa}")
    else:                                   #Si es mayor destripamos
        aux=num
        while aux>=8:
            octa = str(aux%8) + octa
            aux = aux//8
        octa=str(aux)+octa
        print(f"El entero en base(10) {num} es en base(8) : {octa}")
        
    #hagamos ahora la conversión de ENTERO a HEXADECIMAL
    dict_hexa={0:"0", 1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9",
                10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}
    hexa=""
    if num >= 0 and num < 16:                #Si es menor a 16 no necesita conversión
        hexa = dict_hexa[num]
        print(f"El entero en base(10) {num} es en base(8) : {hexa}")
    else:
        aux=num
        while aux >=16:
            hexa = dict_hexa[aux%16]+hexa
            aux = aux//16
        hexa=dict_hexa[aux] + hexa
        print(f"El entero en base(10) {num} es en base(8) : {hexa}")

#-----------LLamada principal.
numero=input("Dame un número: ")
while numero.isdigit():             #mientras no haya letras haremos conversiones
    octa_y_hexa(int(numero))
    numero=input("número: ")
