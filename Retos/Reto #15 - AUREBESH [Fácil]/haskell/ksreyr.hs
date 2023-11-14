import Data.Map qualified as Map

aurebeshMap :: Map.Map Char String
aurebeshMap =
  Map.fromList
    [ ('a', "Aurek"),
      ('b', "Besh"),
      ('c', "Cresh"),
      ('d', "Dorn"),
      ('e', "Esk"),
      ('f', "Forn"),
      ('g', "Grek"),
      ('h', "Herf"),
      ('i', "Isk"),
      ('j', "Jenth"),
      ('k', "Krill"),
      ('l', "Leth"),
      ('m', "Mern"),
      ('n', "Nern"),
      ('o', "Osk"),
      ('p', "Peth"),
      ('q', "Qek"),
      ('r', "Resh"),
      ('s', "Senth"),
      ('t', "Trill"),
      ('u', "Uthar"),
      ('v', "Vev"),
      ('w', "Wesk"),
      ('x', "Xesh"),
      ('y', "Yirt"),
      ('z', "Zur"),
      (' ', " ")
    ]

encode :: Char -> String
encode c = case Map.lookup c aurebeshMap of
  Just s -> s
  Nothing -> ""

decode :: String -> String
decode s = case [k | (k, v) <- Map.toList aurebeshMap, v == s] of
  [] -> ""
  (k : _) -> [k]

main :: IO ()
main = do
  -- para probar el de espanol a AUREBESH descomenta la siguiente linea.
  putStrLn (concat [encode x | x <- "Hola a todos"])

-- para probar de codificar de AUREBESH a espanol descomenta la siguiente linea.
-- putStrLn $ decode "Aurek"
-- TODO: Que decodifique mas que una sola letra, te lo debo 'XD XD'.
