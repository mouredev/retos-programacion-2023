Imports System

Module Program
    Sub Main(args As String())

        'Punto 1: Haz un "Hola, mundo!"
            Console.WriteLine("Hola, Mundo!")

        'Punto 2: Crea variables de tipo String, numéricas (enteras y decimales) y Booleanas (o cualquier tipo de dato primitivo).
            Dim nombre As String = "AcrackSoft"
            Dim edad As Integer = 49
            Dim salario As Double = 1500.5
            Dim esEmpleado As Boolean = False



        'Punto 3: Crea una constante.
            Const PI As Double = 3.14159265359


        'Punto 4: Usa un if, else if y else.
            Dim numero As Integer = 49

            If numero < 0 Then
                Console.WriteLine("El número es negativo.")
            ElseIf numero = 0 Then
                Console.WriteLine("El número es igual a cero.")
            Else
                Console.WriteLine("El número es positivo.")
            End If


        'Punto 5: Crea estructuras como un array, lista, tupla, set y diccionario.
            ' Array
            Dim numeros(4) As Integer
            numeros(0) = 1
            numeros(1) = 2

            ' Lista
            Dim nombres As New List(Of String)
            nombres.Add("David")
            nombres.Add("Alba")

            ' Diccionario
            Dim telefonos As New Dictionary(Of String, String)
            telefonos("David") = "915554433"
            telefonos("Alba") = "914443322"
            'Espero que los teléfonos no sean de alguien :-)


        'Punto 6: Usa un for, foreach y un while.
            ' For
            For i As Integer = 1 To 5
                Console.WriteLine(i)
            Next

            ' For Each (para una lista)
            For Each nombre In nombres
                Console.WriteLine(nombre)
            Next

            ' While
            Dim contador As Integer = 0
            While contador < 5
                Console.WriteLine(contador)
                contador += 1
            End While


        'Punto 7: Crea diferentes funciones (con/sin parámetros y con/sin retorno).
            ' Función sin parámetros ni retorno
            Sub Saludar()
                Console.WriteLine("�Hola!")
            End Sub

            ' Función con parámetros y retorno
            Function Sumar(a As Integer, b As Integer) As Integer
                Return a + b
            End Function


        'Punto 8: Crea una clase.

            Class Persona
                Public Nombre As String
                Public Edad As Integer

                Public Sub New(nombre As String, edad As Integer)
                    Me.Nombre = nombre
                    Me.Edad = edad
                End Sub

                Public Sub Saludar()
                    Console.WriteLine("Hola, soy " & Nombre & " y tengo " & Edad & " años.")
                End Sub
            End Class

            ' Uso de la clase
            Dim persona1 As New Persona("AcrackSoft", 49)
                        persona1.Saludar()

            'Punto 9: Muestra el control de excepciones.
            Try
            Dim resultado As Integer = 10 / 0 ' DivisiÓn por cero
            Catch ex As Exception
                    Console.WriteLine("Error: " & ex.Message)
                End Try

    End Sub
End Module
