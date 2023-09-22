       IDENTIFICATION DIVISION.
       PROGRAM-ID. EjemploCOBOL.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 Mi-Texto      PIC X(30) VALUE "¡Hola desde COBOL!".
       01 Mi-Entero     PIC 9(3) VALUE 42.
       01 Mi-Decimal    PIC 9(3)V9(2) VALUE 3.14.
       01 Mi-Booleano   PIC 9(1) VALUE 1.
       01 Mi-Array      OCCURS 5 TIMES.
          05 Elemento   PIC 9(3).
       01 Mi-Lista      OCCURS 3 TIMES.
          05 Elemento   PIC X(10).
          05 FILLER     PIC X VALUE SPACE.
       01 Mi-Mapa.
          05 Clave1     PIC X(10) VALUE "clave1".
          05 Valor1     PIC X(10) VALUE "valor1".
          05 Clave2     PIC X(10) VALUE "clave2".
          05 Valor2     PIC X(10) VALUE "valor2".

       PROCEDURE DIVISION.
           DISPLAY "Hola, mundo!".
           DISPLAY "Mi texto: " Mi-Texto.
           DISPLAY "Mi entero: " Mi-Entero.
           DISPLAY "Mi decimal: " Mi-Decimal.
           DISPLAY "Mi booleano: " Mi-Booleano.
           IF Mi-Entero > 50
               DISPLAY "El número es mayor que 50".
           ELSE IF Mi-Entero < 50
               DISPLAY "El número es menor que 50".
           ELSE
               DISPLAY "El número es igual a 50".
           END-IF.
           PERFORM VARYING I FROM 1 BY 1 UNTIL I > 5
               DISPLAY "Elemento " I ": " Elemento(I)
           END-PERFORM.
           PERFORM VARYING J FROM 1 BY 1 UNTIL J > 3
               DISPLAY "Elemento " J ": " Elemento(J) " " Elemento(J + 1)
           END-PERFORM.
           PERFORM VARYING K FROM 1 BY 2 UNTIL K > 4
               DISPLAY "Clave: " Clave(K) " Valor: " Valor(K)
           END-PERFORM.
           MOVE ZERO TO K
           PERFORM UNTIL K >= 3
               DISPLAY "Contador: " K
               ADD 1 TO K
           END-PERFORM.
           STOP RUN.
