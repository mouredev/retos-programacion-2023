      ******************************************************************
      * Author: Jose Nardulli
      * Date: 28/8/2023
      * Purpose: learning
      * Tectonics: cobc
      ******************************************************************
       IDENTIFICATION DIVISION.
       PROGRAM-ID. YOUR-PROGRAM-NAME.
       DATA DIVISION.
       FILE SECTION.
       WORKING-STORAGE SECTION.
           01  WS-VARIABLESTRING PIC XXXX VALUE "Hola".
           01  WS-VARIABLEENTERA PIC 9(4) VALUE 256.
           01  WS-ARRAY.
               03 WS-ELEMENTO1 PIC 9(03) VALUE 1.
               03 WS-ELEMENTO2 PIC 9(03) VALUE 2.
               03 WS-ELEMENTO3 PIC 9(03) VALUE 3.
               03 WS-ELEMENTO4 PIC 9(03) VALUE 4.
               03 WS-ELEMENTO5 PIC 9(03) VALUE 5.
       PROCEDURE DIVISION.
       MAIN-PROCEDURE.
            DISPLAY "Hello world"
            DISPLAY "Esto imprime cosas "
            DISPLAY "ahi va la variable en string"
            DISPLAY WS-VARIABLESTRING
            DISPLAY "ahi va la variable numerica entera"
            DISPLAY WS-VARIABLEENTERA
            IF WS-VARIABLEENTERA = 256
               DISPLAY 'Que buen numero'
            END-IF
            DISPLAY 'esto es sparta, o un array'
            DISPLAY WS-ARRAY
            PERFORM 5 TIMES
               DISPLAY 'REPITO 5 VECES'
            END-PERFORM.   
            STOP RUN.
            
       END PROGRAM YOUR-PROGRAM-NAME.

