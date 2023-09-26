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
       01  FRASE          PIC X(300)      VALUE ' '.

       01  CONT           PIC 999         VALUE 0.
       01  CONT1          PIC 999         VALUE 2.

       01  INICIO-LARGA   PIC 99          VALUE 0.
       01  INICIO-TEMP    PIC 99          VALUE 0.
       01  CONT-LARGA     PIC 99          VALUE 0.
       01  CONT-TEMP      PIC 99          VALUE 0.
       01  MAS-LARGA      PIC X(30)       VALUE ' '.

       01  CARACTERES     PIC 999         VALUE 0.
       01  LARGO          PIC 999         VALUE 0.
       01  NUM-PALABRAS   PIC 99          VALUE 1.
       01  LONG-MEDIA     PIC 99          VALUE 0.
       01  NUM-ORACIONES  PIC 99          VALUE 0.

       PROCEDURE DIVISION.
       MAIN-PROCEDURE.

      * Crea un programa que analice texto y obtenga:
      * - Número total de palabras.
      * - Longitud media de las palabras.
      * - Número de oraciones del texto (cada vez que aparecen un punto).
      * - Encuentre la palabra más larga.

           STRING
           'ESTA VA A SER MI FRASE DE PRUEBA. TIENE QUE TENER COSAS.',
           'EN VARIAS MEDIDAS. VARIAS ORACIONES Y UNA PALABRA GRANDE.',
           'Y TIENE QUE TERMINAR EN ALGUN PUNTO.' DELIMITED BY SIZE
           INTO FRASE

      *    ACCEPT FRASE
           DISPLAY FRASE

      *    EMPEZAMOS MIDIENDO LOS CARACTERES TOTALES

           INSPECT FRASE
           TALLYING LARGO FOR CHARACTERS.

      *    SE EMPIEZA CON EL LOOP

           PERFORM VARYING CONT FROM 1 BY 1 UNTIL CONT > LARGO

      *    CONTAMOS LOS CARACTERES

           IF FRASE(CONT:1) NOT = ' ' THEN
               ADD 1 TO CARACTERES
           END-IF

      *    CONTAMOS LAS ORACIONES

           IF FRASE(CONT:1) = '.'
               ADD 1 TO NUM-ORACIONES
           END-IF

      *    CONTAMOS LAS PALABRAS

           IF FRASE(CONT:1) = ' ' AND FRASE(CONT1:1) NOT = ' ' OR
               FRASE(CONT:1) = '.' AND FRASE(CONT1:1) NOT = ' ' THEN
               ADD 1 TO NUM-PALABRAS
           END-IF

      *    EVITAMOS SALIR DE LA LONGITUD DE LA FRASE CON LA VARIABLE

           IF CONT1 = LARGO THEN
               COMPUTE CONT1 = LARGO - 1
           END-IF


      *    SE CALCULA LA PALABRA MAS LARGA
           IF FRASE(CONT:1) NOT = ' ' AND FRASE(CONT:1) NOT = '.' THEN
               IF CONT-TEMP NOT = 0 THEN
                   ADD 1 TO CONT-TEMP
               ELSE
                   ADD 1 TO CONT-TEMP
                   MOVE CONT TO INICIO-TEMP
               END-IF

           ELSE
               IF CONT-TEMP > CONT-LARGA THEN
                   MOVE CONT-TEMP TO CONT-LARGA
                   MOVE INICIO-TEMP TO INICIO-LARGA
                   MOVE FRASE(INICIO-LARGA:CONT-LARGA) TO MAS-LARGA
                   MOVE 0 TO CONT-TEMP
                   MOVE 0 TO INICIO-TEMP
               ELSE
                   MOVE 0 TO CONT-TEMP
                   MOVE 0 TO INICIO-TEMP
               END-IF
           END-IF

      *    AÑADIMOS 1 A LA VARIABLE CONTADOR
           ADD 1 TO CONT1
           END-PERFORM

           COMPUTE LONG-MEDIA = (CARACTERES - NUM-ORACIONES)
           / NUM-PALABRAS

           DISPLAY 'LAS PALABRAS SERIAN: ' NUM-PALABRAS
           DISPLAY 'LAS ORACIONES SERIAN: ' NUM-ORACIONES
           DISPLAY 'LOS CARACTERES TOTALES SERIAN: ' CARACTERES
           DISPLAY 'LA LONGITUD MEDIA DE LAS PALABRAS ES: ' LONG-MEDIA

           DISPLAY 'LA PALABRA MAS LARGA ES: ' MAS-LARGA





            STOP RUN.
       END PROGRAM RETO-19.
