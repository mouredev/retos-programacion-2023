# obtenemos una lista con los valores de los parámetros de la URL
def obtener_valores(url):
	return [p.split('=')[1] for p in url.split('?')[1].split('&')]

print(obtener_valores('https://retosdeprogramacion.com?year=2023&challenge=0'))