'''
/*
 * Dada una URL con parámetros, crea una función que obtenga sus valores.
 * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
 *
 * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
 * los parámetros serían ["2023", "0"]
 */
 '''

def valores_url(url: str) -> list:
    valores = []

    # Contamos el número de parámetros
    parametros = url.count("=")
    
    for _ in range(parametros):
        # Buscamos el valor
        principio = url.find("=")
        final = url.find("&")

        # Puede ser que final ya no esté (entonces devuelve -1).
        if final != -1:
            valor = url[principio+1:final]
            valores.append(valor)
        else:
            valor = url[principio+1::]
            valores.append(valor)
            break

        # Dejamos de reconocer el valor anterior como un valor y así podemos pasar al siguiente.
        url = url.replace("=","",1)
        url = url.replace("&","",1)
    
    return valores       

def main():
    url = "https://retosdeprogramacion.com?year=2023&challenge=0"
    valores_parametros = valores_url(url)
    print(f"Los parámetros de la url tienen como valores: {valores_parametros}")

    url = "https://retosdeprogramacion.com?year=2023&challenge=0&user=PabloGradolph" # url inventada
    valores_parametros = valores_url(url)
    print(f"Los parámetros de la url tienen como valores: {valores_parametros}")

    url = "http://example.com?product=1234&utm_source=google"
    valores_parametros = valores_url(url)
    print(f"Los parámetros de la url tienen como valores: {valores_parametros}")
    
if __name__ == "__main__":
    main()