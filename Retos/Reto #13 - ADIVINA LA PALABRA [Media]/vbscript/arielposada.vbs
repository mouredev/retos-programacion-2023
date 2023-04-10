' Ejemplo de uso:
' cscript arielposada.vbs

' Ejecutar una vez por juego

' Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos:
' - El juego comienza proponiendo una palabra aleatoria incompleta
'   - Por ejemplo "m_ur_d_v", y el número de intentos que le quedan
' - El usuario puede introducir únicamente una letra o una palabra (de la misma longitud que
'   la palabra a adivinar)
'   - Si escribe una letra y acierta, se muestra esa letra en la palabra. Si falla, se resta
'     uno al número de intentos
'   - Si escribe una resolución y acierta, finaliza el juego, en caso contrario, se resta uno
'     al número de intentos
'   - Si el contador de intentos llega a 0, el jugador pierde
' - La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar ocultando más del 60%
' - Puedes utilizar las palabras que quieras y el número de intentos que consideres

' Forzar la consola CScript: 
' https://stackoverflow.com/questions/4388879/vbscript-output-to-console

Dim oWSH, vbsInterpreter

Set oWSH = CreateObject("WScript.Shell")
vbsInterpreter = "cscript.exe"

Function ForceConsole()
If InStr(LCase(WScript.FullName), vbsInterpreter) = 0 Then
    oWSH.Run vbsInterpreter & " //NoLogo " & Chr(34) & WScript.ScriptFullName & Chr(34)
    WScript.Quit
End If
End Function

Function PalabraAleatoria()
  Dim palabras(13)
  palabras(0) = "representante"
  palabras(1) = "repositorio"
  palabras(2) = "versionado"
  palabras(3) = "observatorio"
  palabras(4) = "arquitectura"
  palabras(5) = "simbolizaba"
  palabras(6) = "comunicarse"
  palabras(7) = "especialista"
  palabras(8) = "mantenimiento"
  palabras(9) = "videoconferencia"
  palabras(10) = "circuitos"
  palabras(11) = "estructura"
  palabras(12) = "microprocesador"
  palabras(13) = "nanosegundo"

  Dim palabra
  
  Randomize
  palabra = palabras(Int(Rnd() * 14))

  PalabraAleatoria = palabra
End Function

Function ReemplazarCaracteresAleatorios(palabra)
  Dim posicion, nuevoCaracter, i, palabraTmp
  palabraTmp = palabra
  nuevoCaracter = "_"
  For i = 1 To 4
    Randomize
    posicion = Int((Len(palabraTmp) * Rnd()) + 1)
    palabraTmp = Replace(palabraTmp, Mid(palabraTmp, posicion, 1), nuevoCaracter)
  Next 
  ReemplazarCaracteresAleatorios = palabraTmp
End Function

Function EvaluarEntrada(palabra, palabraOriginal, entrada)
  If entrada = palabraOriginal Then
    palabra = entrada
    EvaluarEntrada = True
    Exit Function
  End If

  if Len(entrada) > 1 Then
    EvaluarEntrada = False
    Exit Function
  End If

  Dim i
  For i=1 To Len(palabraOriginal)
    If Mid(palabra, i, 1) = "_" Then
      If Mid(palabraOriginal, i, 1) = entrada Then
        palabra = Left(palabra, i-1) & entrada & Right(palabra, Len(palabra) - i )
        EvaluarEntrada = True
        Exit Function
      End If
    End If
  Next

  EvaluarEntrada = False
End Function



Call ForceConsole()

Dim miPalabra
miPalabra = PalabraAleatoria()

Dim miPalabraJuego
miPalabraJuego = ReemplazarCaracteresAleatorios(miPalabra)

Dim intentos
intentos = 4

WScript.Echo "Bienvenido al juego de adivina la palabra, la palabra aleatoria de esta ejecución es: "

Do While intentos >= 0
  WScript.Echo ""
  WScript.Echo miPalabraJuego
  WScript.Echo "Quedan " & intentos & " intentos, escribir un carácter o la palabra completa"
  Dim entradaIntento
  entradaIntento = WScript.StdIn.ReadLine()
  
  If EvaluarEntrada(miPalabraJuego, miPalabra, entradaIntento) = True Then
    If miPalabra = miPalabraJuego Then
      WScript.Echo ""
      WScript.Echo "Felicidades, has adivinado la palabra: "
      WScript.Echo miPalabra
      WScript.Echo ""
      Exit Do
    End If
    WScript.Echo "El carácter fue correcto, el número de intentos se conserva"
  Else
    intentos = intentos - 1
  End If
Loop


If intentos = 0 Then
  WScript.Echo "Se han terminado los intentos"
End If

WScript.Echo "Si desea volver a jugar, le recomendamos ejecutar nuevamente el script"