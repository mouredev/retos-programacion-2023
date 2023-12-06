def cifrado(letra:str, fase):
    if len(letra) == 1:
        codigo_org = ord(letra) 
        if codigo_org>= 65 and codigo_org<=90:
            codigo_enc = tranformar(codigo_org, 65, 90, fase)
        elif codigo_org>= 97 and codigo_org<=122:
            codigo_enc = tranformar(codigo_org, 97, 122, fase)
        elif codigo_org>= 192 and codigo_org<=255:
            codigo_enc = tranformar(codigo_org, 192, 255, fase)
        else:
            codigo_enc = codigo_org
    else:
        print("cifre de una letar por vez")
        return False
    return chr(codigo_enc)

def tranformar(codigo, desde, hasta, fase):
    if (codigo >= desde and codigo <= hasta and fase > 0):
        codigo = codigo + fase
        if (codigo > hasta):
            codigo = codigo - ((hasta - desde) + 1)
    if (codigo >= desde and codigo <= hasta and fase < 0):
        codigo = codigo + fase
        if (codigo < desde):
             codigo = codigo + ((hasta - desde) + 1)
    return codigo

def encriptar(texto: str, fase:int = 7):
    if fase >=1 and fase <=25:
        encriptado =""
        for letra in texto:
            encriptado = encriptado + cifrado(letra, fase)
        return encriptado
    else:
        print("la fase debe ser entre 1 y 25")        
        return False

def desencriptar(texto: str, fase:int = 7):
    if fase >=1 and fase <=25:
        encriptado =""
        for letra in texto:
            encriptado = encriptado + cifrado(letra, -fase)
        return encriptado
    else:
        print("la fase debe ser entre 1 y 25")        
        return False
    

if __name__ == "__main__":
    # prueba
    for i in range(65,255):
        print(i, chr(i), cifrado(chr(i), 4), cifrado(cifrado(chr(i), 4),-4))


    #prueba 2
    a = encriptar("federico coronado",10)
    b = desencriptar(a,10)
    print(a)
    print(b)

    a = encriptar("* Crea un programa que realize el cifrado César de un texto y lo imprima. * También debe ser capaz de descifrarlo cuando así se lo indiquemos. * * Te recomiendo que busques información para conocer en profundidad cómo * realizar el cifrado. Esto también forma parte del reto.",10)
    b = desencriptar(a,10)
    print(a)
    print(b)
