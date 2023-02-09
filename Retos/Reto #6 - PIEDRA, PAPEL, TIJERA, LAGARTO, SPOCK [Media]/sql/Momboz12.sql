/*
 * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
 *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
 * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
 */

 
-- O - Piedra
-- P - Papel
-- T - Tijera
-- L - Lagarto
-- S - Spock

CREATE TABLE #Valores
(
	Player1 CHAR(1),
	Player2 CHAR(1)
)
INSERT INTO #Valores (Player1, Player2) 
VALUES ('O','T'),
	   ('T','O'),
	   ('P','T')


DECLARE @Player1 CHAR(1), @Player2 CHAR(1), @Resultado CHAR(2)

DECLARE _Cursor CURSOR
READ_ONLY
FOR 

SELECT Player1, player2 FROM #Valores

OPEN _Cursor

FETCH NEXT FROM _Cursor INTO @Player1, @Player2
WHILE (@@fetch_status <> -1)
BEGIN
	IF (@@fetch_status <> -2)
	BEGIN
		IF @Player1 = @Player2
		BEGIN
			PRINT 'Empate'
		END
		ELSE
		BEGIN
				IF ((@Player1 = 'O' AND (@Player2 = 'T' OR @Player2 = 'L'))
					OR (@Player1 = 'P' AND (@Player2 = 'O' OR @Player2 = 'S'))
					OR (@Player1 = 'T' AND (@Player2 = 'L' OR @Player2 = 'P'))
					OR (@Player1 = 'L' AND (@Player2 = 'S' OR @Player2 = 'P'))
					OR (@Player1 = 'S' AND (@Player2 = 'O' OR @Player2 = 'T'))			
					)
				BEGIN
					SET @Resultado = 'P1'
				END
				ELSE
				IF ((@Player2 = 'O' AND (@Player1 = 'T' OR @Player1 = 'L'))
					OR (@Player2 = 'P' AND (@Player1 = 'O' OR @Player1 = 'S'))
					OR (@Player2 = 'T' AND (@Player1 = 'L' OR @Player1 = 'P'))
					OR (@Player2 = 'L' AND (@Player1 = 'S' OR @Player1 = 'P'))
					OR (@Player2 = 'S' AND (@Player1 = 'O' OR @Player1 = 'T'))	
					)
				BEGIN
					SET @Resultado = 'P2'
				END

			IF @Resultado = 'P1'
			BEGIN
				PRINT 'Ganador player 1'
			END
			ELSE
			BEGIN
				PRINT 'Ganador player 2'
			END
		END
	END
	FETCH NEXT FROM _Cursor INTO @Player1, @Player2
END

CLOSE _Cursor
DEALLOCATE _Cursor
DROP TABLE #Valores
