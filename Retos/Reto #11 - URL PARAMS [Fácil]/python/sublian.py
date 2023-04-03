#
 # Dada una URL con parámetros, crea una función que obtenga sus valores.
 # No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
 #
 # Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
 # los parámetros serían ["2023", "0"]
 #
 #como aporte adicional la funcion retorna una lista con los elementos encontrados
 #en caso contrario genera un mensaje de error y retorna un None
 
 
def get_url_parameters(url: str):
     try:
         
         values=url.split("?")[1].split("&")
         print(values)
         
         url_values=[]
         for value in values:
            val = value.split("=")[1]
            url_values.append(val)
            
         return(url_values)   
     except:
         print("could not obtain url parameters")  
         return(None)

           
print(get_url_parameters("https://retosdeprogramacion.com?year=2023&challenge=0"))     
print(get_url_parameters("https://retosdeprogramacion.com?year=2023&challenge=11&day=03&month=04&year=2023"))
print(get_url_parameters("https://retosdeprogramacion.com"))