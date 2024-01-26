def colision(posicionA, posicionB, velocidadA, velocidadB):

    xA, yA = posicionA
    xB, yB = posicionB
    vxA, vyA = velocidadA
    vxB, vyB = velocidadB

    if vxA - vxB == 0:
        if xA == xB:
            tx = 0
        else:
            return "Los objetos no se encontrarán."
    else:
        tx = (xB - xA) / (vxA - vxB)

    if vyA - vyB == 0:
        if yA == yB:
            ty = 0
        else:
            return "Los objetos no se encontrarán."
    else:
        ty = (yB - yA) / (vyA - vyB)

    if tx == ty:
        t = tx
        x = xA + vxA * tx
        y = yA + vyA * ty
        return f"Los objetos colisionan en el punto ({x}, {y}) en un tiempo {t}."
    else:
        return "Los objetos no se encontrarán."
    
print(colision((0, 0), (1, 1), (1, 1), (0, 0)))

