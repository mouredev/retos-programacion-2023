"""
* Crea una función que sea capaz de transformar Español al lenguaje básico del universo Star Wars: el "Aurebesh".
* Puedes dejar sin transformar los caracteres que no existan en "Aurebesh".
* También tiene que ser capaz de traducir en sentido contrario.
* ¿Lo has conseguido? Nómbrame en twitter.com/mouredev y escríbeme algo en Aurebesh.
* ¡Que la fuerza os acompañe!
"""
#---------------------------------------------------------------Hagamos transcripción ESP -> AUR
def espanol_aurekbesh(texto_esp, diccionario):
    trans_text=""
    i=0
    while i < len(texto_esp):
        if texto_esp[i].isalpha() and texto_esp[i].isascii():                   #comprobar que solo alfabeto y sin tildes 
            if texto_esp[i:i+2] in ("ae","ch","eo","kh","ng" "oo","sh","th"):   #comprobar el siguiente char para ver si doble
                trans_text = trans_text + diccionario[texto_esp[i:i+2]]         #doble char y sumo 1 al indice
                i=i+1
            else:
                trans_text = trans_text + diccionario[texto_esp[i]]             #transcripcion directa del char
        else:
            trans_text = trans_text + texto_esp[i]                              #no es una letra
        i=i+1
    return trans_text.upper()
    
#--------------------------------------------------------------Hagamos la transcripción AUR -> ESP
def aurekbesh_espanol(texto_aur, diccionario):           
    trans_text=""
    i, x = 0, 6                                                     #indice y aux (aux siempre es 3 por que es el min de bloque aureb)
    while i < len(texto_aur):
        if texto_aur[i].isalpha():
            while x > 1:
                if texto_aur[i:i+x] in diccionario.values():        #comprobar con un char menos y si coincide busco el index del dicc
                    trans_text = trans_text + list(diccionario.keys())[list(diccionario.values()).index(texto_aur[i:i+x])]
                    break
                x=x-1
        else:
            trans_text = trans_text + texto_aur[i]                  #no hay transcripción, pongo el char tal cual
            x=1                                                     #reinicio sección para seguir comprobando
        i=i+x
        x=6                                                         
    return trans_text.upper()
    
#--------------------------------------------------------------HagamosArranca el Main 
diccionario={"a":"aurek", "b":"besh", "c":"cresh", "ch":"cherek", "d":"dorn", "e":"esk", "ae":"enth", 
            "eo":"onith", "f":"forn","g":"grek","h":"herf", "i":"isk", "j":"jenth",
            "k":"krill", "kh":"krenth", "l":"leth", "m":"mern", "n":"nern", "ng":"nen", 
            "o":"osk", "oo":"orenth", "p":"peth", "q":"qek", "r":"resh", "s":"senth", "sh":"sen",
            "t":"trill", "th":"thesh", "u":"usk", "v":"vev", "w":"wesk", "x":"xesh", "y":"yirt", "z":"zerek"}
trans_text=""
while trans_text=="":                                             #lo puebo dentro de un while que traduce ESP->AUR y viceversa el mismo
    trans_text = input("Dame un texto para transcribir o pulsa ENTER para salir: ")
    trans_text=espanol_aurekbesh(trans_text.lower(), diccionario)
    print(trans_text)
    trans_text=aurekbesh_espanol(trans_text.lower(), diccionario)
    print(trans_text)
    if trans_text == "": break                                    #para salir del bucle No escribo nada 
