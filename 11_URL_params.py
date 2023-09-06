"""

/*
 * Dada una URL con parámetros, crea una función que obtenga sus valores.
 * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
 *
 * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
 * los parámetros serían ["2023", "0"]

 Link para aprender sobre parametros de uan URL:
 https://es.semrush.com/blog/parametros-url/
 
 */

"""


def obtener_parametros_url(url: str) -> list:
  """
    Esta función toma una URL como entrada y extrae y muestra los valores de los parámetros presentes en la URL.

    Args:
        url (str): La URL de la cual se extraerán los parámetros.

    Returns:
        None: La función imprime los valores de los parámetros o un mensaje si la URL no tiene parámetros.
    """
  
  # Paso 1: Dividir la URL a partir del carácter '?', donde comienzan los parámetros
  partes = url.split("?")

  # Paso 2: Comprobar si existen parámetros en la URL
  if len(partes) == 2:
    # Paso 3: Seleccionar el índice 1 de la lista partes para obtener la subcadena de parámetros y eliminar posibles espacios en blanco
    texto_parametros = partes[1].strip()

    # Paso 4: Definir una lista para almacenar los valores de los parámetros de la URL
    valores_parametros = []

    # Paso 5: Iterar sobre la lista de parámetros divididos por '&'
    for parametro in texto_parametros.split("&"):
      
      # Dividir cada parámetro en variable y valor
      variable, valor = parametro.split("=")
      
      # Inserta valor en la lista
      valores_parametros.append(valor)

    # Paso 6: Imprimir los valores de los parámetros
    return print(valores_parametros)

  else:
    # Paso 7: Si no hay parámetros en la URL, imprimir un mensaje
    return print("La URL no tiene parámetros.")


if __name__ == "__main__":
  # Ejemplo de uso
  url = 'https://retosdeprogramacion.com?year=2023&challenge=0'
  obtener_parametros_url(url)
