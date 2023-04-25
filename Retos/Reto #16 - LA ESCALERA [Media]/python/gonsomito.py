"""
 * Crea una función que dibuje una escalera según su número de escalones.
 * - Si el número es positivo, será ascendente de izquiera a derecha.
 * - Si el número es negativo, será descendente de izquiera a derecha.
 * - Si el número es cero, se dibujarán dos guiones bajos (__).
"""
def starway_to(peldanos):
    if peldanos == 0:                               #nos quedamos en el descansillo
        print("__")
    elif peldanos > 0:                              #positivos: asciende izq a der
        print((peldanos+1)*" "+"_")
        while peldanos>0:
            print(peldanos*" "+"_|")
            peldanos=peldanos-1
    else:                                           #negativos: desciende izq a der
        aux=-peldanos
        print("_")
        while peldanos < 0:
            print((peldanos+aux)*" "+"|_")
            peldanos=peldanos+1
#-------------------------------------------------- 
try:
    starway_to(int(input("Cuantos escalones")))         #por supuesto, esto falla con no valores numéricos
except:
    print("No es un valor correcto")
