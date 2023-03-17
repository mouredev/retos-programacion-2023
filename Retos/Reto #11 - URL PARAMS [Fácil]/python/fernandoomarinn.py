def identificar_parametros(url):
    #  Se crea una lista, que se devolverá despues.
    parametros = []
    #  Nuevo parametro es la variable que irá guardando el parametro actual.
    nuevo_parametro = ""
    #  Variable booleana que nos indica si tenemos que leer o no la url.
    leer_parametro = False

    #  Se itera sobre cada caracter en la url.
    for caracter in url:
        #  Si el caracter es un igual, se activa la lectura de parametros, y el parametro nuevo se resetea.
        if caracter == "=":
            leer_parametro = True
            nuevo_parametro = ""

        #  Si es un ampersand, se acaba la lectura de del parametro, y se añade a la lista.
        elif caracter == "&":
            leer_parametro = False
            parametros.append(nuevo_parametro)

        #  Si leer parametro es True, se añade el caracter al parametro.
        else:
            if leer_parametro:
                nuevo_parametro += caracter

    #  Se añade lo ultimo leido a la lista, para evitar perder el ultimo parametro, ya que no tiene un &.
    parametros.append(nuevo_parametro)

    #  Se devuelve la lista.
    return parametros

