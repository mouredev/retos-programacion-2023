/*
 Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 Podrás configurar generar contraseñas con los siguientes parámetros:
 - Longitud: Entre 8 y 16.
 - Con o sin letras mayúsculas.
 - Con o sin números.
 - Con o sin símbolos.
 (Pudiendo combinar todos estos parámetros entre ellos)
*/
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
-- POSTGRES --
CREATE OR REPLACE FUNCTION pg_temp.GeneratePassword(mayuscula BOOL, num BOOL, carac BOOL, len INT)
RETURNS TABLE (result TEXT) 
LANGUAGE plpgsql 
AS $$
DECLARE resultado TEXT;
BEGIN
	RETURN QUERY
	WITH letras AS (
	  SELECT * FROM (VALUES
		 ('a'),('b'),('c'),('d'),('e'),('f'),('g'),('h'),('i'),
		 ('j'),('k'),('l'),('m'),('n'),('o'),('p'),('q'),('r'),
		 ('s'),('t'),('u'),('v'),('w'),('x'),('y'),('z')
	  ) AS dh(letra)
	),
	numeros AS (
	  SELECT * FROM (VALUES
		('0'),('1'),('2'),('3'),('4'),('5'),('6'),('7'),('8'),('9')
	  ) AS dh(numero)
	),
	caracteres AS (
	  SELECT * FROM (VALUES
		('!'),('#'),('$'),('%'),('&'),('/'),
		('('),(')'),('='),(','),('.'),('-'),
		('_'),('+'),('*'),(';'),(':'),('|')
	  ) AS dh(caracter)
	),
	seleccion AS (
		SELECT * FROM (
			SELECT CASE WHEN mayuscula THEN letra
			ELSE letra END AS letra
			FROM letras	
			UNION ALL
			SELECT * FROM numeros WHERE num
			UNION ALL
			SELECT * FROM caracteres WHERE carac
		) AS result 
		ORDER BY RANDOM() LIMIT 18
	)
	SELECT STRING_AGG(letra, '') AS contrasena
	FROM (
	  SELECT letra,ROW_NUMBER() OVER () AS row_num  
	  FROM seleccion
	) AS result
	WHERE row_num <=  CASE WHEN len<8 THEN 8 ELSE len END;
END
$$;
-- Llamar a la función GeneratePassword longitud minima 8 y maxima 18
SELECT * FROM pg_temp.GeneratePassword(TRUE, TRUE, TRUE, 10) AS contrasena;

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
-- BIGQUERY --
CREATE TEMP FUNCTION GeneratePassword(mayuscula BOOL, num BOOL, carac BOOL, len INT64) 
AS (
  (
    WITH letras AS (
      SELECT * FROM UNNEST([
          ('a'),('b'),('c'),('d'),('e'),('f'),('g'),('h'),('i'),
          ('j'),('k'),('l'),('m'),('n'),('o'),('p'),('q'),('r'),
          ('s'),('t'),('u'),('v'),('w'),('x'),('y'),('z')]) AS letra
    ),
    numeros AS (
      SELECT * FROM UNNEST([('0'),('1'),('2'),('3'),('4'),('5'),('6'),('7'),('8'),('9')]) AS numero
    ),
    caracteres AS (
      SELECT * FROM UNNEST([
        ('!'),('#'),('$'),('%'),('&'),('/'),
        ('('),(')'),('='),(','),('.'),('-'),
        ('_'),('+'),('*'),(';'),(':'),('|')]) AS caracter
    ),
    seleccion AS (
      SELECT * FROM (
        SELECT IF(mayuscula, UPPER(letras.letra), letras.letra) AS letra
        FROM letras
        UNION ALL
        SELECT * FROM numeros WHERE num
        UNION ALL
        SELECT * FROM caracteres WHERE carac
      ) ORDER BY RAND() LIMIT 18
    )
    SELECT STRING_AGG(letra, '') AS contrasena
    FROM (
      SELECT letra,ROW_NUMBER() OVER () AS row_num  
      FROM seleccion 
    )
     WHERE row_num <= IF(len<8, 8, len)
  )
);
-- Llamar a la función GeneratePassword longitud minima 8 y maxima 18
SELECT GeneratePassword(TRUE, TRUE, TRUE, 10) AS contrasena;



