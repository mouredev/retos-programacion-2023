' Ejemplo de uso:
' cscript arielposada.vbs

 '  Escribe un programa que reciba un texto y transforme lenguaje natural a
 '  "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 '   se caracteriza por sustituir caracteres alfanuméricos.
 '  - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 '    con el alfabeto y los números en "leet".
 '    (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 ' 

Option Explicit
Dim original, leet
original = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyzáéíóúñÁÉÍÓÚÑ"
leet = Array("4","8","(","|)","3","F","6","#","!","J","X","1","M","N","0","P","Q","12","5","7","U","V","VV","W","X","Y","2","@","ß","©","Ð","€","ƒ","6","H","!","J","|<","L","M","^","IV","O","Ø","ρ","Q","®","$","7","|_|","V","W","X","¥","Z","2")

Function replace(char)
    replace = char
    If  replace = "a" Then 
        replace = "4" 
    ElseIf  replace = "b" Then 
        replace = "|3" 
    ElseIf  replace = "c" Then 
        replace = "[" 
    ElseIf  replace = "d" Then 
        replace = ")"   
    ElseIf  replace = "e" Then 
        replace = "3" 
    ElseIf  replace = "f" Then 
        replace = "|=" 
    ElseIf  replace = "g" Then 
        replace = "&" 
    ElseIf  replace = "h" Then 
        replace = "#" 
    ElseIf  replace = "i" Then 
        replace = "1" 
    ElseIf  replace = "j" Then 
        replace = "_|" 
    ElseIf  replace = "k" Then 
        replace = ">|" 
    ElseIf  replace = "l" Then 
        replace = "1" 
    ElseIf  replace = "m" Then 
        replace =  "/\/\" 
    ElseIf  replace = "n" Then 
        replace = "^/" 
    ElseIf  replace = "o" Then 
        replace = "0" 
    ElseIf  replace = "p" Then 
        replace = "|*" 
    ElseIf  replace = "q" Then 
        replace = " _, Then " 
    ElseIf  replace = "r" Then 
        replace = "|2" 
    ElseIf  replace = "s" Then 
        replace = "5" 
    ElseIf  replace = "t" Then 
        replace = "7" 
    ElseIf  replace = "u" Then 
        replace = " _ Then " 
    ElseIf  replace = "v" Then 
        replace =  "\/" 
    ElseIf  replace = "w" Then 
        replace =  "\/\/" 
    ElseIf  replace = "x" Then 
        replace = "><" 
    ElseIf  replace = "y" Then 
        replace = "j" 
    ElseIf  replace = "z" Then 
        replace = "2"
    End If

End Function

Function toLeet(text)
    Dim i
    Dim result
    result = ""
    For i = 1 To Len(text)
        result = result & replace(Mid(text, i, 1))
    Next
    toLeet = result
End Function

Dim texto
texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit"
WScript.Echo "Texto original:"
WScript.Echo texto
WScript.Echo ""
WScript.Echo "Texto en lenguaje hacker (leet)"
WScript.Echo toLeet(texto)