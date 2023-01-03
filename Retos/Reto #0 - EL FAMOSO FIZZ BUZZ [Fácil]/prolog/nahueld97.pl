
/*
 * Para ejecurtar sin instalar nada se puede usar el siguiente link 
 * del compilador online de SWI:
 * 
 * https://swish.swi-prolog.org/p/Reto0.pl
 * 
 * o https://swish.swi-prolog.org/ copiando y pegando el codigo
 *
 * para ejecutarlo solo realiza la consulta
 * 		?-print.
 * 
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */

/*
 * X es multiplo de Y
 */
multiplo_de(X,Y) :- 
	X mod Y =:= 0.

print :-
    print(1,100).

/*
 * Imprime de X a Y
 **/
print(X,Y) :-
    X =< Y,
    show(X),
    X1 is X + 1,
    print(X1, Y).

/*
 * muestra los numeros conforme las condiciones dadas.
 * */

show(X):-
   	multiplo_de(X,3),
    \+ multiplo_de(X,5),
   	writeln("fizz"),!.

show(X):-
   	multiplo_de(X,5),
    \+ multiplo_de(X,3),
   	writeln("buzz"),!.

show(X):-
   	multiplo_de(X,3),
    multiplo_de(X,5),
   	writeln("fizzbuzz"),!.

/*Caso por defecto*/
show(X):-
   	writeln(X),!.
