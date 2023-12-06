# Dada una URL con parámetros, crea una función que obtenga sus valores.
# No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
# Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
# los parámetros serían ["2023", "0"]

def param_search(link):
    result = []
    params = link.split('?')[1].split("&")

    for param in params:
        result.append(param.split("=")[1])
        
    print(result)

param_search('https://retosdeprogramacion.com?year=2023&challenge=0&reto=11&proceso=terminado')
