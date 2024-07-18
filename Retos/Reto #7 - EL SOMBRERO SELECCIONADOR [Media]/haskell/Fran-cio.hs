module Fran_cio where
-- ```
-- /*
--  * Crea un programa que simule el comportamiento del sombrero seleccionador del
--  * universo mágico de Harry Potter.
--  * - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
--  * - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
--  * - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
--  *   coloque al alumno en una de las 4 casas de Hogwarts (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
--  * - Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador.
--  *   Por ejemplo, en Slytherin se premia la ambición y la astucia.
--  */
-- ```

data Casa = Gryffindor | Ravenclaw | Hufflepuff | Slytherin deriving (Show, Eq)

preguntas :: [String]
preguntas =
  [ "¿Qué valoras más?\nA) Coraje\nB) Inteligencia\nC) Lealtad\nD) Ambición"
  , "¿Qué actividad prefieres?\nA) Aventura al aire libre\nB) Estudiar en la biblioteca\nC) Pasar tiempo con amigos\nD) Planear tu futuro"
  , "¿Cómo reaccionas ante un problema?\nA) Enfrentándolo de inmediato\nB) Pensando en una solución lógica\nC) Buscando ayuda de tus amigos\nD) Tratando de usarlo a tu favor"
  , "¿Cuál es tu prioridad en la vida?\nA) Ser valiente y honesto\nB) Ser sabio y aprender\nC) Ser justo y leal\nD) Ser exitoso y reconocido"
  , "¿Qué mascota preferirías tener?\nA) León\nB) Águila\nC) Tejón\nD) Serpiente"
  ]

puntuaciones :: Char -> (Int, Int, Int, Int)
puntuaciones 'A' = (1, 0, 0, 0)
puntuaciones 'B' = (0, 1, 0, 0)
puntuaciones 'C' = (0, 0, 1, 0)
puntuaciones 'D' = (0, 0, 0, 1)
puntuaciones _ = (0, 0, 0, 0)

main :: IO ()
main = do
  respuestas <- mapM hacerPregunta preguntas
  let casa = determinarCasa respuestas
  putStrLn $ "¡Felicidades! Perteneces a " ++ show casa

hacerPregunta :: String -> IO (Int, Int, Int, Int)
hacerPregunta pregunta = do
  putStrLn pregunta
  respuesta <- getLine
  return $ puntuaciones (head respuesta)

determinarCasa :: [(Int, Int, Int, Int)] -> Casa
determinarCasa respuestas =
  let (gTotal, rTotal, hTotal, sTotal) = foldr (\(g, r, h, s) (gt, rt, ht, st) -> (gt + g, rt + r, ht + h, st + s)) (0, 0, 0, 0) respuestas
  in case maximum [gTotal, rTotal, hTotal, sTotal] of
       g | g == gTotal -> Gryffindor
       r | r == rTotal -> Ravenclaw
       h | h == hTotal -> Hufflepuff
       s | s == sTotal -> Slytherin

