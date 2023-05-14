      ******************************************************************
      * Author:  Fernando Marin
      * Date:    13-05-2023
      * Purpose:  Reto programacion Moure numero 19
      * Tectonics: cobc
      ******************************************************************
       IDENTIFICATION DIVISION.
       PROGRAM-ID. RETO-19.
       DATA DIVISION.
       FILE SECTION.
       WORKING-STORAGE SECTION.
       01  FRASE          PIC X(300) VALUE ' '.
       01  LONG-FRASE     PIC 999 VALUE 0.
       01  CONT-FRASE     PIC 999 VALUE 1.

       01  A              PIC 99 VALUE 0.
       01  E              PIC 99 VALUE 0.
       01  I              PIC 99 VALUE 0.
       01  O              PIC 99 VALUE 0.
       01  US             PIC 99 VALUE 0.

       PROCEDURE DIVISION.
       MAIN-PROCEDURE.

      * Crea un programa que analice texto y obtenga:
      * - Número total de palabras.
      * - Longitud media de las palabras.
      * - Número de oraciones del texto (cada vez que aparecen un punto).
      * - Encuentre la palabra más larga.



           DISPLAY 'INTRODUCE LA FRASE AQUI: '
           ACCEPT FRASE

           INSPECT FRASE
               TALLYING LONG-FRASE FOR CHARACTERS.

           PERFORM LONG-FRASE TIMES

               EVALUATE FRASE(CONT-FRASE:1)



                   WHEN 'A'
                   WHEN 'a'
                       ADD 1 TO A
                   WHEN 'E'
                   WHEN 'e'
                       ADD 1 TO E
                   WHEN 'I'
                   WHEN 'i'
                       ADD 1 TO I
                   WHEN 'O'
                   WHEN 'o'
                       ADD 1 TO O
                   WHEN 'U'
                   WHEN 'u'
                       ADD 1 TO US

                   END-EVALUATE
           ADD 1 TO CONT-FRASE
           END-PERFORM.


           DISPLAY 'NUMERO DE A: ' A
           DISPLAY 'NUMERO DE E: ' E
           DISPLAY 'NUMERO DE I: ' I
           DISPLAY 'NUMERO DE O: ' O
           DISPLAY 'NUMERO DE U: ' US


            STOP RUN.
       END PROGRAM RETO-19.
