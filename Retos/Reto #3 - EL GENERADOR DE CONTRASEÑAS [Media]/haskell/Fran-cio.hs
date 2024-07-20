module Fran_cio where
import System.Random (randomRIO)
import Text.Read (readMaybe)

-- /*
--  * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
--  * Podrás configurar generar contraseñas con los siguientes parámetros:
--  * - Longitud: Entre 8 y 16.
--  * - Con o sin letras mayúsculas.
--  * - Con o sin números.
--  * - Con o sin símbolos.
--  * (Pudiendo combinar todos estos parámetros entre ellos)
--  */

passwordLenght :: IO Int
passwordLenght = do
  putStrLn "What is the password length? (Between 8 and 16 characters)"
  length <- getLine
  if readMaybe length >= Just 8 && readMaybe length <= Just 16 then return (read length :: Int) else passwordLenght

yesOrNo :: IO Bool
yesOrNo = do
  putStrLn "Yes or No"
  decision <- getLine 
  if decision == "Yes" then return ( True :: Bool)
    else if decision == "No" then return ( False :: Bool)
      else yesOrNo


minus :: [Char]
minus = ['a'..'z']
capitals :: [Char]
capitals = ['A'..'Z']
numbers :: [Char]
numbers = ['1'..'9']
symbols :: [Char]
symbols = ['!'..'/']

genPassword :: Int -> [Char] -> [Char] -> IO [Char]
genPassword len dic accum
  | len == length accum = return accum
  | otherwise = do
     char <- randomRIO (0, length dic - 1) :: IO Int
     genPassword len dic (accum <> [dic !! char] )

getDic :: Bool -> Bool -> Bool -> [Char]
getDic capitalsCond numbersCond symbolsCond = minus <> 
  (if capitalsCond then capitals else []) <>
  (if numbersCond then numbers else []) <>
  (if symbolsCond then symbols else []) 


main :: IO String
main = do
  putStrLn "Hello, welcome to mouredev random password generator made by FranCio"
  putStrLn "Please tell me your preferences"
  len <- passwordLenght
  putStrLn "The passworld would have capital letters?"
  capitalsCond <- yesOrNo
  putStrLn "The passworld would have numbers?"
  numbersCond <- yesOrNo
  putStrLn "The passworld would have symbols?"
  symbolsCond <- yesOrNo
  let dic = getDic capitalsCond numbersCond symbolsCond
  putStrLn dic
  genPassword len dic []


