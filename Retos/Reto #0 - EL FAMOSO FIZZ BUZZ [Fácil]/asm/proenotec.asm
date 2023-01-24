;   ////////////////////////////////
;  //  ASM, The fast and furious //
; //     by MCC at Proenotec    //
;////////////////////////////////
;
;
; * Escribe un programa que muestre por consola (con un print) los
; * números de 1 a 100 (ambos incluidos y con un salto de línea entre
; * cada impresión), sustituyendo los siguientes:
; * - Múltiplos de 3 por la palabra "fizz".
; * - Múltiplos de 5 por la palabra "buzz".
; * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
;

.data
fizz: .ascii "fizz\n"
buzz: .ascii "buzz\n"
fizzbuzz: .ascii "fizzbuzz\n"
saltoLinea: .ascii "\n"

.global main
main:
  mov $1, %eax   ; inicializa el registro %eax con cero

buclePrincipal:
  cmp $101, %eax    ; compara %eax con 101
  jge end_loop      ; si %eax es mayor o igual a 101 terminamos
  mov $15, %ebx     ; cargo 15 en %ebx
  xor %edx, %edx    ; limpio el registro %edx
  div %ebx          ; divido %eax por %ebx y almaceno el resultado en %edx
  cmp $0, %edx      ; comparo si el resto de la división es cero
  je print_fizzbuzz ; si es cero, imprimo fizzbuzz
  mov $3, %ebx      ; cargo 3 en %ebx
  xor %edx, %edx    ; limpio el registro %edx
  div %ebx          ; divide %eax por %ebx y almaceno el resultado en %edx
  cmp $0, %edx      ; compruebo si el resto de la división es cero
  je print_fizz     ; si es cero, imprimo fizz
  mov $5, %ebx      ; cargo 5 en %ebx
  xor %edx, %edx    ; limpio el registro %edx
  div %ebx          ; divide %eax por %ebx y almaceno el resultado en %edx
  cmp $0, %edx      ; comparo si el resto de la división es cero
  je print_buzz     ; si es cero, imprimo buzz
  print_int %eax    ; imprime el valor de %eax
  jmp incrementar_contador  ; salta a incrementar_contador

print_fizz:
  print_string fizz         ; imprime "fizz"
  jmp incrementar_contador  ; salta a incrementar_contador

print_buzz:
  print_string buzz         ; imprime "buzz"
  jmp incrementar_contador  ; salta a incrementar_contador


incrementar_contador:
  inc %eax                  ; incrementa %eax en uno
  jmp buclePrincipal       ; vuelve al inicio del ciclo

end_loop:
  ret            ; fin
