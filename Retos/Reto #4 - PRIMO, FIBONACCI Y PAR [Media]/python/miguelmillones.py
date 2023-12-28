# Reto #4: PRIMO, FIBONACCI Y PAR #### Dificultad: Media | Publicación: 23/01/23 | Corrección: 30/01/23
## Enunciado
## Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
## * Ejemplos:
## * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
## * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"

N=-1
SERIE=[]

def par():
    div=N%2
    if div==0:
        resp2='par'
    else:
        resp2='impar'
    return resp2

def fibo():
    fib=[0,1]
    n=2
    if (N==0 or N==1):
        resp1='es'
    else:
        while n>1:
            f_n=fib[n-1]+fib[n-2]
            if f_n<N:
                fib.append(f_n)
                n=n+1
            elif f_n>N:
                resp1='no es'
                n=1
            else:
                resp1='es'
                n=1
    return resp1

def primo():
    count=0
    if N>1:
        for i in SERIE:
            r=N%i
            if r==0:
                count+=1
    else:
        resp='no es'
    if count>2 or count==0:
        resp='no es'
    else:
        resp='es'
    return resp


while not (N>-1):
    N=int(input("Enter the number: "))
SERIE=list(range(1,N+1))
RES_P=primo()
RES_F=fibo()
RES_I=par()

print(f'El {N} {RES_P} primo, {RES_F} fibonacci y es {RES_I}.')
