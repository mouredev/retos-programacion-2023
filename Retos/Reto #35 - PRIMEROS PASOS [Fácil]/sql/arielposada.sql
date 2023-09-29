-- SQL
-- Hola mundo
PRINT 'Hola Mundo!';

-- Variables
DECLARE @myVariable NVARCHAR(255);
SET @myVariable = 'Esto es una variable';
SET @myVariable = 'Aquí asigno un nuevo valor a la variable';

-- Tipos de datos primitivos
DECLARE @myString NVARCHAR(255) = 'Mi cadena de texto';
DECLARE @myInt INT = 1;
DECLARE @myFloat FLOAT = 1.5;
DECLARE @myBool BIT = 1; -- 1 para True, 0 para False

-- Constantes
-- SQL no tiene una forma nativa de definir constantes. Sin embargo, puedes usar variables y simplemente no modificarlas.

-- Control de flujo
IF @myInt = 1
    PRINT 'myInt vale 1';
ELSE IF @myInt = 2
    PRINT 'myInt vale 2';
ELSE
    PRINT 'myInt no vale ni 1 ni 2';

-- Estructuras
-- SQL no tiene listas o arrays nativos. En su lugar se usan tablas o tablas temporales.
CREATE TABLE #myList (value NVARCHAR(255));
INSERT INTO #myList 
VALUES (@myString), 
    (CAST(@myInt AS NVARCHAR(255))), 
    (CAST(@myFloat AS NVARCHAR(255))), 
    (CAST(@myBool AS NVARCHAR(255)));

-- Bucles usando un cursor (equivalentes a ciclo for)
DECLARE @item NVARCHAR(255);
DECLARE myListCursor CURSOR FOR 
SELECT value FROM #myList;

OPEN myListCursor;
FETCH NEXT FROM myListCursor INTO @item;

WHILE @@FETCH_STATUS = 0
BEGIN
    PRINT @item;
    FETCH NEXT FROM myListCursor INTO @item;
END;

-- Cerrar y limpiar el cursor
CLOSE myListCursor;
DEALLOCATE myListCursor;

-- Funciones
CREATE FUNCTION myFunctionWithReturn()
RETURNS NVARCHAR(255)
AS
BEGIN
    RETURN 'Función con retorno';
END;

-- Procedimientos
CREATE PROCEDURE myFunctionWithParam @param INT
AS
BEGIN
    PRINT 'Función con un parámetro de valor ' + CAST(@param AS NVARCHAR(255));
END;

EXEC myFunctionWithParam 256;

-- Excepciones
BEGIN TRY
    PRINT 0 / 0;
END TRY
BEGIN CATCH
    PRINT 'Se ha producido una excepción';
END CATCH;

PRINT 'Siempre se ejecuta el finally';

-- Limpieza
DROP TABLE #myList;
DROP FUNCTION myFunctionWithReturn;
DROP PROCEDURE myFunctionWithParam;
