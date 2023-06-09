from requests_html import HTMLSession
"""
instalar  libreria pip install  requests_html

"""



def main():
     # iniciar objeto de sesion y obtener la pagina 
     session=HTMLSession()
     page=session.get("https://holamundo.day")
     
     """
       al inspecionar la pagina puedes ver que cada  evento de la 
       charla usa una etiqueta blockquote solo hay que ver cuantos elementos son 
       y traer el rango en este caso [19:34]
       postd: los conte de manera manual para saber el rango  debe de haber una mejor manera
       de hacerlo
    """
    
     for event in page.html.find("blockquote")[19:34]:
         print(event.text)

if __name__=='__main__':
    main()