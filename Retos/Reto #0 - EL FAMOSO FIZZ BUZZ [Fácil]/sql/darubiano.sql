/*
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
Múltiplos de 3 por la palabra "fizz".
Múltiplos de 5 por la palabra "buzz".
Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz"
 */

-- BIGQUERY
SELECT CASE
    WHEN MOD(numeros,3) = 0 AND MOD(numeros,5) = 0 
    THEN "fizzbuzz"
    WHEN MOD(numeros,3) = 0
    THEN "fizz"
    WHEN MOD(numeros,5)= 0 
    THEN "buzz"
    ELSE CAST(numeros AS STRING)
    END AS result 
FROM UNNEST(GENERATE_ARRAY(1, 100)) AS numeros

-- POSTGRESQL
SELECT CASE
    WHEN MOD(numeros,3) = 0 AND MOD(numeros,5) = 0 
    THEN 'fizzbuzz'
    WHEN MOD(numeros,3) = 0
    THEN 'fizz'
    WHEN MOD(numeros,5)= 0 
    THEN 'buzz'
    ELSE CAST(numeros AS varchar)
    END AS result 
FROM GENERATE_SERIES(1, 100) AS numeros;