#reto 2 lenguaje leet 1337->codificado 

"""
incia declarando diccionarios porque es estructura de datos
permite guardar los valores clave valor,
las listas encode y decode guardan el resultado obtenido cuando 
el usuario digite la parabra a convertir 
"""
import requests

#descarga el archivo txt desde mi repositorio github
url = "https://raw.githubusercontent.com/ccobando66/fast-api_api_movie/main/1337_base_languaje.txt"
#nombre de archivo separando por el delimitador (/) buscamos el ultimo valor con [-1]
nombre = url.split('/')[-1]
#realiza una peticion get al repositorio y traer el contenido
reponse = requests.get(url)

#genera el nuevo archivo usando open
with open(nombre,"w") as filename:
  filename.write(reponse.text)

lett_code:dict = {}
encode:list = []
decode:list = []
"""
 - with abre subfuncion y finaliza cuando acabe la tarea 
 - open funcion nativa de python para abrir documentos, modo = 'r' es decir
   abre el archivo modo lectura
 - as es un alias en este caso, se llama reader    
 
 funcion: transforma la data obtenida desde el archivo txt
 para almacenar en el diccionario
"""
with open("1337_base_languaje.txt","r") as reader:
     #funcion map transforma la data en list, usando el delimitador split(,)
     #se leer list->map(aplica los cambios a toda la data)->lambda(funcion anonina usa reader = read) 
     data = list(map(lambda read: read.split(','),reader))
     
     #recorre los datos obtenidos en la variable data devuelve una lista de 
     for value in data:
         #slicing para obtener solo una letra sera el valor el diccionario
         other_data = value[1:2]
         #acceder al indice 0 para establecer al primer valor de la lista para el key
         #Join para uni valores por in delimitador, map trasforma la data de list a str, que llega a de other data  
         lett_code[value[0]] = ''.join(map(str,other_data)).strip()


#recive el valor obtenido desde la variable parabra para recorrer leta por letra que se almacena en value
#busca la letra usando el metodo get, valida el resuldo si esta en el diccionario,si es none, agrega un espacio 
#todo se gurda en la lista encode usando el metodo append
for value in input(palabra :="conversor texto a 1337, escribe la frase: ").upper():
     encode.append(" ") if lett_code.get(value) is None else encode.append(lett_code.get(value)) 

#muestra el resultado codificado
print(f"encode 1337 = {''.join(map(str,encode))}")

#recorre todos los valores almacenados en la lista encode se almacena en value
for value in encode:
     #recorre todos los valores de diccionario usando items, k = key, v = value 
     for k,v in lett_code.items():
         #verifica si valor de la lista encode = value es igual a el valor del diccionario 
         if value == v: 
            #si es cierto, almacena la key asociada al valor encontrado en la lista decode 
            decode.append(k)
     else:
         #esta condicion valida los espacios entre cada palabra
         if value == " ":
             #si es cierto, almacena el espacio en decode
             decode.append(value)
         
#muestra el resultado decodificado
print(f"decode leet = {''.join(map(str ,decode))}")
    
    


    