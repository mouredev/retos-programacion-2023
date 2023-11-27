def validate(objeto_1, objeto_2):
    x1, y1, vx1, vx2 = objeto_1
    x2, y2, vy1, vy2 = objeto_2

    dx = x2 - x1
    dy = y2 - y1
    dvx = vx2 - vx1
    dvy = vy2 - vy1

    if dvx == 0 and dvy == 0:
        return "Los objetos son paralelos y nunca se cruzan."
    
    #calculamos el producto escalar (nos dice si el objeto se aleja y a que ritmo lo hacen)
    pd = (-dx * dvx - dy * dvy)
    #Calculamos la velocidad relativa
    vr = (dvx ** 2 + dvy**2 )

    t = pd/vr

    if t < 0:
        return "Los objetos jamas se tocan"
    
    x_encuentro = x1 + vx1 * t
    y_encuentro = y1 + vy1 * t

    return [x_encuentro, y_encuentro, t]

objeto_1 = [0, 0, 5, 1] 
objeto_2 = [3, 1, 2, 2] 

resultado = validate(objeto_1, objeto_2)

if isinstance(resultado, str):
    print(resultado)
else:
    print(f"Los objetos se encuentran en ({resultado[0]}, {resultado[1]}) después de {resultado[2]} unidades de tiempo.")

