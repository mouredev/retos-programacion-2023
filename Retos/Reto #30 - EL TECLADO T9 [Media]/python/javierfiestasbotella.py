def teclado_t9():
    letra=''
    palabra=''
    t9={'a':2,'b':22,'c':222,'d':3,'e':33,'f':333,'g':4,'h':44,'i':444,'j':5,'k':55,'l':555,'m':6,'n':66,'o':666,'p':7,'q':77,'r':777,'s':7777,'t':8,'u':88,'v':888,'w':9,'x':99,'y':999,'z':9999}
    teclas=input('Teclea separando con un guion: ')
    for i in teclas:
        if i!='-' or i==teclas[-1]:
            letra+=i
        else:
            for clave,valor in t9.items():
                if valor==int(letra):
                  palabra+=clave.upper() 
            letra='' 
    for clave, valor in t9.items():
        if valor == int(letra):
            palabra += clave.upper()
    return palabra


