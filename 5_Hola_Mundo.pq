(nombre as text) as text =>
let
    Nombre = nombre,
    #"Saludo Personalizado" = "!Hola, " & Nombre & "!"
in
     #"Saludo Personalizado"