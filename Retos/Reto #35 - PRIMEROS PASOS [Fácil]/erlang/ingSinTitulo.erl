% Punto 1: Hola, mundo!
io:format("Hola, mundo!~n").

% Punto 2: Crea una variable de texto o string
MiTexto = "¡Hola desde Erlang!".

% Punto 3: Crea una variable de número entero
MiEntero = 42.

% Punto 4: Crea una variable de número con decimales (en Erlang, solo enteros o fracciones)
MiDecimal = 3.14.

% Punto 5: Crea una variable de tipo booleano (en Erlang, los átomos se usan para representar booleanos)
MiBooleano = true.

% Punto 6: Crea una constante (en Erlang, no hay constantes en el sentido tradicional)

% Punto 7: Usa un if, else if y else
if MiEntero > 50 ->
    io:format("El número es mayor que 50~n");
  MiEntero < 50 ->
    io:format("El número es menor que 50~n");
  true ->
    io:format("El número es igual a 50~n")
end.

% Punto 8: Crea un Array (no es común en Erlang, se trabaja con listas)
MiLista = [1, 2, 3, 4, 5].

% Punto 9: Crea una lista
MiListaTexto = ["Manzana", "Banana", "Naranja"].

% Punto 10: Crea una tupla
% Las tuplas en Erlang se definen directamente en su contexto de uso, no como variables independientes

% Punto 11: Crea un set (no aplicable en Erlang)

% Punto 12: Crea un diccionario (no aplicable en Erlang)

% Punto 13: Usa un ciclo for (no es común en Erlang, se prefieren funciones recursivas)
% Punto 14: Usa un ciclo foreach (no es común en Erlang, se prefieren funciones recursivas)

% Punto 15: Usa un ciclo while (no es común en Erlang, se prefieren funciones recursivas)

% Punto 16: Crea una función sin parámetros que no retorne nada
funcion_sin_parametros() ->
    io:format("Función sin parámetros~n").

% Punto 17: Crea una función con parámetros que no retorne nada
funcion_con_parametros(Param1, Param2) ->
    io:format("Parámetro 1: ~p~n", [Param1]),
    io:format("Parámetro 2: ~p~n", [Param2]).

% Punto 18: Crea una función con parámetros que retorne valor
funcion_con_retorno(A, B) ->
    A + B.

% Punto 19: Crea una clase (no aplicable en Erlang, se trabaja con funciones y módulos)

% Punto 20: Muestra control de excepciones (try-catch en Erlang)
try
    Resultado = MiEntero / 0,
    io:format("~p~n", [Resultado])
catch
    _:Error ->
        io:format("Error: ~p~n", [Error])
end.
