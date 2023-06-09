import random
import os
import string
def clean():
    _so=os.name 
    if _so == "nt":
        os.system('cls')
    elif _so == "posix":
        os.system('clear')

random.randint(65, 91)
random.randint(97, 123)
def PasswordGen(Mayusculas,Numeros,Symbol,Longitud=8):
    #Bool={"N":False,"S":True}
    parameters=[Mayusculas,Numeros,Symbol]
    newparameters=list()
    for parameter in parameters:
        if parameter=="N":
            parameter=False
            newparameters.append(parameter)
        if parameter=="S":
            parameter=True
            newparameters.append(parameter)

    Mayusculas,Numeros,Symbol=newparameters
    Simbolos="!@#$%^&*" #8
    Mayus=string.ascii_uppercase
    Minus=string.ascii_lowercase
    Numbers=string.digits
    ResponsedPass=""

    while len(ResponsedPass)<=Longitud:
        Core=random.randint(0,3)
        if Core==0:#a-z
            charac=Minus[random.randint(0,(len(Minus)-1))]
            ResponsedPass+=str(charac)
        
        if Core==1 and Mayusculas:#A-Z
            charac=Mayus[random.randint(0,(len(Mayus)-1))]
            ResponsedPass+=str(charac)
        if Core==2 and Numeros:
            charac=Numbers[random.randint(0,(len(Numbers)-1))]
            ResponsedPass+=str(charac)    
        if Core==3 and Symbol:
            charac=Simbolos[random.randint(0,(len(Simbolos)-1))] #0-9
            ResponsedPass+=str(charac)

    return ResponsedPass
def main():
    _len=8
    _num="N"
    _sim="N"
    _upper="N"
    Contrasena=""
    while True:

        print("-"*40)
        print(f"1-Longitud.....(8-16): [{_len}]")
        print(f"2-Numeros......(S/N) : [{_num}]")
        print(f"3-Simbolos.....(S/N) : [{_sim}]")
        print(f"4-Mayusculas...(S/N) : [{_upper}]")
        print(f"5-Generar............: [{Contrasena}]")
        print(f"6-Salir")
        print("-"*40)
        opc = input("Elige una opción: ")
        
        if opc in ["1","2","3","4","5","6"]:
            opcion = int(opc)
        else:
            opcion=0
        if opcion == 1:
            try:
                _len = int(input("Longitud de Contraseña: "))
                if _len > 16:
                    _len=16
                if _len < 8:
                    _len=8        
            except:
                pass
        elif opcion == 2:
            try:
                _num=str(input("Numeros: N - S : ")).upper()
                
                if _num!="S": _num = "N"    
            except:
                pass
        elif opcion == 3:
            try:
                _sim=str(input("Simbolos: N - S : ")).upper()
                if  _sim!="S": _sim = "N"    
            except:
                pass
        elif opcion == 4:
            try:
                _upper=str(input("Mayusculas: N - S : ")).upper()
                if _upper!="S": _upper="N"

            except:
                pass
        elif opcion == 5:
            Contrasena=PasswordGen(_upper,_num,_sim,_len)
        elif opcion == 6:
            break
        clean()
        
        print(PasswordGen(_upper,_num,_sim,_len))
        print(PasswordGen(_upper,_num,_sim,_len))
if __name__=="__main__":
    main()