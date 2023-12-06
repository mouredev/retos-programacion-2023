module Main where

import Data.Time.Clock.POSIX ( getPOSIXTime )
import System.Timeout ( timeout )
import Control.Concurrent
import Text.Read (readMaybe)
import Data.Maybe
import System.IO


----


main :: IO ()
main = do

    hSetBuffering stdout NoBuffering  -- Corrige errores de salida a terminal al compilar con ghc
    hSetBuffering stdin LineBuffering -- Corrige errores de entrada al ejecutar con ghci

    putStrLn "--------------------------------------"
    putStrLn "¡Bienvenido a Adivinanzas matemáticas!"
    putStrLn "--------------------------------------"
    putStrLn $
        "Tendrás 3 segundos para responder correctamente el resultado de una operación matemática." ++
        "\n" ++
        "- Si lo consigues, se te presentará una nueva cuestión. Cada 5 aciertos aumentará en uno" ++
        " el posible número de cifras de un operando." ++
        "\n" ++
        "- Si no lo consigues, acabará el juego y se mostrará tu puntuación final."

    iniciar


----


iniciar :: IO ()
iniciar = do
    putStrLn "---"
    putStr "Cuando estés listo escribe 'y': "
    respuesta <- getLine
    if respuesta == "y"
        then comenzarJuego (1, 1) 0
        else do
            putStrLn "No hay prisa, ya sabes..."
            iniciar


----


comenzarJuego :: (Int, Int) -> Int -> IO ()
comenzarJuego longitud puntuacion = do

    semilla1 <- obtenerSemilla
    semilla2 <- obtenerSemilla
    semilla3 <- obtenerSemilla

    let opStr = operacionAleatoria semilla1
        op = strToOp opStr
        x = numeroAleatorio (semilla2 + 564851568) (fst longitud)
        y = if opStr /= "/" then numeroAleatorio (semilla3 + 3219781323) (snd longitud) else (numeroAleatorio (semilla3 + 98202238) (snd longitud)) + 1
        -- Controla la división entre 0

    putStr "\n"
    putStrLn "--------------------------------------"
    putStrLn $ "Pregunta " ++ show (puntuacion + 1)
    putStr "\n"
    putStr $ ">>> " ++ show x ++ opStr ++ show y ++ " = "

    maybeRespuesta <- timeout (3 * 10^6) getLine -- Máximo 3 segundos para responder
    let solucion = x `op` y

    case maybeRespuesta of
        Nothing -> incorrecto solucion                          -- El jugador no responde
        Just respuestaStr -> case readMaybe respuestaStr of     -- El jugador responde
            Nothing -> incorrecto solucion                      -- El jugador da una respuesta no válida
            Just respuestaInt ->                                -- La respuesta es válida
                if respuestaInt == solucion
                    then correcto longitud puntuacion           -- El jugador acierta
                    else incorrecto solucion                    -- El jugador falla

    where
        incorrecto :: Int -> IO ()
        incorrecto s = do
            putStr   "\n"
            putStrLn "--------------------------------------"
            putStrLn "¡Has fallado!"
            putStrLn $ "La respuesta correcta era: " ++ show s
            putStrLn $ "Tu puntuación final: " ++ show puntuacion
            putStrLn "--------------------------------------"

        correcto :: (Int, Int) -> Int -> IO ()
        correcto l p
            | (p `mod` 5) /= 0 || p == 0 = comenzarJuego longitud (puntuacion + 1)
            | otherwise = comenzarJuego (actualizar longitud) (puntuacion + 1)

        actualizar :: (Int, Int) -> (Int, Int)
        actualizar (l1, l2)
            | l1 == l2 = (l1 + 1, l2)
            | otherwise = (l1, l2 + 1)

        obtenerSemilla :: IO Int
        obtenerSemilla = round <$> getPOSIXTime


----


operaciones :: [String]
operaciones = ["+", "-", "*", "/"]


operacionAleatoria :: Int -> String
operacionAleatoria semilla = operaciones !! (semilla `mod` length operaciones)


strToOp :: String -> (Int -> Int -> Int)
strToOp "+" = (+)
strToOp "-" = (-)
strToOp "*" = (*)
strToOp "/" = div
strToOp _ = error "ERROR: Operador no reconocido"


----


numeroAleatorio :: Int -> Int -> Int
numeroAleatorio semilla longitud
    | longitud <= 0 = error "ERROR: La longitud de un número debe ser mayor que 0"
    | otherwise = semilla `mod` (limiteSuperior - limiteInferior + 1) + limiteInferior
    where
        limiteSuperior = 10 ^ longitud - 1
        limiteInferior = 0

