def BuscarObjetivo(list, objetivo):
    combinaciones = pow(2,len(list))
    suma = 0
    for k in range (1,combinaciones):
        b= bin(k)[2:].zfill(len(list))
        ret=[]
        for i, bit in enumerate(b):
            if bit == '1':
                suma += list[i]
                ret.append(list[i])
        if suma==objetivo:
            print(ret)
        suma=0
        ret=[]
    return ()
BuscarObjetivo([1,5,3,2],6)