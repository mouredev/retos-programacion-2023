#import <Foundation/Foundation.h>

int main(int argc, const char * argv[]) {
    @autoreleasepool {
        // Punto 1: Hola, mundo!
        NSLog(@"Hola, mundo!");

        // Punto 2: Crea una variable de texto o string
        NSString *miTexto = @"¡Hola desde Objective-C!";

        // Punto 3: Crea una variable de número entero
        int miEntero = 42;

        // Punto 4: Crea una variable de número con decimales
        double miDecimal = 3.14;

        // Punto 5: Crea una variable de tipo booleano
        BOOL miBooleano = YES;

        // Punto 6: Crea una constante (no aplicable en Objective-C)

        // Punto 7: Usa un if, else if y else
        if (miEntero > 50) {
            NSLog(@"El número es mayor que 50");
        } else if (miEntero < 50) {
            NSLog(@"El número es menor que 50");
        } else {
            NSLog(@"El número es igual a 50");
        }

        // Punto 8: Crea un Array (NSArray en Objective-C)
        NSArray *miArray = @[@1, @2, @3, @4, @5];

        // Punto 9: Crea una lista (NSArray en Objective-C)
        NSArray *miLista = @[@"Manzana", @"Banana", @"Naranja"];

        // Punto 10: Crea una tupla (no aplicable en Objective-C)

        // Punto 11: Crea un set (NSSet en Objective-C)
        NSSet *miSet = [NSSet setWithObjects:@"Rojo", @"Verde", @"Azul", nil];

        // Punto 12: Crea un diccionario (NSDictionary en Objective-C)
        NSDictionary *miDiccionario = @{@"clave1": @"valor1", @"clave2": @"valor2"};

        // Punto 13: Usa un ciclo for
        for (NSNumber *elemento in miArray) {
            NSLog(@"%@", elemento);
        }

        // Punto 14: Usa un ciclo foreach (no aplicable en Objective-C)

        // Punto 15: Usa un ciclo while
        int contador = 0;
        while (contador < 3) {
            NSLog(@"Contador: %d", contador);
            contador++;
        }

        // Punto 16: Crea una función sin parámetros que no retorne nada
        void (^funcionSinParametros)(void) = ^{
            NSLog(@"Función sin parámetros");
        };
        funcionSinParametros();

        // Punto 17: Crea una función con parámetros que no retorne nada
        void (^funcionConParametros)(int, NSString*) = ^(int param1, NSString *param2) {
            NSLog(@"Parámetro 1: %d", param1);
            NSLog(@"Parámetro 2: %@", param2);
        };
        funcionConParametros(1, @"dos");

        // Punto 18: Crea una función con parámetros que retorne valor
        int (^funcionConRetorno)(int, int) = ^(int a, int b) {
            return a + b;
        };
        NSLog(@"Resultado: %d", funcionConRetorno(3, 4));

        // Punto 19: Crea una clase (no aplicable en Objective-C)

        // Punto 20: Muestra control de excepciones (no es común en Objective-C, se usa @try-@catch)
    }
    return 0;
}
