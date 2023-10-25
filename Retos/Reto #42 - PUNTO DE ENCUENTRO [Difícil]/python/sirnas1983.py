from matplotlib import pyplot as plt


def interseccion(coor1 : tuple, coor2 : tuple, vel1 : tuple, vel2 : tuple, plot_graph : bool = False):
    '''
    Funcion que imprime por pantalla si existe o no colision de 2 objetos en el plano
    y retorna True en caso de existir y False en caso que no
    
    Deben ingresarse las coordenadas de partida de ambos objetos como tuplas y sus
    velocidades en x e y tambien como tuplas. Para que imprima los graficos pase True como 5to argumento.
    '''
    colision = False
    try:
        # Asigno el valor de las tuplas a variables individuales
        vx1 = vel1[0]
        vy1 = vel1[1]
        vx2 = vel2[0]
        vy2 = vel2[1]    
        
        x0 = coor1[0]
        y0 = coor1[1]
        x1 = coor2[0]
        y1 = coor2[1]
        
        colision = False
        
        # Verifico que ambos objetos no esten en reposo
        if (vx1 == vy1 == 0) and (vx2 == vy2 == 0):
            print("Ambos objetos estan en reposo")
        # Verifico la condicion de que no parten del mismo punto
        elif (x0 == x1) and (y0 == y1):
            print("Ambos objetos estan colisionados antes de iniciar su movimiento")
            colision = True
        else:
            # Verifico que ambas trayectorias no sean coplanares
            if (vx1*vy2 - vy1*vx2) != 0:
                
                # Calculo alpha y beta de sus ecuaciones vectoriales
                beta = (vx1*(y0 - y1) + vy1*(x1 - x0)) / (vx1*vy2 - vy1*vx2)
                if vy1 != 0:
                    alpha = (y1 - y0 + beta * vy2) / vy1
                elif vx1 != 0:
                    alpha = (x1 - x0 + beta * vx2) / vx1
                
                x = x1 + beta * vx2
                y = y1 + beta * vy2

                # Si alpha y beta son iguales (tiempo) hay colision, sino solamente interseccion de trayectorias
                if alpha == beta:
                    print("Las objetos colisionan en", (x,y).__str__(),"transcurridos", alpha, "segundos")
                    colision = True
                else:
                    print(f"Si bien las trayectorias se intersectan en {(x,y).__str__()} no hay colision entre objetos.")
            else:
                # Hago el analisis puntual de trayectorias coplanares
                alpha1 = None
                alpha2 = None
                # Para ello calculo la constante del vector
                if vx1 - vx2 != 0:
                    alpha1 = (x1 - x0) / (vx1 - vx2)
                elif vy1 - vy2 != 0:
                    alpha2 = (y1 - y0) / (vy1 - vy2)
                else:
                    print("Los objetos van en la misma direccion pero uno igual o mas lento que el otro")
                    alpha2 = 1
                    alpha1 = alpha2 + 1
                # La constante del vector debe ser igual para ambos y mayor a 0 
                if alpha1 == alpha2 > 0:
                    x = x0 + alpha1 * vx1
                    y = y0 + alpha1 * vy1
                    print("Los objetos colisionan en", (x,y).__str__(),"transcurridos", alpha1, "segundos")
                    colision = True
                elif alpha1 < 0:
                    print("Los objetos son colineales pero van en direcciones opuetas")
                elif (vx1 == vy1 == 0) or (vx2 == vy2 == 0):
                    print("El objeto en movimento no intersecta el objeto en reposo")
        # Si existe colision pregunto si quieren ver el grafico
        if colision and plot_graph:
            plt.axhline(0, color='black', linewidth=0.5)
            plt.axvline(0, color='black', linewidth=0.5)
            plt.scatter(x, y, color='red', linewidths=10, label='Punto de encuentro')
            plt.scatter(x0, y0, color='blue', linewidths=5, label='Salida objeto 1')
            plt.scatter(x1, y1, color='green', linewidths=5, label='Salida objeto 2')
            plt.plot([x0, x], [y0, y], color='blue', ls="-." )
            plt.plot([x1, x], [y1, y], color='green', ls="-.")
            plt.legend()
            plt.xlabel('Eje X')
            plt.ylabel('Eje Y')
            plt.title('Punto de Colision')
            plt.grid(True)
            plt.show()
        return colision  
    except:
        print("Debe ingresar valores de coordenadas y velocidades como tuplas")     
        return colision

##### PRUEBAS ######
  
coor1 = (0,0)
v1 = (-4,-4)       
coor2 = (2,2)    
v2 = (-6,-6)
interseccion(coor1, coor2, v1, v2) 

coor1 = (0,0)
v1 = (0,0)       
coor2 = (3,2)    
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

coor1 = (0,0)
v1 = (4,4)       
coor2 = (2,2)    
v2 = (4,4)
interseccion(coor1, coor2, v1, v2)  

interseccion(4,3,1,6)
