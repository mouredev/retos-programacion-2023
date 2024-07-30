module Fran_cio where

-- ```
-- /*
--  * Crea 3 funciones, cada una encargada de detectar si una cadena de
--  * texto es un heterograma, un isograma o un pangrama.
--  * - Debes buscar la definición de cada uno de estos términos.
--  */
-- ```

-- Un heterograma (del griego héteros, 'diferente' y gramma, 'letra') es una palabra o frase que no contiene ninguna letra repetida.
-- Un isograma (del griego isos, 'igual' y gramma, 'letra') es una palabra o frase en la que cada letra aparece el mismo número de veces.
-- Los pangramas son textos en los que debe aparecer todas las letras del abecedario
countElemWrap :: (Eq t1, Num t2) => t1 -> [t1] -> t2
countElemWrap elem arr =
  countElem elem arr 0
  where
    countElem elem [] accum = accum
    countElem elem (x:xs) accum = if elem == x
                                    then countElem elem xs (accum+1)
                                    else countElem elem xs accum

isHeterograma palabra = all ((== 1) . (`countElemWrap` palabra)) palabra
isIsograma palabra = all ((==countElemWrap (head palabra) palabra) . (`countElemWrap` palabra)) palabra
isPanagrama palabra = all ((== True) . (`elem` palabra)) ['a' .. 'z']

message :: [Char] -> String
message palabra = show palabra
  <> (if isHeterograma palabra then " " else " no ") <> "es Heterograma,"
  <> (if isIsograma palabra then " " else " no ") <> "es Isograma, y"
  <> (if isPanagrama palabra then " " else " no ") <> "es Panagrama."

palabras = ["flamenco", "backdrop", "crumpled", "discord", "jumps", 
  "dermatoglyphics", "subdermatoglyphic", "nonsecretory",
  "uncopyrightable", "hydropneumatics",
  "aaddbb","llyypp",
  "the quick brown fox jumps over a lazy dog.",
 "pack my box with five dozen liquor jugs.",
 "jackdaws love my big sphinx of quartz.",
 "the five boxing wizards jump quickly.",
 "how vexingly quick daft zebras jump!"]

main :: IO ()
main = mapM_ (putStrLn . message ) palabras
