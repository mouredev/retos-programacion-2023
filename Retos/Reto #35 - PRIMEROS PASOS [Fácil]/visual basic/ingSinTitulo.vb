Imports System

Module Program
    Sub Main()
        ' Punto 1: Hola, mundo!
        Console.WriteLine("Hola, mundo!")

        ' Punto 2: Crea una variable de texto o string
        Dim miTexto As String = "¡Hola desde Visual Basic .NET!"

        ' Punto 3: Crea una variable de número entero
        Dim miEntero As Integer = 42

        ' Punto 4: Crea una variable de número con decimales
        Dim miDecimal As Double = 3.14

        ' Punto 5: Crea una variable de tipo booleano
        Dim miBooleano As Boolean = True

        ' Punto 6: Crea una constante
        Const miConstante As Integer = 10

        ' Punto 7: Usa un if, else if y else
        If miEntero > 50 Then
            Console.WriteLine("El número es mayor que 50")
        ElseIf miEntero < 50 Then
            Console.WriteLine("El número es menor que 50")
        Else
            Console.WriteLine("El número es igual a 50")
        End If

        ' Punto 8: Crea un Array (array en Visual Basic .NET)
        Dim miArray() As Integer = {1, 2, 3, 4, 5}

        ' Punto 9: Crea una lista (List en Visual Basic .NET)
        Dim miLista As New List(Of String) From {"Manzana", "Banana", "Naranja"}

        ' Punto 10: Crea una tupla (no aplicable en Visual Basic .NET)

        ' Punto 11: Crea un set (no aplicable en Visual Basic .NET)

        ' Punto 12: Crea un diccionario (Dictionary en Visual Basic .NET)
        Dim miDiccionario As New Dictionary(Of String, String)()
        miDiccionario.Add("clave1", "valor1")
        miDiccionario.Add("clave2", "valor2")

        ' Punto 13: Usa un ciclo for
        For Each elemento As Integer In miArray
            Console.WriteLine(elemento)
        Next

        ' Punto 14: Usa un ciclo foreach
        For Each elemento As String In miLista
            Console.WriteLine(elemento)
        Next

        ' Punto 15: Usa un ciclo while
        Dim contador As Integer = 0
        While contador < 3
            Console.WriteLine("Contador: " & contador)
            contador += 1
        End While

        ' Punto 16: Crea una función sin parámetros que no retorne nada
        Sub FuncionSinParametros()
            Console.WriteLine("Función sin parámetros")
        End Sub

        ' Punto 17: Crea una función con parámetros que no retorne nada
        Sub FuncionConParametros(param1 As Integer, param2 As String)
            Console.WriteLine("Parámetro 1: " & param1)
            Console.WriteLine("Parámetro 2: " & param2)
        End Sub

        ' Punto 18: Crea una función con parámetros que retorne valor
        Function FuncionConRetorno(a As Integer, b As Integer) As Integer
            Return a + b
        End Function

        ' Punto 19: Crea una clase (Class en Visual Basic .NET)
        Class Persona
            Public Property Nombre As String
            Public Property Edad As Integer
        End Class

        ' Punto 20: Muestra control de excepciones (Try...Catch en Visual Basic .NET)
        Try
            Dim resultado As Integer = miEntero \ 0
            Console.WriteLine(resultado)
        Catch ex As Exception
            Console.WriteLine("Error: " & ex.Message)
        End Try
    End Sub
End Module
