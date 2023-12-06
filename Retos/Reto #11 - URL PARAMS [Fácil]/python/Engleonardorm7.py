# /*
#  * Dada una URL con parámetros, crea una función que obtenga sus valores.
#  * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
#  *
#  * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
#  * los parámetros serían ["2023", "0"]
#  */

def get_parameters(url):
    
    parameters=url.split('?')
    
    parameters=parameters[1].split('&')
    values=[]
    for each in parameters:
        parameters=each.split("=")
        values.append(parameters[1])
    return (values)

print(get_parameters('https://retosdeprogramacion.com?year=2023&challenge=0'))
