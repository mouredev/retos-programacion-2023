
#  * ¿Sabías que puedes leer información de Git y GitHub desde la gran
#  * mayoría de lenguajes de programación?
#  *
#  * Crea un programa que lea los últimos 10 commits de este repositorio y muestre:
#  * - Hash
#  * - Autor
#  * - Mensaje
#  * - Fecha y hora
#  *
#  * Ejemplo de salida:
#  * Commit 1 (el más reciente) | 12345A | MoureDev | Este es un commit | 24/04/2023 21: 00
#  *
#  * Se permite utilizar librerías que nos faciliten esta tarea.
#  *
#  */

import requests

from  token_logic import url, headers
# url = "https://api.github.com/repos/mouredev/retos-programacion-2023/commits"
# headers = {
#     'Accept': 'application/vnd.github+json',
#     'Authorization': 'Bearer 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',
#     'X-GitHub-Api-Version': '2022-11-28'
# }

response = requests.get(url,headers=headers)
data = response.json()
print
# print(help(json.dumps))

counter= 0
for commit in data[:10]:
    counter += 1
    Hash = commit["sha"]
    Autor = commit['commit']['author']['name']
    Mensaje = commit["commit"]["message"]
    C_Mensaje = Mensaje.replace("\n"," ")
    Fecha_y_hora = commit["commit"]["author"]["date"]

    #  * Ejemplo de salida:
#  * Commit 1 (el más reciente) | 12345A | MoureDev | Este es un commit | 24/04/2023 21: 00
    # print(Hash,Autor,C_Mensaje,Fecha_y_hora)
    print("Commit" ,counter, " mas recientes", Fecha_y_hora, Hash, Autor,C_Mensaje,)
    
   
   
  
    




   
   
    