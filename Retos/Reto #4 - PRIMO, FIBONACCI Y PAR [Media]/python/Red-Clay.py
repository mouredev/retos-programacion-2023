# /*
#  * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
#  * Ejemplos:
#  * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
#  * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
#  */

def es_primo(_input):
    y=True
    for x in range(2,_input):
        #print(f"{_input} % {x}")
        if _input % x == 0: y= False ;break
    return y

def fibonacci(num):
    a,b =0,1
    fibonacci_lista=[]
    for i in range(num+1):
        if b >= num: return b
        else:
            fibonacci_lista.append(b) 
            a,b=b,a+b
def ParImpar(num):
    y=False
    if num % 2 == 0:
        y=True
    return y
def main():
    try:
        _input=int(input("Ingrese un Numero: "))
    except:
       print("input incorrecto")

    Response=""
    Response+=(f"{str(_input)}")
    if  es_primo(_input):
        Response+=" es primo "
    if  not es_primo(_input):
        Response+=" es no primo "
    if _input==fibonacci(_input) :
        Response+=(f", fibonacci ")
    if _input!=fibonacci(_input) :
        Response+=(f",no es fibonacci ")
    if  ParImpar(_input):
        Response+="y es par "
    if  not ParImpar(_input):
        Response+="y es impar "
    print(Response)

main()
