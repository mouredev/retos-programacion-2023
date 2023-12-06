       IDENTIFICATION DIVISION.
       PROGRAM-ID. RETO6.
       AUTHOR. ROSWELL468.
       DATA DIVISION.

      ******************************************************************
      * DEFINICION DE VARIABLES, CONSTANSTES Y TABLAS.
      ******************************************************************
       WORKING-STORAGE SECTION.
       01 VARIABLES.
           05 WS-CURRENT-GAME  PIC X(2).
           05 WS-I             PIC 9(3).
           05 WS-SCORE-P1      PIC 9(3).
           05 WS-SCORE-P2      PIC 9(3).

       01 TABLES.
           05 WS-GAMES-AUX.
               10 WS-TBL-GAMES OCCURS 500 TIMES.
                   15 FILLER       PIC X(2).
                   15 WS-GAME-P1   PIC X(1).
                   15 FILLER       PIC X(3).
                   15 WS-GAME-P2   PIC X(1).
                   15 FILLER       PIC X(4).

           05 WS-GAME-RESULTS      PIC X(75)
              VALUE 'RR0PP0SS0LL0VV0' &
      -             'RS1RL1PR1PV1SP1SL1LP1LV1VS1VR1' &
      -             'SR2LR2RP2VP2PS2LS2PL2VL2SV2RV2'.
           05 FILLER REDEFINES WS-GAME-RESULTS.
               10 WS-GAMES      OCCURS 25 INDEXED BY WS-J.
                   15 WS-GAME   PIC X(2).
                   15 WS-RESULT PIC 9(1).

      ******************************************************************
      * PROGRAMA PRINCIPAL.
      ******************************************************************
       PROCEDURE DIVISION.

           INITIALIZE VARIABLES WS-GAMES-AUX
           MOVE '("P","R"), ("S","S"), ("R","S")' TO WS-GAMES-AUX
           PERFORM CHECK-GAME

           INITIALIZE VARIABLES WS-GAMES-AUX
           MOVE '("R","S"), ("S","R"), ("P","S")' TO WS-GAMES-AUX
           PERFORM CHECK-GAME

           INITIALIZE VARIABLES WS-GAMES-AUX
           MOVE '("R","S"), ("S","P"), ("L","S"), ("P","S"), ' &
      -     '("P","R"), ("V","V"), ("P","S"), ("L","L")' TO WS-GAMES-AUX
           PERFORM CHECK-GAME

           INITIALIZE VARIABLES WS-GAMES-AUX
           MOVE '("L","L")' TO WS-GAMES-AUX
           PERFORM CHECK-GAME

           INITIALIZE VARIABLES WS-GAMES-AUX
           MOVE '("R","V"), ("X","L")' TO WS-GAMES-AUX
           PERFORM CHECK-GAME

           PERFORM END-PROGRAM.

      ******************************************************************
      * PROCESAMIENTO DE LA PARTIDA, VALIDACION Y CALCULO DE RESULTADO
      ******************************************************************
       CHECK-GAME.

           PERFORM VARYING WS-I FROM 1 BY 1
           UNTIL WS-TBL-GAMES(WS-I) = SPACES
               MOVE WS-GAME-P1(WS-I) TO WS-CURRENT-GAME(1:1)
               MOVE WS-GAME-P2(WS-I) TO WS-CURRENT-GAME(2:1)
               SET WS-J TO 1
               SEARCH WS-GAMES
                   AT END PERFORM ERROR-VALIDATION
                   WHEN WS-GAME(WS-J) = WS-CURRENT-GAME
                       EVALUATE WS-RESULT(WS-J)
                           WHEN 1
                               ADD 1 TO WS-SCORE-P1
                           WHEN 2
                               ADD 1 TO WS-SCORE-P2
                       END-EVALUATE
               END-SEARCH
           END-PERFORM
           PERFORM DISPLAY-RESULT.

      ******************************************************************
      * MUESTRA EL RESULTADO DE LA PARTIDA.
      ******************************************************************
       DISPLAY-RESULT.

           EVALUATE TRUE
               WHEN WS-SCORE-P1 = WS-SCORE-P2
                   DISPLAY 'TIE'
               WHEN WS-SCORE-P1 > WS-SCORE-P2
                   DISPLAY 'PLAYER 1'
               WHEN OTHER
                   DISPLAY 'PLAYER 2'
           END-EVALUATE.

      ******************************************************************
      * ERROR EN DATOS DE ENTRADA.
      ******************************************************************
       ERROR-VALIDATION.

           DISPLAY 'DATOS DE ENTRADA INCORRECTOS'
           PERFORM END-PROGRAM.

      ******************************************************************
      * FIN DEL PROGRAMA.
      ******************************************************************
       END-PROGRAM.
           STOP RUN.
