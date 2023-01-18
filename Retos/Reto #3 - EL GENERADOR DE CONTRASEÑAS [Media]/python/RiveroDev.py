from random import randint as rand

alpha = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t",
        "u","v","w","x","y","z")

numb = ("1","2","3","4","5","6","7","8","9","0")

sign = ("!","@","#","$","%","^","&","*","(",")","_","+","-","=",
        "{","}","[","]","<",">",",",".","?","/")

def inicializador():
        longitud = input("Indique la cantos digitos quieres tu clave: ")
        con_numero = input("quieres que contenga numeros s/n: ")
        con_letras = input("quieres que contenga letras s/n: ")
        con_letras_mayusculas = input("quieres que contenga letras mayusculas s/n:")
        con_simbolos = input("quieres que contenga simbolos s/n: ")

def valor_valido() -> str:
        """Genera una nuevo input para reemplazar uno ya realizado"""
        valor_entrada = input("ingrese una valor valido: ")
        return valor_entrada

def validar(input_valor: str ) -> bool:
        """Verifica si un input str es numerico, si no lo es
        pedira que ingreses un numero """

        valide = True
        while valide:
                if input_valor.isnumeric() == False:
                        longitud = valor_valido()
                else:
                        valide = False

def verificacion(valor_entrada: str) -> bool:
        """Verifica que un input cumpla con las reglas 
        que se  introdusca un Si o un NO
        y reitera que debes dar una respuesta"""

        valor = False
        estado = True
        valor_entrada = valor_entrada.lower()
        print(valor_entrada)
        while estado:
                if valor_entrada == "s" or valor_entrada == "si":
                        valor = True
                        estado = False
                elif valor_entrada == " " or valor_entrada == "":
                        print("Debe ingresar una respuesta")
                        valor_entrada = valor_valido().lower()

                elif not(valor_entrada == "n" or valor_entrada == "no"):
                        print("intente de nuevo e ingrese una respuesta valida")
                        valor_entrada = valor_valido().lower()    
                else:
                        estado = False
        return valor 

def select_dicc() -> dict:
        pass

def code_generate():
        pass

if __name__=="__main__":
        pass