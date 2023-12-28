'''
/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */

'''



def main() -> None:
    for number in range(101):
        if number % 3 == 0 and number % 5 == 0:
            print("fizzbuzz\n")
            continue;
        if number % 3 == 0:
            print("fizz\n")
            continue;
        if number % 5 == 0:
            print("buzz\n")
            continue;
        print(str(number) + '\n');
        
        
if __name__ == '__main__':
    main();