/*
 Escribe un programa que reciba un texto y transforme lenguaje natural a 'lenguaje hacker' (conocido realmente como "leet" o "1337").
 Este lenguaje se caracteriza por sustituir caracteres alfanuméricos.

 Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) con el alfabeto y los números en "leet".
 (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
*/

----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
-- POSTGRES --
CREATE OR REPLACE FUNCTION pg_temp.LenguajeHacker(texto TEXT)
RETURNS TABLE (result TEXT) 
LANGUAGE plpgsql 
AS $$
DECLARE resultado TEXT;
BEGIN
	RETURN QUERY
	WITH diccionario_hacker AS (
      SELECT * FROM (VALUES
         ('a', '4'),
         ('b', 'I3'),
         ('c', '['),
         ('d', ')'),
         ('e', '3'),
         ('f', '|='),
         ('g', '&'),
         ('h', '#'),
         ('i', '1'),
         ('j', ',_|'),
         ('k', '>|'),
         ('l', '1'),
         ('m', '/\\/\\'),
         ('n', '^/'),
         ('o', '0'),
         ('p', '|*'),
         ('q', '(_,)'),
         ('r', 'I2'),
         ('s', '5'),
         ('t', '7'),
         ('u', '(_)'),
         ('v', '\\/'),
         ('w', '\\\\/\\\\/'),
         ('x', '><'),
         ('y', 'j'),
         ('z', '2'),
         ('1', 'L'),
         ('2', 'R'),
         ('3', 'E'),
         ('4', 'A'),
         ('5', 'S'),
         ('6', 'b'),
         ('7', 'T'),
         ('8', 'B'),
         ('9', 'g'),
         ('0', 'o')
      ) AS dh(letra, traduccion)
   	)
	SELECT STRING_AGG(COALESCE(DH.traduccion, tabla.letra), '') AS resultado
	FROM (SELECT REGEXP_SPLIT_TO_TABLE(texto,'') AS letra) AS tabla
	LEFT JOIN diccionario_hacker AS DH
   	ON LOWER(tabla.letra) = DH.letra;
END
$$;

SELECT * FROM pg_temp.LenguajeHacker('Aquí está un texto de prueba para ver si funciona el reto!');

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
-- BIGQUERY --
CREATE TEMP FUNCTION LenguajeHacker(texto STRING) 
AS ((
   WITH diccionario_hacker AS (
    SELECT * FROM UNNEST([
      STRUCT('a' AS letra,'4' AS traduccion), 
      ('b', 'I3'),
      ('c', '['),
      ('d', ')'),
      ('e', '3'),
      ('f', '|='),
      ('g', '&'),
      ('h', '#'),
      ('i', '1'),
      ('j', ',_|'),
      ('k', '>|'),
      ('l', '1'),
      ('m', '/\\/\\'),
      ('n', '^/'),
      ('o', '0'),
      ('p', '|*'),
      ('q', '(_,)'),
      ('r', 'I2'),
      ('s', '5'),
      ('t', '7'),
      ('u', '(_)'),
      ('v', '\\/'),
      ('w', '\\\\/\\\\/'),
      ('x', '><'),
      ('y', 'j'),
      ('z', '2'),
      ('1', 'L'),
      ('2', 'R'),
      ('3', 'E'),
      ('4', 'A'),
      ('5', 'S'),
      ('6', 'b'),
      ('7', 'T'),
      ('8', 'B'),
      ('9', 'g'),
      ('0', 'o')
    ]))
    SELECT STRING_AGG(COALESCE(traduccion,letra),'') AS resultado
    FROM UNNEST(SPLIT(texto,'')) AS letra
    LEFT JOIN diccionario_hacker AS DH
    ON DH.letra = LOWER(letra)
));
-- LLamar funcion Hacker
SELECT LenguajeHacker("Aquí está un texto de prueba para ver si funciona el reto!") AS resultado