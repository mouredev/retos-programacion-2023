''''/*
 * El día 128 del año celebramos en la comunidad el "Hola Mundo day"
 * Vamos a hacer "web scraping" sobre su sitio web: https://holamundo.day
 *
 * Crea un programa que se conecte a la web del evento e imprima únicamente la agenda de eventos
 * del día 8. Mostrando hora e información de cada uno.
 * Ejemplo: "16:00 | Bienvenida"
 *
 * Se permite utilizar librerías que nos faciliten esta tarea.
 *
 */'''


from bs4 import BeautifulSoup
import requests
url = "https://holamundo.day"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
#Aqui se hacen 2 cosas se especifica el tipo de etiqueta y nombre de la clase
proagen = soup.find_all('blockquote',class_="BlockquoteElement___StyledBlockquote-sc-1dtx4ci-0 slate-BlockquoteElement notion-quote unset-width")
k=0
#recorremo la informacion que tienen todo lo anterior
for i in proagen:
       #a k le aumentamos el valor
             k+=1
            #delimitamos desde y hasta donde queremos que nos muestre
             if(k>21 and k<=35):
                  #y mostramos
                  print(f"{i.text} ")               
       
#print(f" {programa} ")
