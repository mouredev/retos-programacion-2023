: Ejemplo de uso: arielposada.bat 4
@echo off
setlocal enabledelayedexpansion

set "n=%1"

if %n% == 0 (
    echo __
    goto :eof
)

if %n% GTR 0 (
    call :repeat_space %n%
    echo !_spaces!_
    for /l %%i in (1, 1, %n%) do (
        set /a "spaces = 2 * (%n% - %%i)"
        call :repeat_space !spaces!
        echo !_spaces!_|
    )
) else (
    set /a "n = -1 * %n%"
    echo _
    for /l %%i in (1, 1, !n!) do (
        set /a "spaces = 2 * %%i - 1"
        call :repeat_space !spaces!
        echo !_spaces!|_
    )
)

goto :eof

:repeat_space
set "output="
for /l %%j in (1, 1, %1) do set "output= !output!"
set _spaces=!output!
goto :eof

