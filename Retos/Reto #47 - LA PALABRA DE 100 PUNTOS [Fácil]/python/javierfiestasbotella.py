'''
Crea un programa que calcule los puntos de una palabra.
 * - Cada letra tiene un valor asignado. Por ejemplo, en el abecedario
 *   español de 27 letras, la A vale 1 y la Z 27.
 * - El programa muestra el valor de los puntos de cada palabra introducida.
 * - El programa finaliza si logras introducir una palabra de 100 puntos.
 * - Puedes usar la terminal para interactuar con el usuario y solicitarle
 *   cada palabra.'''

abc='a,b,c,d,e,f,g,h,i,j,k,l,m,n,ñ,o,p,q,r,s,t,u,v,w,x,y,z'
abc=abc.split(',')
abc_valores=dict()
valor=[n for n in range(1,28)]
for i in range(27):
    abc_valores[abc[i]]=valor[i]

acierto=0
while True:
    question=input('Introduce una palabra con valor 100: ')
    for i in question:
        acierto+=abc_valores[i] 
    if acierto<100:
        print(f'La palabra {question} tiene un valor de {acierto}. te has quedado corto, inténtalo de nuevo.')
    elif acierto > 100:
        print(f'La palabra {question} tiene un valor de {acierto}, te has pasado, inténtalo de nuevo') 
    elif acierto==100:
        break
    acierto=0        
print(f'¡¡¡Enhorabuena la palabra {question} tiene un valor de 100!!!')   