'''
Crea una función que dibuje una escalera según su número de escalones.
- Si el número es positivo, será ascendente de izquiera a derecha.
- Si el número es negativo, será descendente de izquiera a derecha.
- Si el número es cero, se dibujarán dos guiones bajos (__).

Ejemplo: 4
        _
      _|       
    _|
  _|
_|

'''
def escalera(n):
    escalera = ''
    if n > 0:
        for i in range(abs(n+1)):
            if i == 0:
                escalera += ' ' * (abs(n*2)) + '_' + '\n'
            else:
                escalera += '  ' * (abs(n) - i ) + '_|' + '\n'
        print(escalera)
    elif n < 0:
        for i in range(abs(n)+1):
            if i == 0:
                escalera +=  '_' + '\n'
            else:
                escalera += '  ' * i  + '|_' + '\n'
        print(escalera)
    else:
        print("__")

if __name__ == '__main__':
    escalera(-4)
    escalera(4)
    escalera(0)