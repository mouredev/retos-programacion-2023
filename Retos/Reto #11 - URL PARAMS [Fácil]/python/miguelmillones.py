'''Dada una URL con parámetros, crea una función que obtenga sus valores.
No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
 *
 * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
 * los parámetros serían ["2023", "0"]
'''
VALUES=[]

def url_parameter(url):
    value=''
    point=[]
    tamano=len(url)
    P=0
    while P<tamano:
        point=url[P]
        if point=='=':
            while not url[P+1]=='&':
                P+=1
                value=value+url[P]
                if P==tamano-1:
                    url=url+'&'
            VALUES.append(value)
            value=''
        P+=1
    return VALUES

URL=input("Ingrese url: \n")
print(url_parameter(URL))
