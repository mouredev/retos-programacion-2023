SECTION .DATA
    hello:     db '!Hola mundo!',10
    helloLen:  equ $-hello

SECTION .TEXT
    GLOBAL _start

_start:
    mov eax,4            ; 'write' system call = 4
    mov ebx,1            ; file descriptor 1 = STDOUT
    mov ecx,hello        ; string to write
    mov edx,helloLen     ; length of string to write
    int 80h              ; call the kernel

    mov eax,1            ; 'exit' system call
    mov ebx,0            ; exit with error code 0
    int 80h              ; call the kernel