' Ejemplo de uso:
'   cscript arielposada.vbs
' 
' Crea un generador de números pseudoaleatorios entre 0 y 100.
' - No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
'
' Es más complicado de lo que parece...
Option Explicit

Function CurrentTimeMilliseconds()
    CurrentTimeMilliseconds = CLng(Timer * 1000)  Mod 1000
End Function

Function PseudoAleatorio(min,max)
    PseudoAleatorio = min + CInt((CurrentTimeMilliseconds/1000)*(max-min))
End Function

WScript.Echo PseudoAleatorio(0,100)
