def Colision(pa, sa, pb, sb):
    xa, ya = pa
    xb, yb = pb
    vxa, vya = sa
    vxb, vyb = sb

    if vxa - vxb == 0:
        if xa == xb:
            tx = 0
        else:
            return "No se encontrarán"
    else:
        tx = (xb - xa) / (vxa - vxb)

    
    if vya - vyb == 0:
        if ya == yb:
            ty = 0
        else:
            return "No se encontrarán"
    else:
        ty = (yb - ya) / (vya - vyb)


    if tx == ty:
        t = tx        
        x = xa + vxa * tx
        y = ya + vya * ty
        return f"Se colisionarán en el punto ({x}, {y}) en un tiempo de {t}."
    else:
        return "No se encontrarán"
    

print(Colision((5, 0), (0, 1), (0, 5), (1, 0)))
print(Colision((2, 0), (0, 1), (0, 2), (1, 0)))
print(Colision((0, 0), (10, 5), (100, 50), (-5, -2.5)))
