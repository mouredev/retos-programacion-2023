from random import randint as rand

alpha = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
numb = ("1","2","3","4","5","6","7","8","9","0")
sign = ("!","@","#","$","%","^","&","*","(",")","_","+","-","=","{","}","[","]","<",">",",",".","?","/")


longitud = int(input("Indique la cantos digitos quieres tu clave: "))
con_numero = input("quieres que contenga numeros s/n: ")
con_letras = input("quieres que contenga letras s/n: ")
con_letras_mayusculas = input("quieres que contenga letras mayusculas s/n:")
con_simbolos = input("quieres que contenga simbolos s/n: ")


# validaciones de entrada

def validar(input_valor: str ) -> bool:
        """Verifica si un input str es numerico, si no lo es
        pedira que ingreses un numero """

        valide = True
        while valide:
                if input_valor.isnumeric() == False:
                        longitud = valor_valido()
                else:
                        valide = False

def valor_valido() -> str:
        """Genera una nuevo input para reemplazar uno ya realizado"""
        valor_entrada = input("ingrese una valor valido: ")
        return valor_entrada

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

# La verificaciones con para que los input sean correctos 

def select_dicc() -> dict:
        dicc_total = ()
        if con_numero == True :
                dicc_total += numb
        if con_letras == True :
                dicc_total += alpha
        if con_letras_mayusculas == True :
                dicc_total += (x.lower() for x in alpha)
        if con_simbolos == True :
                dicc_total += sign

        return dicc_total

def code_selec(valores: list) -> str:
        """selecciona de una lista un item al azar"""
        valor = rand.choise(valores)
        return valor

def code_gerenerator(longitud) -> str:
        """Gerenara un codigo aleatorio 
        necesita la logintud y una lista"""

        letras = select_dicc()
        passcode = ""
        for i in range(longitud + 1):
                passcode += code_selec(letras)


if __name__=="__main__":
        pass