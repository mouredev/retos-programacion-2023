; hello-dos.asm 16-bit "hello world" program


    org  0x100        ; .com files always start 256 bytes into the segment

    mov  dx, msg      ; the address of or message in dx
    mov  ah, 9        ; ah=9 - "print string" sub-function
    int  0x21         ; call dos services

    mov  ah, 0x4c     ; "terminate program" sub-function
    int  0x21         ; call dos services

    msg  db 'Hola, Mundo!', 0x0d, 0x0a, '$'   ; $-terminated message