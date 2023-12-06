#
# Dada una URL con parámetros, crea una función que obtenga sus valores.
# No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
#
# Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
# los parámetros serían ["2023", "0"]
#

def params(url):
    text=url.split('?')
    param=text[1].split('&')
    parametros=[]
    
    for i in param:
        param=i.split('=')
        parametros.append(param[1])
        
    print(parametros)

params('https://retosdeprogramacion.com?year=2023&challenge=0')