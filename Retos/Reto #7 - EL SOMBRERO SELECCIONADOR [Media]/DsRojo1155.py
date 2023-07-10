import signal
import sys

# gryffindor: valor
# hufflepuff: lealtad
# ravenclaw: sabiduría
# slytherin: ambición

def terminar(sig,frame):
    print(f"\n\n[!] Saliendo...\n")
    sys.exit(1)

signal.signal(signal.SIGINT,terminar)

houses = {"grynffindor" : 0,
        "hufflepuff" : 0,
        "ravenclaw" : 0,
        "slytherin" : 0}
def get_awnser():
        preguntas = [[("¿Cómo te definirías?",""),
                    ("1. Valiente", "grynffindor"),
                    ("2. Leal", "hufflepuff"),
                    ("3. Sabio", "ravenclaw"),
                    ("4. Ambicioso", "slytherin"),],

                    [("¿Cuál es tu clase favorita?",""),
                    ("1. Vuelo", "grynffindor"),
                    ("2. Pociones", "ravenclaw"),
                    ("3. Defensa contra las artes oscuras", "slytherin"),
                    ("4. Animales fantásticos", "hufflepuff")],

                    [("¿Dónde pasarías más tiempo?",""), 
                    ("1. Invernadero", "hufflepuff"),
                    ("2. Biblioteca", "ravenclaw"),
                    ("3. En la sala común", "slytherin"),
                    ("4. Explorando", "grynffindor")],

                    [("¿Cuál es tu color favorito?",""), 
                    ("1. Rojo", "grynffindor"),
                    ("2. Azul", "ravenclaw"),
                    ("3. Verde", "slytherin"),
                    ("4. Amarillo", "hufflepuff")],
                    
                    [("¿Cuál es tu mascota?",""),
                    ("1. Sapo", "ravenclaw"),
                    ("2. Lechuza", "grynffindor"),
                    ("3. Gato", "hufflepuff"),
                    ("4. Serpiente", "slytherin")]]
        for pregunta in preguntas:
            print(pregunta[0][0])
            opciones = pregunta[1:]

            for opcion in opciones:
                print(opcion[0])
            while True:
                    try: 
                        op = int(input("Selecciona una opción: "))
                        if op == 1 or op == 2 or  op == 3 or op == 4:
                            op = op-1
                            casa = opciones[op][1]
                            houses[casa] +=1
                            break
                        else:
                            print("[+] Opcion invalida")
                    except Exception as e:
                        print("[+]Opcion invalida")
            
        # obtenemos los valores maximos del diccionario
        max_value = max(houses.values())
        # aca almacenaremos las casas con valores iguales
        casa_maximas = []
        
        for casa,valor in houses.items():
             if valor == max_value:
                  casa_maximas.append(casa)

        if len(casa_maximas) >=2:     
            print(f"Lo tengo puedes escoger entre estas casas: ")
        else:
            print(f"Lo tengo esta es tu casa ")
     

        for casa in casa_maximas:
            print(f"'{casa}'")
     

if __name__ == '__main__':
      get_awnser()
