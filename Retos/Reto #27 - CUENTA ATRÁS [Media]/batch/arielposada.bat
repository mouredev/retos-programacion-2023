:: Ejemplo de uso: 
:: arielposada.bat 5 2
:: Crea una función que reciba dos parámetros para crear una cuenta atrás.
:: - El primero, representa el número en el que comienza la cuenta.
:: - El segundo, los segundos que tienen que transcurrir entre cada cuenta.
:: - Sólo se aceptan números enteros positivos.
:: - El programa finaliza al llegar a cero.
:: - Debes imprimir cada número de la cuenta atrás.
@echo off
setlocal enabledelayedexpansion

if "%~2"=="" (
    exit /b
)

set startNumber=%1
set delay=%2

if %startNumber% lss 1 (
    exit /b
)

if %delay% lss 1 (
    exit /b
)

:loop
if %startNumber% gtr 0 (
    echo %startNumber%
    timeout /t %delay% >nul
    set /a startNumber-=1
    goto loop
)

echo 0
endlocal
