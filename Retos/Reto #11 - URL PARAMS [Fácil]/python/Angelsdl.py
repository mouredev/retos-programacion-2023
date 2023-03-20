# ! Definimos la función y especificamos que el parámetro que debe pasarse es un string o cadena
def obtenerValoresURL(url: str):
    # ? Cortamos la URL por la ? que así se suelen pasar los parámetros por URL (método GET) en el desarrollo web.
    try:
        variablesAndValuesURL = url.split("?")[1]
        # ! Una vez tenemos solos las variables y sus valores, cortamos por la & para que tengamos cada variable y valor separados en diferentes cadenas
        variablesAndValuesSeparated = variablesAndValuesURL.split("&")
        # Creamos una lista donde se guardarán sólo los valores de la URL
        values = list()
        '''
        '' Creamos un bucle para recorrer todas las variables de las lista con sus valores y volvemos a cortar por el =
        '' para quedarnos sólo con los valores, cogemos el primer índice. Ej: ['Hola=Brais'] -> .split('=')[1] = 'Brais'
        ''' 
        for variableAndValue in variablesAndValuesSeparated:
            value = variableAndValue.split("=")[1]
            values.append(value)
        print(values)            
    except:
        print("Esa URL no tiene parámetros los cuáles desglosar")


obtenerValoresURL("https://www.google.com/") 
obtenerValoresURL("https://retosdeprogramacion.com?year=2023&challenge=0")