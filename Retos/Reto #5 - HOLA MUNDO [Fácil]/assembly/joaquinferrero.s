;
; Hola, Mundo!, en ensamblador para Atari ST
; Joaquin Ferrero, 20230201

        move.l  #mensaje,-(sp)		; dirección del texto
        move.w  #9,-(sp)		; Cconws, función del sistema: imprimir un texto
        trap    #1			; GEMDOS, llamada a sistema
        addq.l  #6,sp			; arreglo de pila

        move.w  #8,-(sp)		; Cnecin, función del sistema: esperar pulsación del teclado
        trap    #1			; GEMDOS, llamada a sistema
        addq.l  #2			; arreglo de pila

        clr.w	-(sp)			; Pterm0, función del sistema: regresar al escritorio
        trap    #1			; GEMDOS, llamada a sistema

mensaje:
        dc.b    "Hola, Mundo!", 13, 10, 0

