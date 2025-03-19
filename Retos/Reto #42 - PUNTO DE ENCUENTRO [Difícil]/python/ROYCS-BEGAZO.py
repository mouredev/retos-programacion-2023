def colision(position_a, speed_a, position_b, speed_b):
    #desenpaquetado de variables
    xa,ya = position_a #posision en x, y
    sxa, sya = speed_a #velocidad en x, y
    xb, yb = position_b #posision en x, y
    sxb, syb = speed_b #velocidad en x, y
    #si las velocidadedes en x son las mismas
    if sxa - sxb == 0:
        if xa == xb: #entonces las posiciones tambien
            tx = 0
        else:
            #  si no hay igualdad no hay colision
            return 'los objetos no se encontraran'
    #si las velocidades son distintas se  despeja t de la formula de mru
    else:
        tx = (xb - xa) / (sxa - sxb)
    #se repite con el otro eje
    if sya - syb == 0:
        if ya == yb:
            ty = 0
        else:
            return 'los objetos no se encontraran'
    else:
        ty = (yb - ya) / (sya - syb)
    #si los tiempos de encuentro son iguales en ambos ejes hay colision
    if tx == ty:
        t = tx
        x = xb + sxb * t
        y = yb + syb * t
        return f'el punto de encuentro es {x},{y} en el momento {t}'
    else:
        return 'los objetos no se encontraran'
