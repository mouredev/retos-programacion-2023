module Fran_cio where
-- ```
-- /*
--  * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
--  * Ejemplos:
--  * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
--  * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
--  */
-- ```

isPrimo :: Integral t => t -> t -> Bool
isPrimo num accum 
  | accum == num = True
  | accum == 0 = isPrimo num 1
  | accum == 1 = isPrimo num 2
  | mod num accum == 0 = False
  | otherwise = isPrimo num (accum+1)

isFibo :: (Eq t, Num t, Num a, Ord a) => a -> t -> Bool
isFibo num accum
  | accum==0 = isFibo num 1
  | accum==1 = isFibo num 2
  | fib accum == num = True
  | fib accum > num = False
  | otherwise = isFibo num (accum+1)
  where
    fib 1 = 1
    fib 0 = 0
    fib n = fib (n-2) + fib (n-1)

message :: (Show a, Integral a) => a -> String
message num = show num
  <> (if isPrimo num 0 then " " else " no ") <> "es primo,"
  <> (if isFibo num 0 then " " else " no ") <> "es fibonacci, y"
  <> (if even num then " es par." else " es impar")

main :: IO ()
main =do
  mapM_ (putStrLn . message ) [0..100]

