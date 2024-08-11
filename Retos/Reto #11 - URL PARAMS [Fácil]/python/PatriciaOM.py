"""
Dada una URL con parámetros, crea una función que obtenga sus valores.
No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.

Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
los parámetros serían ["2023", "0"]

"""
def discover_parameters(url):
    if (url.find("?") > 0): #la función find retorna un entero positivo si lo encuentra
    #separamos por ? que es el caracter por el que empiezan los parámetros
        url_parameters = url.split("?") 
        parameters_value = url_parameters[1].split("&") #separamos los parámetros
        for parameter in parameters_value:
            total_values = parameter.split("=") #de cada parámetro separamos valor y descripcion
            value = total_values[1]
            print(value)
    else:
        print("No tiene parámetros")
    
discover_parameters("https://retosdeprogramacion.com?year=2023&challenge=0")
discover_parameters("https://www.google.com/")