' Ejemplo de uso: 
' cscript arielposada.vbs
' Realiza una conexión desde el lenguaje que hayas seleccionado a la siguiente base de datos MySQL:
' - Host: mysql-5707.dinaserver.com
' - Port: 3306
' - User: mouredev_read
' - Password: mouredev_pass
' - Database: moure_test
' 
' Una vez realices la conexión, lanza la siguiente consulta e imprime el resultado:
' - SELECT' FROM `challenges`

Option Explicit

Dim conn, rs, connectionString, query

Set conn = CreateObject("ADODB.Connection")
Set rs = CreateObject("ADODB.Recordset")

' Es necesario descargar el driver, y corregir la línea con la versión
' https://dev.mysql.com/downloads/connector/odbc/
connectionString = "Driver={MySQL ODBC 8.1 Unicode Driver};" & _
          "Server=mysql-5707.dinaserver.com;" & _
          "Port=3306;" & _
          "Database=moure_test;" & _
          "User=mouredev_read;" & _
          "Password=mouredev_pass;" & _
          "Option=3;"

conn.Open connectionString

query = "SELECT * FROM `challenges`"

Set rs = conn.Execute(query)

While Not rs.EOF
    WScript.Echo rs.Fields(0).Value & ", " & rs.Fields(1).Value & ", " & rs.Fields(2).Value & ", " & rs.Fields(3).Value
    rs.MoveNext
Wend

rs.Close
conn.Close
Set rs = Nothing
Set conn = Nothing
