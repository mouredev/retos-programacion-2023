/*
 * # Reto #5: ¡Hola Mundo!
 * #### Dificultad: Fácil | Publicación: 30/01/23 | Corrección: 06/02/23
 *
 * ## Enunciado
 *
 * Escribe un !Hola Mundo! en todos los lenguajes de programación que puedas.
 * Seguro que hay algún lenguaje que te llama la atención y nunca has utilizado,
 * o quizás quieres dar tus primeros pasos... ¡Pues este es el momento!
 *
 * A ver quién se atreve con uno de esos lenguajes que no solemos ver por ahí...
 *
 * .....................................................................................................................
 *
 * Author: kyrex23
 * Date:   06/02/2023
 *
 * WARNING: This source is an alternative "hola mundo" for fun. Don't take it as a correct way of coding
 */

#include <stdio.h>

int main() {
    static int i = 0x10;
    putchar(*("\xa\x2a\x3c\x23\x25\x26\x75\x6b\x76\x7e\x77\x2b\x6d\x79\x7d\x77" + --i) - i);
    return i && main();
}
