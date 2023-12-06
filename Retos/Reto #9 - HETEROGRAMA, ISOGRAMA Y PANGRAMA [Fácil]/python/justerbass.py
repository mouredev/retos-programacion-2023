import re

abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]

def heterograma (text):

    for chart in abc:
        contador = len(re.findall( chart,text))
        if contador > 1:
            print("el texto ingrasado no es heterograma")
            break
    else:
        print("el texto es heterograma")

heterograma ("quieres probar tu codigo")
heterograma ("tu code in my har")

def isograma (text):
    cantidad = []
    for chart in abc:
        contador = len(re.findall( chart,text))
        cantidad.append(contador)
    
    valores = []
    for items in cantidad:
        if items not in valores:
            valores.append(items)

    valores.remove(0)
    if min(valores) == max(valores):
        print("el texto es isograma")    
    else:
        print("el texto ingrasado no es isograma")

isograma ("quieres probar tu codigo")
isograma ("fome catrin")

def pangrama (text):

    for chart in abc:
        contador = len(re.findall( chart,text))
        
        if contador == 0:
            print("el texto ingrasado no es pangrama")
            break
    else:
        print("el texto es pangrama")

pangrama ("quieres probar tu codigo")
pangrama ("un jugoso zumo de piña y kiwi bien frío es exquisito y no lleva alcohol")
