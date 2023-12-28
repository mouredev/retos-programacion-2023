
#Primer reto de programación realizado ;)

#empecé a estudiar python en Abril de 2023, 
#y ha sido una gran viaje!

# por ahora el programa no hace todo, haré comentarios sobre qué mejorar
#########################

#creación de lista verificación
n = 999 #quedo pendiente de buscar una libreria que rescate números
check_list = []
for i in range(1, n+1):
    check_list.append(i)

check_list_ope =['+', '-', '/', '*'] 

#fin de creación de listas de verificación

requeriment = input('Ingresa tu operación:')
lista = requeriment.split(' ')
print(lista)
converted_list = [str(num) if index % 2 != 0 else int(num) for index, num in enumerate(lista)]
#esta creación de lista de comprensión tiene un problema: en caso de que se ingrese
#un carácter que no  pueda ser convertido a número, crashea, por ejemplo un /

#además, se debe incluir eventualmente que acepte números negativos y decimales. 

print(converted_list) #validación de creación.

def validacion(converted_list):
    g = 0
    for i in converted_list:
        if (type(i) == int) and (i in check_list): #falta agregar que la conversión sea 
            g += 1
        elif (type(i) == str) and (i in check_list_ope):
            g += 1
    if g == len(converted_list):
        return True
    else:
        return False   
    
if validacion(converted_list):
    print('True')
else:
    print('False')
    
    
    
         
    








    

        




