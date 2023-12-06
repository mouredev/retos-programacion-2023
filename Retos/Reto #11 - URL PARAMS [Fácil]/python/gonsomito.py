"""
 * Dada una URL con parámetros, crea una función que obtenga sus valores.
 * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
 *
 * Ejemplo: En la url https://retosdeprogramacion.com/?year=2023&challenge=0
 * los parámetros serían ["2023", "0"]
"""
def url_params(url):
    url=url.split("?")                      #parto en cachos la url y me quedo con el trozo final
    url=url[-1]
    url=url.split("&")                      #divido en trozos cogiendo & como límite de bloque
    dict_url={}
    for i in url:                           #creo un diccionario para almacenar parámetro y valor, porque nunca se sabe si haran falta
        url_left=i.split("=")[0]
        url_value=i.split("=")[1]
        dict_url[url_left]=url_value        #recorro la lista, qme quedo con ambos lados del igual y almaceno al diccionario
    print(list(dict_url.values()))          #muestro solo los valores en formato lista como en el ejemplo.
    
    
url_params("http://www.url.com/index.php?num=1234&txt=texto&coord=42,4587445&id=USR0112&auth=false") 
#sólo será válido para una url con este formato url?params.
