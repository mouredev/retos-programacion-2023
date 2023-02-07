/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

CREATE FUNCTION dbo.fnPrimoFibonacciParImpar(@ValorSolicitado BIGINT)
RETURNS VARCHAR(1000)
AS
BEGIN
	DECLARE @Valor0 BIGINT = 0, 
		@Valor1 BIGINT = 1, 
		@Resultado BIGINT = 1, 
		@fibonacci BIT = 0,
		@par_impar BIT = 0,
		@primo BIT = 1

	--INICIO SECCION FIBONACCI
	WHILE @ValorSolicitado >= @Resultado
	BEGIN
		IF @ValorSolicitado IN (0,1)
		BEGIN
			SET @fibonacci = 1
		END
		SET @Resultado = @Valor0 + @Valor1
		SET @Valor1 = @Valor0
		SET @Valor0 = @Resultado
		IF @Resultado = @ValorSolicitado
		BEGIN
			SET @fibonacci = 1
		END
	END
	--INICIO SECCION FIBONACCI

--INICIO SECCION PAR-IMPAR
	IF (@ValorSolicitado % 2) = 1
	BEGIN 
		SET @par_impar = 0
	END 
	ELSE
	BEGIN
		SET @par_impar = 1
	END
	--INICIO SECCION PAR-IMPAR

	--INICIO SECCION PRIMO
	DECLARE @i INT = 2
	IF @ValorSolicitado > 2 AND (@ValorSolicitado % 2) = 0
	BEGIN
		SET @primo = 0
	END
	ELSE
	BEGIN
		WHILE @i <= @ValorSolicitado
		BEGIN
			SET @i = @i + 1
			IF ((@ValorSolicitado % @i )= 0) AND (@i <> @ValorSolicitado)
			BEGIN
				SET @primo = 0
				BREAK
			END
		END
	END
	--INICIO SECCION PRIMO


	
	RETURN  CONCAT(@ValorSolicitado, CASE WHEN @fibonacci = 1 THEN ' es fibonacci' ELSE ' no es fibonacci' END, 
			', ', 
			CASE WHEN @par_impar = 0 THEN 'es impar' ELSE 'es par' END, 
			CASE WHEN @primo = 0 THEN ' y no es primo' ELSE ' y es primo' END)
END

SELECT  dbo.fnPrimoFibonacciParImpar(34) AS Resultado