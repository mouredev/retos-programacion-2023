"""/*
 * Dada una URL con parámetros, crea una función que obtenga sus valores.
 * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
 *
 * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
 * los parámetros serían ["2023", "0"]
 */"""

def ask_url():
    return input("URL: ")

def get_url_parameters(url):
    url_string,parameters_string=url.split("?")
    return parameters_string.split("&")

def main():
    parameters = {}
    lista = get_url_parameters(ask_url())
    for parameter in lista:
        parameter_name,parameter_value = parameter.split("=")
        parameters[parameter_name] = parameter_value
    print(parameters)
if __name__ == "__main__":
    main()