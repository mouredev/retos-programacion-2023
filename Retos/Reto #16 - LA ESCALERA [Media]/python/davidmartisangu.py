'''* Crea una función que dibuje una escalera según su número de escalones.
 * - Si el número es positivo, será ascendente de izquiera a derecha.
 * - Si el número es negativo, será descendente de izquiera a derecha.
 * - Si el número es cero, se dibujarán dos guiones bajos (__).
 * 
 * Ejemplo: 4
 *         _
 *       _|       
 *     _|
 *   _|
 * _|
'''
numero_esc=int(input("Introduce el número de escalones: "))

if numero_esc>0:
    for i in range(numero_esc,0,-1):
        dibujo="  "*i+"_|"
        print(dibujo)
elif numero_esc<0:
    numero_esc=abs(numero_esc)
    for i in range(numero_esc):
        dibujo="  "*(i+1)+"|_"
        print(dibujo)
else:
    print("__")