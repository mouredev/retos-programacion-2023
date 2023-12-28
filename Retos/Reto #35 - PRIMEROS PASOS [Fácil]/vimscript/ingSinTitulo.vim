" Punto 1: Hola, mundo!
echo "Hola, mundo!"

" Punto 2: Crea una variable de texto o string
let mi_texto = "¡Hola desde Vimscript!"

" Punto 3: Crea una variable de número entero
let mi_entero = 42

" Punto 4: Crea una variable de número con decimales
let mi_decimal = 3.14

" Punto 5: Crea una variable de tipo booleano
let mi_booleano = 1 " 1 para verdadero, 0 para falso

" Punto 6: Crea una constante (no aplicable en Vimscript)

" Punto 7: Usa un if, else if y else
if mi_entero > 50
    echo "El número es mayor que 50"
elseif mi_entero < 50
    echo "El número es menor que 50"
else
    echo "El número es igual a 50"
endif

" Punto 8: Crea un Array (lista en Vimscript)
let mi_array = [1, 2, 3, 4, 5]

" Punto 9: Crea una lista (no aplicable en Vimscript)

" Punto 10: Crea una tupla (no aplicable en Vimscript)

" Punto 11: Crea un set (no aplicable en Vimscript)

" Punto 12: Crea un diccionario (Dictionary en Vimscript)
let mi_diccionario = {'clave1': 'valor1', 'clave2': 'valor2'}

" Punto 13: Usa un ciclo for (bucle for)
for elemento in mi_array
    echo elemento
endfor

" Punto 14: Usa un ciclo foreach (no aplicable en Vimscript)

" Punto 15: Usa un ciclo while
let contador = 0
while contador < 3
    echo "Contador: " . contador
    let contador += 1
endwhile

" Punto 16: Crea una función sin parámetros que no retorne nada
function! funcion_sin_parametros()
    echo "Función sin parámetros"
endfunction
call funcion_sin_parametros()

" Punto 17: Crea una función con parámetros que no retorne nada
function! funcion_con_parametros(param1, param2)
    echo "Parámetro 1: " . a:param1
    echo "Parámetro 2: " . a:param2
endfunction
call funcion_con_parametros(1, "dos")

" Punto 18: Crea una función con parámetros que retorne valor
function! funcion_con_retorno(a, b)
    return a:a + a:b
endfunction
let resultado = call funcion_con_retorno(3, 4)
echo "Resultado: " . resultado

" Punto 19: Crea una clase (no hay clases en Vimscript)

" Punto 20: Muestra control de excepciones (no hay manejo de excepciones en Vimscript)
