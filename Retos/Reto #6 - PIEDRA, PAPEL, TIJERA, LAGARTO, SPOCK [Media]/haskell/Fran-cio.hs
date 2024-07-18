module Fran_cio where
-- ```
-- /*
--  * Crea un programa que calcule quien gana más partidas al piedra,
--  * papel, tijera, lagarto, spock.
--  * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
--  * - La función recibe un listado que contiene pares, representando cada jugada.
--  * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
--  *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
--  * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
--  * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
--  */
-- ```

data Jugadas = Piedra | Papel | Tijera | Lagarto | Spock deriving (Eq, Show)

partida :: (Jugadas, Jugadas) -> [Char]
partida (p1 , p2)  
  | p1 == p2 = "Tie"
  | otherwise = case (p1, p2) of
      (Tijera, Papel) -> "Player 1"
      (Tijera, Lagarto) -> "Player 1"
      (Piedra, Tijera) -> "Player 1"
      (Piedra, Lagarto) -> "Player 1"
      (Lagarto, Spock) -> "Player 1"
      (Lagarto, Papel) -> "Player 1"
      (Spock, Tijera) -> "Player 1"
      (Spock, Piedra) -> "Player 1"
      (Papel, Spock) -> "Player 1"
      (Papel, Piedra) -> "Player 1"
      _ -> "Player 2"

main :: [Char]
main = partida (Tijera, Tijera)
