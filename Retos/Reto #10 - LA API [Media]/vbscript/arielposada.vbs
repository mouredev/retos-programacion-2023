' Ejemplo de uso:
' cscript arielposada.vbs
 ' Llamar a una API es una de las tareas más comunes en programación.
 '
 ' Implementa una llamada HTTP a una API (la que tú quieras) y muestra su
 ' resultado a través de la terminal. Por ejemplo: Pokémon, Marvel...
 '
 ' Aquí tienes un listado de posibles APIs: 
 ' https://github.com/public-apis/public-apis
 ' 

Option Explicit
' BoardGameGeek XML API
' https://api.geekdo.com/xmlapi2

Dim url, xmlHttp, xml, xmlDoc, boardgame, name, yearpublished

' Establecer URL del API REST, con la búsqueda del juego llamado "Chess"
url = "https://api.geekdo.com/xmlapi/search?exact=1&search=Chess"

set xmlHttp = CreateObject("MSXML2.XMLHTTP")
xmlHttp.Open "GET", url, False
xmlHttp.send

Set xmlDoc = CreateObject("MSXML2.DOMDocument")
xml = xmlHttp.responseText
xmlDoc.loadxml xml

Set boardgame = xmlDoc.getElementsByTagName("boardgame")(0)
Set name = boardgame.getElementsByTagName("name")(0)
Set yearpublished = boardgame.getElementsByTagName("yearpublished")(0)

WScript.Echo "Servicio: https://api.geekdo.com/xmlapi/search?exact=1&search=Chess"
WScript.Echo "Respuesta XML:"
WScript.Echo xml
WScript.Echo "Datos: "
WScript.Echo "Juego de mesa: " & boardgame.Text
WScript.Echo "Nombre: " & name.Text
WScript.Echo "Fecha en que fue publicado: " & yearpublished.Text