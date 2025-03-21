def ternas(rango):
    return [(a,b,int(c)) for a in range(1, rango+1)
            for b in range(a,rango + 1)
            if (c := (a ** 2 + b ** 2) ** 0.5).is_integer() and c < rango + 1]
