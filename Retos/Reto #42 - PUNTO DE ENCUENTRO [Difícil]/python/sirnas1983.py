def interseccion(coor1 : tuple, coor2 : tuple, vel1 : tuple, vel2 : tuple):
    try:
        a = vel1[0]
        b = vel1[1]
        c = vel2[0]
        d = vel2[1]    
        
        x0 = coor1[0]
        y0 = coor1[1]
        x1 = coor2[0]
        y1 = coor2[1]
        
        if (a*d - b*c) != 0:
            
            beta = (a*(y0 - y1) + b*(x1 - x0)) / (a*d - b*c)
            alpha = (y1 - y0 + beta * d) / b     
            
            x = x1 + beta * c
            y = y1 + beta * d

            if alpha == beta:
                print("Las rectas se intersectan en", (x,y).__str__(),"transcurridos", alpha, "segundos")
            else:
                print("Si bien las trayectorias se intersectan no hay colision entre objetos.")
        else:
            alpha1 = None
            alpha2 = None
            if a - c != 0:
                alpha1 = (x1 - x0) / (a - c)
            if b - d != 0:
                alpha2 = (y1 - y0) / (b - d)
            if alpha1==alpha2 and alpha1 > 0:
                x = x0 + alpha1 * a
                y = y0 + alpha1 * b
                print("Los objetos se intersectan en", (x,y).__str__(),"transcurridos", alpha1, "segundos")
            elif alpha1 < 0:
                print("Los objetos son colineales pero tienen trayectorias opuestas")
            else:
                print("Los objetos tienen trayectorias paralelas")  
    except:
        print("Debe ingresar valores de coordenadas y velocidades como tuplas")     

###### PRUEBAS ######
  
coor1 = (0,0)
v1 = (-4,-4)       
coor2 = (2,2)    
v2 = (-6,-6)
interseccion(coor1, coor2, v1, v2) 
    
coor1 = (1,1)
v1 = (-4,-4)       
coor2 = (2,2)    
v2 = (-6,-6)
interseccion(coor1, coor2, v1, v2)   
    
coor1 = (10,8)
v1 = (7,.5)       
coor2 = (4,0)    
v2 = (-0.5,0.5)
interseccion(coor1, coor2, v1, v2)     
    
coor1 = (0,0)
v1 = (4,4)       
coor2 = (4,0)    
v2 = (0,4)
interseccion(coor1, coor2, v1, v2)  
interseccion(4,3,1,6)  
