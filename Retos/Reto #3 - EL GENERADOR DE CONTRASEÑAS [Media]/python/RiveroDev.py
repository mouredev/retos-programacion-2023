#! /bin/python3

import random

alpha = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
numb = ("1","2","3","4","5","6","7","8","9","0")
sign = ("!","@","#","$","%","^","&","*","(",")","_","+","-","=","{","}","[","]","<",">",",",".","?","/")


def preguntas():
        dic_valores = {"longitud":None,"con_numero":None,"con_letras":None,
                        "con_letras_mayusculas":None,"con_simbolos":None}

        dic_valores["longitud"] = validar(input("Indique la cantidad de digitos de tu clave: "))
        dic_valores["con_numero"] = verificacion(input("quieres que contenga numeros s/n: "))
        dic_valores["con_letras"] = verificacion(input("quieres que contenga letras s/n: "))
        dic_valores["con_letras_mayusculas"] = verificacion(input("quieres que contenga letras mayusculas s/n:"))
        dic_valores["con_simbolos"] = verificacion(input("quieres que contenga simbolos s/n: "))

        return dic_valores

# validaciones de entrada

def validar(input_valor: str ) -> int:
        """Verifica si un input str es numerico, si no lo es
        pedira que ingreses un numero """
        valor = input_valor        
        valide = True
        while valide:
                if (valor.isnumeric()) == False:
                        valor = valor_valido()
                else:
                        valide = False
        return int(valor)

def valor_valido() -> str:
        """Genera una nuevo input para reemplazar uno ya realizado"""
        valor_entrada = input("ingrese una valor valido: ").lower()
        return valor_entrada

def verificacion(valor_entrada: str) -> bool:
        """Verifica que un input cumpla con las reglas 
        que se  introdusca un Si o un NO
        y reitera que debes dar una respuesta"""

        valor = False
        estado = True
        valor_entrada = valor_entrada.lower()

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

# La verificaciones para que los input sean correctos 

def select_dicc(respuestas = preguntas()) -> list:
        
        list_total = ()
        if respuestas["con_numero"] == True :
                list_total += numb
        if respuestas["con_letras"] == True :
                list_total += alpha
        if respuestas["con_letras_mayusculas"] == True :
                list_total += tuple(x.upper() for x in alpha)
        if respuestas["con_simbolos"] == True :
                list_total += sign

        return list_total , respuestas["longitud"]

def code_selec( valores = select_dicc()) -> str:
        """selecciona de una lista un item al azar"""

        valor = random.choice(valores)
        return valor

def code_gerenerator(letras= None, longitud = None, interno = True ) -> str:
        """Gerenara un codigo aleatorio 
        necesita la logintud y una lista o tupla donde selecionar los simbolos
        el parametor interno es para identificar y se recibe de forma directa o no los parametros"""
        if interno == True:
                letras, longitud = select_dicc() #recibe tanto el diccionario como la longitud
        x = 0
        passcode = ''
        while x < longitud:
                passcode += code_selec(letras)
                x+=1
        return passcode

if __name__=="__main__":

        print(f"tu nuevo codigo es:  {code_gerenerator()}")