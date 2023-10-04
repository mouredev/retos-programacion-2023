-- Escribe un programa que reciba un texto y transforme lenguaje natural a
-- "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
-- se caracteriza por sustituir caracteres alfanuméricos.
-- Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
-- con el alfabeto y los números en "leet".
-- (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")


local keys =
{
  a = "4",
  b = "I3",
  c = "[",
  d = ")",
  e = '3',
  f = "|",
  g = "&",
  h = "#",
  i = "1",
  j = ",_|",
  k = ">|",
  l = "1",
  m = "/" .. "\\" .. "/" .. "\\"
}

io.write("Ingrese el texto a cifrar: ")
local texto = io.read()
local textoCifrado = ""

for i = 1, #texto do
  local caracter = texto:sub(i, i)
  local valorCifrado = keys[caracter]
  if valorCifrado then
    textoCifrado = textoCifrado .. valorCifrado
  else
    textoCifrado = textoCifrado .. caracter
  end -- if end
end   -- for end

io.write("Texto Cifrado: \n")
print(textoCifrado)
