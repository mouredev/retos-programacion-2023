** ESTE LENGUAJE ERA EL QUE SE USABA CON LOS ORDENADORES AMSTRAD CPC, YO TENIA EL 6128.


05 REM Punto 1: Haz un "Hola, mundo!"
10 PRINT "Hola, Mundo!"
20 
30 REM Punto 2: Crea variables de tipo String, numéricas (enteras y decimales) y Booleanas (o cualquier tipo de dato primitivo).
40 LET nombre$ = "AcrackSoft"
50 LET edad% = 49
60 LET salario# = 1800.50
70 LET esEmpleado% = 1
80 
90 REM Punto 3: Crea una constante.
100 CONST PI# = 3.14159265359
110 
120 REM Punto 4: Usa un if, else if y else.
130 IF edad% < 18 THEN
140   PRINT "Eres menor de edad."
150 ELSEIF edad% >= 18 AND edad% <= 65 THEN
160   PRINT "Eres adulto."
170 ELSE
180   PRINT "Eres un adulto mayor."
190 END IF
200 
210 REM Punto 5: Crea estructuras como un array, lista, tupla, set y diccionario.
220 DIM numeros%(4)
230 FOR i = 1 TO 5
240   LET numeros%(i) = i
250 NEXT i
260 
270 REM Punto 6: Usa un for, (foreach y while no se aplican, que yo recuerde, a este lenguaje).
280 FOR i = 1 TO 5
290   PRINT "Número: "; numeros%(i)
300 NEXT i
310
320 REM Punto 7: Crea diferentes funciones (con/sin parámetros y con/sin retorno). 
325 REM Creación de una función sin parámetros y sin retorno
330 DEF PROC Saludar
340   PRINT "¡Hola!"
350 END PROC
360 
370 REM Llamada a la función
380 CALL Saludar
390 
400 REM Creación de una función con parámetros y con retorno
410 DEF FN Sumar(a%, b%)
420   = a% + b%
430 END FN
440 
450 LET resultado% = FN Sumar(5, 7)
460 PRINT "La suma es: "; resultado%
470 
480 REM Punto 8: Crea una clase.
490 DEF PROC Persona(nombre$, edad%)
500   PRIVATE nombre$
510   PRIVATE edad%
520   DEF PROC Saludar
530     PRINT "Hola, soy "; nombre$; " y tengo "; edad%; " años."
540   END PROC
550 END PROC
560 
570 REM Creación de una instancia de la clase Persona
580 LET persona = Persona("AcrackSoft", 49)
590 CALL persona.Saludar
600 
610 REM Punto 9: Muestra el control de excepciones.
620 ON ERROR GOTO ErrorHandler
630 LET division% = 10 / 0
640 END
650 
660 REM Manejo de errores
670 ErrorHandler:
680   PRINT "Error: "; ERR
690   RESUME NEXT
700 
710 END
