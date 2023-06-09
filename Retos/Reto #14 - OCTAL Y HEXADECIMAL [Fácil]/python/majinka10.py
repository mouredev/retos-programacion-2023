#Tabla de conversion. 
#Para los numeros que tienen un array: el primer elemento corresponde a su conversión en octal y el segundo a hexadecimal
conversion={0:[0,0], 1:[1,1], 2:[2,2], 3:[3,3], 4:[4,4], 5:[5,5], 6:[6,6], 7:[7,7], 8:[10,8], 
            9:[11,9], 10:[12,'A'], 11:[13,'B'], 12:[14,'C'], 13:[15,'D'], 14:[16,'E'], 15:[17,'F']}

#Con esta función separo la parte entera de la decimal
def separar(number:float):
    parte_entera=int(number)
    parte_decimal=round((number-parte_entera)*1000)
    return parte_entera, parte_decimal

#Con esta función convierto el número en base 10 a la base objetivo.
def decimal_to_base(number:float, base:int):
    (entera, decimal)=separar(number)
    #Conversión de la parte entera
    modulos=[]
    cociente,modulo=int(entera/base), entera%base
    modulos.append(conversion[modulo][1])
    while cociente>base:
        cociente, modulo=int(cociente/base), cociente%base
        modulos.append(conversion[modulo][1])
    modulos.append(conversion[cociente][1])
    modulos.reverse()
    #Conversión de la parte decimal
    decimales=[]
    #Añado la coma para separar la parte entera de la decimal
    decimales.append(',')
    entero,nuevo_decimal=separar(decimal*base/1000)
    decimales.append(conversion[entero][1])
    for i in range(4):
        entero, nuevo_decimal=separar(nuevo_decimal*base/1000)
        decimales.append(conversion[entero][1])
    #Uno ambos arrays
    result_list=modulos+decimales
    #Lo convierto a string (para que se vea más bonito)
    resultado=''.join(map(str,result_list))
    return resultado

def conversor(number:float):
    print(f'El número en base 8 es {decimal_to_base(number,8)}\nEl número en base 16 es {decimal_to_base(number,16)}')
    
conversor(94260.238)


