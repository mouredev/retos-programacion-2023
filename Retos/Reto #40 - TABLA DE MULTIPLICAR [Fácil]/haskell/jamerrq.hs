import Text.Printf

-- Función que imprime la tabla de multiplicar de un número
-- Recibe un número entero
-- Devuelve una cadena con la tabla de multiplicar
-- Ejemplo (para n = 5):
-- 5 x 1 = 5
-- 5 x 2 = 10
-- 5 x 3 = 15
-- ...
-- 5 x 10 = 50
tablaMultiplicar :: Int -> String
tablaMultiplicar n = unlines [printf "%d x %d = %d" n i (n * i) | i <- [1..10]]

-- Función principal
main = do
    -- Pedimos el número
    putStrLn "Introduce un número:"
    numero <- getLine
    -- Imprimimos la tabla de multiplicar
    putStrLn $ tablaMultiplicar $ read numero

-- Cómo compilar y ejecutar:
-- $ ghc jamerrq.hs -o reto40hs
-- $ ./reto40hs
