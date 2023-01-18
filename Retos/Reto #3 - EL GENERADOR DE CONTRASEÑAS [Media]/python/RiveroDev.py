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
        valor_entrada = input("ingrese una valor valido: ")
        valor_entrada = valor_entrada.lower()
        return valor_entrada

def validar(input_valor: str ) -> bool:
        valide = True
        while valide:
                if input_valor.isnumeric() == False:
                        longitud = input("ingrese una valor valido: ")
                else:
                        valide = False

def verificacion(valor_entrada: str) -> bool:
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
                        valor_entrada = valor_valido()
                elif not(valor_entrada == "n" or valor_entrada == "no"):
                        print("intente de nuevo e ingrese una respuesta valida")
                        valor_entrada = valor_valido()    
                else:
                        estado = False
        return valor 

def select_dicc():
        pass

def code_generate():
        pass

if __name__=="__main__":
        pass