"""
 * Crea un programa capaz de interactuar con un fichero TXT.
 * IMPORTANTE: El fichero TXT NO debe subirse como parte de la corrección. 
 * Únicamente el código.
 * 
 * - Si no existe, debe crear un fichero llamado "text.txt".
 * - Desde el programa debes ser capaz de introducir texto por consola y guardarlo
 *   en una nueva línea cada vez que se pulse el botón "Enter".
 * - Si el fichero existe, el programa tiene que dar la opción de seguir escribiendo
 *   a continuación o borrar su contenido y comenzar desde el principio.
 * - Si se selecciona continuar escribiendo, se tiene que mostrar por consola
 *   el texto que ya posee el fichero. 
"""

def create_tex():
    try:
        text = input("Si el documento no exites se creata de manera automatica\nIngrese el documento a trabajar: ")

        file = open(f"{text}.txt","a+")

        quiz = input("desea solo ver el contenido de documento[R]\ntrabajar/continuar trabajando en el documento[W]\neliminar el contenido del documento y trabajar con el en blanco[C]: ")
        quiz = quiz.upper()
        if quiz == "R":
            file = open(f"{text}.txt","r")
            print(file.read())
            file.close()
            
        elif quiz == "W":
            print("Este sistema interpretara cada [.] como un cierre a texto o un puto y aparte.")
            cond = True
            while cond == True:
                file = open(f"{text}.txt","r")
                print(file.readline())
                file = open(f"{text}.txt","a")
                whiter = input("ingrese texto: ")
                file.write(whiter+"\n")
                if whiter[-1] == ".":
                    respond =input("Es un punto y aparte[P]\nEs un punto final[F]\n:")
                    respond = respond.upper()
                    if respond == "P":
                        print("Continue su escritura: ")
                        cond = True
                    else:
                        print("Este es su texto final.")
                        cond = False
        elif quiz == "C":
            file = open(f"{text}.txt","w")
            print("Todo el contenido de {text}.txt ha sido borrado.")
            cond = True
            while cond == True:
                file = open(f"{text}.txt","a")
                whiter = input("ingrese texto: ")
                file.write(whiter+"\n")
                if whiter[-1] != ".":
                    respond =input("Es un punto y aparte[P]\nEs un punto final[F]")
                    respond.upper
                    if respond == "P":
                        print("Continue su escritura: ")
                        cond = True
                    else:
                        print("Este es su texto final.")
                        cond = False
        file = open(f"{text}.txt","r")
        print(file.read())
        file.close()
    except:
        {"ERROR":"Unepetex ERROR"}
create_tex()
