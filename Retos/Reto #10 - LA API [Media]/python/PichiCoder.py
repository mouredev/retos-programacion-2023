#Conexion con API de https://math.tools/api/numbers/

import urllib.request, json

url = urllib.request.urlopen("https://api.math.tools/numbers/nod")

jsonData = url.read()

parsed_json = json.loads(jsonData) #el json feo
pretty_json = json.dumps(parsed_json, indent=2) #el json lindo y fachero

fichero = open("C:/Users/Usuario/MyPythonScripts/Pruebas Varias/numbersDataJSON.txt", "w")
fichero.write(pretty_json)

print(pretty_json)
