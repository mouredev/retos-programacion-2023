"""/*
 * La última semana de 2021 comenzamos la actividad de retos de programación,
 * con la intención de resolver un ejercicio cada semana para mejorar
 * nuestra lógica... ¡Hemos llegado al EJERCICIO 100! Gracias 🙌
 *
 * Crea un programa que calcule los puntos de una palabra.
 * - Cada letra tiene un valor asignado. Por ejemplo, en el abecedario
 *   español de 27 letras, la A vale 1 y la Z 27.
 * - El programa muestra el valor de los puntos de cada palabra introducida.
 * - El programa finaliza si logras introducir una palabra de 100 puntos.
 * - Puedes usar la terminal para interactuar con el usuario y solicitarle
 *   cada palabra.
 */"""

#word=str(input("Entre una palabra: "))
letter={}
cont=0
for i in range(ord('a'), ord('n')+1):
    cont+=1
    letter[chr(i)]=cont
letter["ñ"]=15
for l in range(ord('o'),ord('z')+1):
    cont+=1
    letter[chr(l)]=cont+1

while True:
        word=input("Introduce una palabra: ")
        if len(word.split()) > 1:
            print("Error: Por favor, introduce solo una palabra.")
            continue    
        sum=0
        for i in word.lower():
            sum+=letter.get(i)
        print(f'Lo siento, la palabra {word} tiene {sum} puntos.')
        if sum == 100:
            print(f"Felicidades, la palabra {word} tiene {sum} puntos")
            break