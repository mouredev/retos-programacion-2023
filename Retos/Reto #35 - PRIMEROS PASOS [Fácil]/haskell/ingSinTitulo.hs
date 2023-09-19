-- Punto 1: Hola, mundo!
main :: IO ()
main = putStrLn "Hola, mundo!"

-- Punto 2: Crea una variable de texto o string
miTexto :: String
miTexto = "¡Hola desde Haskell!"

-- Punto 3: Crea una variable de número entero
miEntero :: Int
miEntero = 42

-- Punto 4: Crea una variable de número con decimales
miDecimal :: Double
miDecimal = 3.14

-- Punto 5: Crea una variable de tipo booleano
miBooleano :: Bool
miBooleano = True

-- Punto 6: Crea una constante
miConstante :: Int
miConstante = 10

-- Punto 7: Usa un if, else if y else
ejemploIf :: Int -> String
ejemploIf x
  | x > 50 = "El número es mayor que 50"
  | x < 50 = "El número es menor que 50"
  | otherwise = "El número es igual a 50"

-- Punto 8: Crea un Array (lista en Haskell)
miArray :: [Int]
miArray = [1, 2, 3, 4, 5]

-- Punto 9: Crea una lista
miLista :: [String]
miLista = ["Manzana", "Banana", "Naranja"]

-- Punto 10: Crea una tupla
-- Las tuplas en Haskell se definen directamente en su contexto de uso, no como variables independientes

-- Punto 11: Crea un set (no aplicable en Haskell)

-- Punto 12: Crea un diccionario (no aplicable en Haskell)

-- Punto 13: Usa un ciclo for (no es común en Haskell, se utilizan funciones de alto orden)
-- Punto 14: Usa un ciclo foreach (no es común en Haskell, se utilizan funciones de alto orden)

-- Punto 15: Usa un ciclo while (no es común en Haskell, se utilizan funciones recursivas)

-- Punto 16: Crea una función sin parámetros que no retorne nada
funcionSinParametros :: IO ()
funcionSinParametros = putStrLn "Función sin parámetros"

-- Punto 17: Crea una función con parámetros que no retorne nada
funcionConParametros :: Int -> String -> IO ()
funcionConParametros param1 param2 = do
  putStrLn $ "Parámetro 1: " ++ show param1
  putStrLn $ "Parámetro 2: " ++ param2

-- Punto 18: Crea una función con parámetros que retorne valor
funcionConRetorno :: Int -> Int -> Int
funcionConRetorno a b = a + b

-- Punto 19: Crea una clase (no aplicable en Haskell)

-- Punto 20: Muestra control de excepciones (no es común en Haskell, se utilizan tipos de datos como Maybe o Either)
