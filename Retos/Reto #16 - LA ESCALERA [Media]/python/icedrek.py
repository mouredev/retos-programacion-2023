def draw_stair(steps):
    if steps == 0:
        print ("__")

    if steps > 0:
        print((" "*(2 + (2 * steps))) + "_")

        while (steps > 0):
            print((" " * (2 * steps)) + "_|")
            steps -= 1

    if steps < 0:    
        print ("_")

        for i in range(-steps):
            print((" " * (1 + (2 * i))) + "|_")
       
def main():
    while True:
        try:
            steps = int(input ("Introduce los escalones de la escalera: "))            
            break
        except ValueError:
            print("El valor debe ser un entero")
    
    draw_stair(steps)
