; Este era el código de los procesadores Z80 que tenían los ordenadores más populares en España en los años 80
; Amstrad CPCxxxx, Sinclair ZX, Sinclair ZX8x y Spectrum
; Espero no haber cometido muchos fallos en el código aunque me he asegurado revisando mis antiguos apuntes y
; ayudandome con ChatGPT ;-)

; Punto 1: Haz un "Hola, mundo!"
    org 100h  ; Dirección de inicio

    ld  hl, mensaje  ; Carga la dirección del mensaje en HL
    call    imprimir_mensaje  ; Llama a la función para imprimir el mensaje

    halt  ; Detiene la ejecución

    mensaje:
        db  "Hola Mundo!", 0  ; El mensaje a imprimir, seguido de byte nulo para identificar el final del mensaje

    imprimir_mensaje:
        ld  a, (hl)  ; Carga el byte actual de HL en el registro A
        inc hl  ; Incrementa HL para apuntar al siguiente byte

        ; Verifica si hemos llegado al final del mensaje (byte nulo)
        cp  0
        ret z  ; Si es igual a cero, salta de vuelta

        ; Si no es el final del mensaje, imprime el carácter y continúa
        call    imprimir_caracter

        ; Repite el proceso para el siguiente carácter del mensaje
        jr  imprimir_mensaje

    imprimir_caracter:
        ; Llama a la función de sistema operativo CONOUT para imprimir el carácter en pantalla
        ld  c, 2   ; Función de salida en Amstrad CPC6128 (CONOUT)
        ld  de, 1  ; Canal de salida estándar (pantalla)
        ld  a, (hl)  ; Carga el carácter en el registro A
        call    5  ; Llama a la función de sistema operativo CONOUT

        ret


; Punto 2: Crea variables de tipo String, numéricas (enteras y decimales) y Booleanas (o cualquier tipo de dato primitivo).

    ; Variables de tipo numérico
    LD BC, 1234 ; Un ejemplo de valor numérico en los registros BC

    ; Variables de tipo String
    LD HL, mensaje ; Carga la dirección del mensaje en HL

    ; Variables booleanas (usando 0 para falso y 1 para verdadero)
    LD A, 1 ; Carga el valor booleano "verdadero" en el registro A


; Punto 3: Crea una constante.
    ; Definir una constante
    MI_CONSTANTE equ 42


; Punto 4: Usa un if, else if y else.
    ; Supongamos que tenemos dos valores en registros A y B
    ; Comparar A y B
    CP A, B

    ; Salto condicional basado en el resultado de la comparación
    JR C, es_menor ; Salta si A es menor que B
    JR NC, no_es_menor ; Salta si A no es menor que B

    es_menor:
        ; Código si A es menor que B
        ...

    no_es_menor:
        ; Código si A no es menor que B
        ...


; Punto 5: Crea estructuras como un array, lista, tupla, set y diccionario.
    ; No es posible crear estructuras en ensamblador, que yo sepa.


; Punto 6: Usa un for, foreach y un while.
    ; Bucle while
    loop:
    ; Código del bucle
      ...

    ; Comprobar la condición de salida
    LD A, [contador]
    CP A, 10 ; Suponiendo que 10 es el límite
    JR NZ, loop ; Saltar de nuevo al bucle si la condición no se cumple

    ; Otro código después del bucle
    ...


; Punto 7: Crea diferentes funciones (con/sin parámetros y con/sin retorno).
     mi_funcion:
        ; Código de la función
        ...

        RET ; Retorno de la función


; Punto 8: Crea una clase.
     ; No es posible crear clases en ensamblador, que yo sepa.


; Punto 9: Muestra el control de excepciones.
; Las excepciones dependían mucho del sistema en el que se usara por lo que no es facil de implementar
; pero implementaré la interrupción de reinicio (RST) en el vector de interrupción 'RST_08H'
        ORG 32768 ; Dirección de inicio para el Amstrad CPC6128

        ; Definición del vector de interrupción
            LD HL, mi_rutina_interrupcion ; Carga la dirección de la rutina de interrupción
            LD (RST_08H), HL              ; Establece el vector de interrupción

        ; Instrucciones principales del programa
        main:
            ; Tu código principal aquí

        ; Rutina de interrupción personalizada
        mi_rutina_interrupcion:
            ; Tu manejo de la interrupción aquí
            ; Puede incluir la recuperación de datos, limpieza, etc.

            ; Finaliza la rutina de interrupción
            RETI

        ; Otro código y datos aquí

        ; Vector de interrupción (RST 08H)
        RST_08H EQU 08H

        ; Otros vectores de interrupción y datos aquí

        END