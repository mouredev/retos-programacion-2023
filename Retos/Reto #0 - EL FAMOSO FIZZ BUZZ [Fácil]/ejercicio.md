# Reto #0: EL FAMOSO "FIZZ BUZZ"
#### Dificultad: Fácil | Publicación: 26/12/22 | Corrección: 02/01/23

## Enunciado

```
/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */
```
#### Tienes toda la información extendida sobre los retos de programación semanales en **[retosdeprogramacion.com/semanales2023](https://retosdeprogramacion.com/semanales2023)**.

Sigue las **[instrucciones](../../README.md)**, consulta las correcciones y aporta la tuya propia utilizando el lenguaje de programación que quieras.

> Recuerda que cada semana se publica un nuevo ejercicio y se corrige el de la semana anterior en directo desde **[Twitch](https://twitch.tv/mouredev)**. Tienes el horario en la sección "eventos" del servidor de **[Discord](https://discord.gg/mouredev)**.



<!DOCTYPE html>
<html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>EL FAMOSO "FIZZ BUZZ”</title>
    </head>
    <body>
        <script>
            
            function multiplos(valor, multi) {

                var respuesta = valor % multi;

                if (respuesta == 0) { 

                    return true;

                } 
                else {
                    
                    return false;
                    
                }
            }

            function multiple() {

                var num = 100;
                    
                for ( i = 0; i <= 100; i++) {
                       
                    var multi3 = multiplos (i, 3);
                    var multi5 = multiplos (i, 5);


                    if (  multi3 && multi5 ) {

                        console.log(i, "fizzbuzz");

                    } 
                    else {

                        if (multi3) {

                            console.log(i, "fizz");
                                    
                        } else {

                            if (multi5) {

                                console.log(i, "buzz");

                            } else {
                                            
                                console.log(i);

                            }
                        }       
                    }
                }         
            } 
               
        </script>                 
    </body>  
</html>
