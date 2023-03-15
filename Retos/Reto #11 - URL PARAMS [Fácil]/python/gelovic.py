# obtenemos una lista con los valores de los parámetros de la URL
def obtener_valores(url):
	try:
		parametros = url.split('?')[1].split('&') # obtenemos una lista con los parámetros
		parametros = dict([p.split('=') for p in parametros]) # creamos un diccionario clave/valor
		return [v for v in parametros.values()] # devolvemos una lista con los valores
	except:
		return False # si no hay parámetros o la URL está mal formada, devolvemos False

url = 'https://retosdeprogramacion.com?year=2023&challenge=0'
valores = obtener_valores(url)
print(valores)