' Ejemplo de uso: 
' cscript arielposada.vbs 
' Crea un programa que lea los últimos 10 commits de este repositorio y muestre:
' - Hash
' - Autor
' - Mensaje
' - Fecha y hora 
' Ejemplo de salida:
' Commit 1 (el más reciente) | 12345A | MoureDev | Este es un commit | 24/04/2023 21:00 
' Se permite utilizar librerías que nos faciliten esta tarea.
'

Option Explicit
Dim objShell 
' Se utiliza la herramienta de consola desde aquí...
Set objShell = CreateObject("CScript.Shell")
' El comando ejecuta todo
objShell.Exec("git log --pretty=format:'%H | %an | %s | %cd' -10")
