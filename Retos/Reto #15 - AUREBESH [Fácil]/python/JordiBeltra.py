#En este programa se pueden incluir más combinaciones de letras, o canviar la equivalencia a cada letra muy fácilmente.
#Pero, si se quisieran utilizar combinaciones de más de dos letras, requeriría código extra.

AlfabetoAurebesh = { #Letras del alfabeto Aurebesh.
    "a": "aurek",
    "b": "besh",
    "c": "cresh",
    "d": "dorn",
    "e": "esk",
    "f": "forn",
    "g": "grek",
    "h": "herf",
    "i": "isk",
    "j": "jenth",
    "k": "krill",
    "l": "leth",
    "m": "mern",
    "n": "nern",
    "o": "osk",
    "p": "peth",
    "q": "qek",
    "r": "resh",
    "s": "senth",
    "t": "trill",
    "u": "usk",
    "v": "vev",
    "w": "wesk",
    "x": "xesh",
    "y": "yirt",
    "z": "zerek", 
    "ae": "enth", #A partir de aquí las combinaciones dobles:
    "ch": "cherek",
    "eo": "onith",
    "kh": "krenth",
    "ng": "nen",
    "oo": "orenth",
    "sh": "shen",
    "th": "thesh",
    "ñ": "ñ", #Así se puede usar también la "ñ".
}

def EspanolAAurebesh(Texto: str) -> str: #Traducir de Español a Aurebesh.
    Mensaje = list(map(str, Texto.lower())) #Guarda en una lista el texto a traducir dígito por dígito. Se hace en minúsculas para que no de error.
    Traduccion = [] #Simplemente una lista para guardar la traducción.
    SaltarLetra = False #Utilizo esto para los carácteres de doble letra.
    for ch in range(len(Mensaje)):
        if SaltarLetra == False: #Aquí comprueba que no sea una combinación de dos letras.
            if Mensaje[ch] in AlfabetoAurebesh: #Comprueba que la letra correspondiente esté en el Alfabeto.
                try: #Sólo para asegurarse de que no salte un IndexError
                    if Mensaje[ch] + Mensaje[ch + 1] in AlfabetoAurebesh: #Comprueba si existe combinación de dos letras:
                        Traduccion.append(AlfabetoAurebesh[Mensaje[ch] + Mensaje[ch + 1]]) #En caso de que la haya, se añade la combinación de letras correspondientes. 
                        SaltarLetra = True #Se activa el código para saltar una letra (SaltarLetra = True).
                        continue
                    else: #Si no es una combinación de dos letras, simplemente se añade el carácter
                        Traduccion.append(AlfabetoAurebesh[Mensaje[ch]])
                except IndexError: #Si el índice que quieres comprobar se encuentra fuera de la lista, se ejecuta este código.
                    Traduccion.append(AlfabetoAurebesh[Mensaje[ch]])
            else: #Si el dígito comprobado NO está en el alfabeto, se añade ese carácter, y así dejamos ese dígito sin traducir.        
                Traduccion.append(Mensaje[ch])
        else: #Si era una combinación de dos letras, ya no hace falta que el programa se salte ninguna más (SaltarLetra = False).
            SaltarLetra = False
    return "".join(Traduccion) #Simplemente devuelve la lista en forma de string.

def AurebeshAEspanol(Texto: str) -> str: #Traducir de Aurebesh a Español.
    Guardado = [] #Aquí se irán guardando las letras hasta que el programa encuentre una letra que se encuentre en el alfabeto o hasta que se encuentre con un carácter que no está en el alfabeto (a-z).
    Mensaje = [] #Cada vez que se encuente una letra en el alfabeto, se añadirá aquí.
    for i in Texto:
        if i.isalpha(): #Comprueba si el dígito es una letra.
            Guardado.append(i) #Si lo es, se guarda en "Guardado".
        else: #El siguiente código se ejecuta sólo si no es una letra.
            try:
                Mensaje.append("".join(Guardado)) #Se añade a la lista todo lo que teníamos guardado en "Guardado", incluso si no se encuentra en el alfabeto.
                Guardado = [] #Se prepara la lista "Guardado" para guardar más dígitos.
                Mensaje.append(i) #Se añade al mensaje el carácter en cuestión.
            except:
                Guardado = [] #Se prepara "Guardado".
                continue
        if "".join(Guardado) in AlfabetoAurebesh.values(): #Esto comprueba en cada iteración si lo que tenemos guardado en "Guardado" se encuentra en el alfabeto.
            Mensaje.append("".join(Guardado)) #Se añade a "Mensaje" la letra correspondiente.
            Guardado = []
    Traduccion = []
    for ch in Mensaje: 
        if ch in list(AlfabetoAurebesh.values()): #Aquí comprueba si el carácter correspondiente se encuentra en el alfabeto (paso necesario, ya que hemos añadido carácteres que no pertenecen al alfabeto).
            Traduccion.append(list(AlfabetoAurebesh.keys())[list(AlfabetoAurebesh.values()).index(ch)]) #Lo que está haciendo aquí el programa es añadir a la lista "Traduccion" la llave correspondiente al valor que corresponde al item seleccionado de "Mensaje".
        else: #Si no se encuentra, simplemente añades el carácter en cuestión.
            Traduccion.append(ch)
    return "".join(Traduccion) #Devuelve la traducción en forma de string.

#FRASES DE EJEMPLO
print(EspanolAAurebesh("hola, moure!"))
print(AurebeshAEspanol("herfosklethaurek, mernoskuskreshesk!"))
print(AurebeshAEspanol(EspanolAAurebesh("esta frase se mostrará en español")))
print(EspanolAAurebesh(AurebeshAEspanol("esksenthtrillaurek fornreshaureksenthesk senthesk mernosksenthtrillreshaurekreshá esknern aurekuskresheskbesheskshen"))) #Aquí dice: "Esta frase se mostrará en Aurebesh".
print(AurebeshAEspanol("#reshesktrillosksenth_sentheskmernaureknernaureklethesksenth_mernoskuskresheskdorneskvev"))