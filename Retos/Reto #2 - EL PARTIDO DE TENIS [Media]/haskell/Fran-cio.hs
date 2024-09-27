module Fran_cio where
-- /*
--  * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
--  * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
--  * gane cada punto del juego.
--  * 
--  * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
--  * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
--  *   15 - Love
--  *   30 - Love
--  *   30 - 15
--  *   30 - 30
--  *   40 - 30
--  *   Deuce
--  *   Ventaja P1
--  *   Ha ganado el P1
--  * - Si quieres, puedes controlar errores en la entrada de datos.   
--  * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
--  */
data Puntaje = Love | D15 | D30 | D40 | Ventaja | Win deriving (Eq)
data Player = P1 | P2 deriving (Eq, Show)
type State = (Puntaje, Puntaje)

instance Show Puntaje where
  show Love = "Love"
  show D15 = "15"
  show D30 = "30"
  show D40 = "40"
  show Ventaja = "Advantage"
  show Win = "Win"

nextPuntaje :: Puntaje -> Puntaje
nextPuntaje Love = D15
nextPuntaje D15  = D30
nextPuntaje D30  = D40
nextPuntaje D40  = Win 
nextPuntaje Ventaja = Win
nextPuntaje Win = Win

nextState :: Player -> State -> State
nextState P1 (p1, p2) = case (p1, p2) of
    (D40, D40)         -> (Ventaja, D40)
    (_, Ventaja)       -> (D40, D40)
    (Ventaja, _)       -> (Win, p2)
    (Win, _)           -> (Win, p2)
    _                  -> (nextPuntaje p1, p2)
nextState P2 (p1, p2) = case (p1, p2) of
    (D40, D40)         -> (D40, Ventaja)
    (Ventaja, _)       -> (D40, D40)
    (_, Ventaja)       -> (D40, Win)
    (_, Win)           -> (p1, Win)
    _                  -> (p1, nextPuntaje p2)

-- Estado inicial para iniciar un partido
estadoInicial :: State
estadoInicial = (Love, Love)

printEstado :: State -> String
printEstado (Win,_) = "Gano P1" 
printEstado (_,Win) = "Gano P2" 
printEstado (Ventaja,_) = "Ventaja P1" 
printEstado (_,Ventaja) = "Ventaja P2" 
printEstado (D40,D40) = "Deuce" 
printEstado (p1,p2) = show p1 ++ " - " ++ show p2 

partido :: [Player] -> State -> IO()
partido _ (p1,Win) = do putStrLn (printEstado (p1,Win))
partido _ (Win,p2) = do putStrLn (printEstado (Win,p2))
partido [] state = do putStrLn (printEstado state)
partido (x:xs) state = do
  putStrLn (printEstado state)
  _ <- partido xs (nextState x state)
  return ()

main = partido [P1, P1, P2, P2, P2, P1, P2, P1, P1,P1] estadoInicial
