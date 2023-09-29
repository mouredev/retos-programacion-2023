:: Batch
@echo off
:: Hola mundo
echo Hola mundo!

:: Variables
set myVariable=Esto es una variable
set myVariable=Aquí asigno un nuevo valor a la variable

:: Tipos de datos primitivos
set myString=Mi cadena de texto
set myInt=1
set myFloat=1.5
set myBool=True

:: Control de flujo
if %myInt%==1 (
    echo myInt vale 1
) else if %myInt%==2 (
    echo myInt vale 2
) else (
    echo myInt no vale ni 1 ni 2
)

:: Bucles
for /L %%i in (0,1,9) do (
    echo %%i
)

:: Usando un pseudo-array para la lista
set myList[0]=%myString%
set myList[1]=%myInt%
set myList[2]=%myFloat%
set myList[3]=%myBool%

echo Iterando arreglo

setlocal enabledelayedexpansion
for /L %%i in (0,1,3) do (
    echo !myList[%%i]!
)

:: Funciones
:myFunction
echo Funcion simple
:: Al terminar la función va a la etiqueta mencionada
goto RETURN_1

:myFunctionWithReturn
setlocal
set "result=Funcion con retorno"
endlocal & set "myFunctionWithReturnResult=%result%" & goto RETURN_2

:myFunctionWithParam
echo Funcion con un parametro de valor %1
goto RETURN_3

call :myFunction
:: Es importante mantener etiquetas para que una vez que termine la función, vaya a dicho
:: bloque de código
:RETURN_1
call :myFunctionWithReturn
:RETURN_2
echo %myFunctionWithReturnResult%
call :myFunctionWithParam 256
:RETURN_3

:: Excepciones
:: Batch no tiene un manejo de excepciones nativo. Pero se puede obtener el nivel de error
set /a "result=0/0"
if %errorlevel% neq 0 (
    echo Se ha producido una excepcion
)
echo Siempre se ejecuta el finally

exit /b
