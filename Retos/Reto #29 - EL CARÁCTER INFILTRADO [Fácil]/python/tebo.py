x = input("Ingrese la primera cadena de texto")
z = input("Ingrese la segunda cadena de texto")
p = []
l = []
w = []
if len(x) == len(z) :
    for y in x : 
        l.append(y)
        if len(l) == len(x) :
                for t in z :
                    w.append(t)
                    if len(l) == len(w) :
                        for g in range(len(l)) :
                             if l[g] != w[g] :
                                p.append(w[g])
    print(f"{x} / {z} -> {p}")
