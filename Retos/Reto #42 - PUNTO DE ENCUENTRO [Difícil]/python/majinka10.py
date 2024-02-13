# m = (y2 - y1) - (x2 - y1)
# y = m x + b

def calcular_pendiente(x, y, sx, sy):
    x1 = x
    x2 = x + sx
    y1 = y
    y2 = y + sy
    return (y2 - y1) / (x2 - x1)

def calcular_interseccion(x, y, m):
    # y = m x + b
    # b = y - m x
    return y - (m * x)

def puntoDeEncuentro(posicion_a, velocidad_a, posicion_b, velocidad_b):
    xa, ya = posicion_a
    sxa, sya = velocidad_a
    xb, yb = posicion_b
    sxb, syb = velocidad_b

    try:
        m1 = calcular_pendiente(xa, ya, sxa, sya)
        m2 = calcular_pendiente(xb, yb, sxb, syb)

        # La segunda condicion del if es cuando son paralelas pero van en 
        # sentido contrario (osea chocan), pero falta incluir el caso en el
        # que son paralelas pero una alcanza la otra.
        if m1 == m2 and (sxa * sxb > 0 or syb * sya > 0):
            return "Son paralelas. Nunca se encontrarán."

        b1 = calcular_interseccion(xa, ya, m1)
        b2 = calcular_interseccion(xb, yb, m2)
        x = (b2 - b1) / (m1 - m2)
        y = m1 * x + b1
        t = (xa - xb) / (sxb - sxa)
        return f"Las rectas se unen en el punto {x, y} en el tiempo {t}"
    
    except: # Caso en que la pendiente sea cero (error de division por cero)
        if sxa != 0 or sxb != 0: # Caso en el que algun punto no se mueva en x
            tx = (xb - xa) / (sxa - sxb)
        else:
            tx = False 
        if sya != 0 or syb != 0: # Caso en el que algun punto no se mueva en y
            ty = (yb - ya) / (sya - syb)
        else:
            ty = False

        if tx == ty: # Si ambos puntos se mueven en las dos direcciones
            t = tx
            x = xa + sxa * tx
            y = ya + sya * ty
        elif ty: # Si solo se mueven en y
            t = ty
            x = xa
            y = ya + sya * ty
        else: # Si solo se mueven en x
            t = tx
            y = ya
            x = xa + sxa * tx
        return f"Las rectas se unen en el punto {x, y} en el tiempo {t}"

    
print(puntoDeEncuentro([2, 3], [-6, 5], [2, 3], [1, 2]))

print(puntoDeEncuentro([2, 0], [0, 1], [0, 2], [1, 0])) 

print(puntoDeEncuentro([0, 0], [1, 0], [0, -1], [1, 0]))

print(puntoDeEncuentro([0, 0], [2, 0], [4, 0], [-1, 0])) 

print(puntoDeEncuentro([0, 0], [1, 2], [4, 0], [-1, 2]))

print(puntoDeEncuentro((0, 0), (10, 5), (100, 50), (-5, -2.5)))