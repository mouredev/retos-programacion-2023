' VBScript es una variacion del lenguaje de programacion Visual Basic
' Se utiliza principalmente en Windows para la ejecucion de script con tareas básicas.
' El motivo de su aprendizaje es su cercanía a VBA (Visual Basic for Applications),
' el cual es muy utilizado, principalmente en los Macros de Excel y de Power Point.
' Al ser similares, escribo soluciones para tanto VBA como VBScript en este repositorio.

Option Explicit

' Hola mundo!
WScript.Echo "Hola mundo!"

' Variables
Dim myVariable
myVariable = "Esto es una variable"
myVariable = "Aquí asigno un nuevo valor a la variable"

' Tipos de datos primitivos
Dim myString
myString = "Mi cadena de texto"
Dim myInt
myInt = 1
Dim myFloat
myFloat = 1.5
Dim myBool
myBool = True

' Constantes
' VBScript no tiene una forma nativa de definir constantes dentro de procedimientos o funciones. 
' Sin embargo, puedes definir constantes a nivel de script.
Const MY_CONSTANT = "No existen las constantes. Simplemente se nombran variables en mayúscula."

' Control de flujo
If myInt = 1 Then
    WScript.Echo "myInt vale 1"
ElseIf myInt = 2 Then
    WScript.Echo "myInt vale 2"
Else
    WScript.Echo "myInt no vale ni 1 ni 2"
End If

' Estructuras
' VBScript no tiene listas, tuplas o conjuntos nativos. Puedes usar arrays para simular listas.
Dim myList(3)
myList(0) = myString
myList(1) = myInt
myList(2) = myFloat
myList(3) = myBool

' Bucles
Dim index
For index = 0 To 9
    WScript.Echo index
Next

Dim item
For Each item In myList
    WScript.Echo item
Next

index = 0
Do While index < UBound(myList) + 1
    WScript.Echo myList(index)
    index = index + 1
Loop

' Funciones
Sub myFunction()
    WScript.Echo "Funcion simple"
End Sub

Function myFunctionWithReturn()
    myFunctionWithReturn = "Funcion con retorno"
End Function

Sub myFunctionWithParam(param)
    WScript.Echo "Funcion con un parametro de valor " & param
End Sub

myFunction()
WScript.Echo myFunctionWithReturn()
myFunctionWithParam(256)

' Clases
Class MyClass
    Private pName

    Public Property Let Name(value)
        pName = value
    End Property

    Public Property Get Name()
        Name = pName
    End Property

    Public Sub hello()
        WScript.Echo "Hola, " & pName & "!"
    End Sub
End Class

Dim myClassInstance
Set myClassInstance = New MyClass
myClassInstance.Name = "MoureDev"
WScript.Echo myClassInstance.Name
myClassInstance.hello()

' Excepciones
On Error Resume Next
WScript.Echo 0 / 0
If Err.Number <> 0 Then
    WScript.Echo "Se ha producido una excepcion"
End If
' On Error GoTo 0
WScript.Echo "Siempre se ejecuta el finally"
