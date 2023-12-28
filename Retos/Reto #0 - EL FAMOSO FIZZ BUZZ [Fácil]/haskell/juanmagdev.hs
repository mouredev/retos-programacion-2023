fizzbuzz :: Integer -> String
fizzbuzz 0 = "0"
fizzbuzz n | n `mod` 15 == 0 = "FizzBuzz"
           | n `mod` 3 == 0 = "Fizz"
           | n `mod` 5 == 0 = "Buzz"
           | otherwise = show n

main = mapM_ putStrLn [fizzbuzz x | x <- [0..100]]