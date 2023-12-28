      ******************************************************************
      * Author:    Fernando Marin
      * Date:      22/07/2023
      * Purpose:   Retro de programacion 29 MoureDev
      * Tectonics: cobc
      ******************************************************************
       IDENTIFICATION DIVISION.
       PROGRAM-ID. RETO29.
       DATA DIVISION.
       FILE SECTION.
       WORKING-STORAGE SECTION.

       01 TABLA.
           03 REPETIDAS          PIC X(1) VALUE '*' OCCURS 140 .

       01 FRASE1                 PIC X(140).
       01 FRASE2                 PIC X(140).

       01 INDICE                 PIC 9(3).
       01 INDICE-TABLA           PIC 9(2) VALUE 1.
       PROCEDURE DIVISION.
       MAIN-PROCEDURE.

      *     COMO COBOL ES UN POQUITO ESPECIAL NO PUEDO DEVOLVER
      *     EL RESULTADO EN UN ARRAY, ASI QUE LO DEVUELVO EN UNA
      *     TABLA DE COBOL, QUE SERIA LO MAS PARECIDO QUE HAY A UN ARRAY.


      *     SE ACEPTAN AMBAS FRASES.
            DISPLAY "Introduce una frase de 140 caracteres."
            ACCEPT FRASE1

            DISPLAY "Introduce la otra frase parecida."
            ACCEPT FRASE2

      *---------------------------------------------------------------
      *     SE COMPRUEBA LETRA A LETRA SI SON IGUALES.
      *     SI NO LO SON, SE GUARDA EL VALOR EN LA TABLA
            PERFORM VARYING INDICE
            FROM 1 BY 1

            UNTIL INDICE = 140

                IF FRASE1(INDICE:1) NOT = FRASE2(INDICE:1) THEN
                    MOVE FRASE1(INDICE:1) TO REPETIDAS(INDICE-TABLA)
                    ADD 1 TO INDICE-TABLA
                END-IF

            END-PERFORM

      *-----------------------------------------------------------------
      *     AL FINAL, SE IMPRIMEN LOS VALORES DE LA TABLA
            MOVE 1 TO INDICE-TABLA

            PERFORM UNTIL REPETIDAS(INDICE-TABLA) = '*'
                DISPLAY REPETIDAS(INDICE-TABLA)
                ADD 1 TO INDICE-TABLA
            END-PERFORM

            STOP RUN.
       END PROGRAM RETO29.
