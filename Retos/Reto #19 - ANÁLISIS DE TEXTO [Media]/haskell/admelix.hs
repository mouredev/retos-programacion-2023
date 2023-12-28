import Data.List (maximumBy)
import Data.Char (isAlpha, isSpace)
import Data.Ord (comparing)

analyzeText :: String -> (Int, Double, Int, String)
analyzeText text =
  let (wordCount, totalLength, sentenceCount, longestWord) = analyzeTextHelper text 0 0 0 0 0 "" "" 0
      averageLength = fromIntegral totalLength / fromIntegral wordCount
  in (wordCount, averageLength, sentenceCount, longestWord)

analyzeTextHelper :: String -> Int -> Int -> Int -> Int -> Int -> String -> String -> Int -> (Int, Int, Int, String)
analyzeTextHelper [] wordCount totalLength sentenceCount longestLength currentLength currentWord longestWord =
  (wordCount, totalLength, sentenceCount, longestWord)
analyzeTextHelper (c:cs) wordCount totalLength sentenceCount longestLength currentLength currentWord longestWord
  | isAlpha c =
      analyzeTextHelper cs wordCount totalLength sentenceCount longestLength (currentLength + 1) (currentWord ++ [c]) longestWord
  | isSpace c =
      let newWordCount = if currentLength > 0 then wordCount + 1 else wordCount
          newTotalLength = totalLength + currentLength
          newLongestLength = if currentLength > longestLength then currentLength else longestLength
          newLongestWord = if currentLength > longestLength then currentWord else longestWord
      in analyzeTextHelper cs newWordCount newTotalLength sentenceCount newLongestLength 0 "" newLongestWord
  | c == '.' =
      analyzeTextHelper cs wordCount totalLength (sentenceCount + 1) longestLength currentLength currentWord longestWord
  | otherwise =
      analyzeTextHelper cs wordCount totalLength sentenceCount longestLength currentLength currentWord longestWord

main :: IO ()
main = do
  putStrLn "Ingrese un texto:"
  text <- getLine
  let (wordCount, averageLength, sentenceCount, longestWord) = analyzeText text
  putStrLn $ "Número total de palabras: " ++ show wordCount
  putStrLn $ "Longitud media de las palabras: " ++ show averageLength
  putStrLn $ "Número de oraciones: " ++ show sentenceCount
  putStrLn $ "Palabra más larga: " ++ longestWord

git config --global user.email "sakudacastro@gmail.com" &&  git config --global user.name "Jose Sakuda"