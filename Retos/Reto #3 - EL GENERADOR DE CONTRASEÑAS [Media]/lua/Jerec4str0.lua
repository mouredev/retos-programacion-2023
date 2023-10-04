--Escribe un programa que sea capaz de generar contraseñas de forma aleatoria
--Podrás configurar generar contraseñas con los siguientes parámetros:
-- Longitud: Entre 8 y 16.
-- Con o sin letras mayúsculas.
-- Con o sin números.
--Con o sin símbolos.
-- (Pudiendo combinar todos estos parámetros entre ellos)
local bool
is_long_16 = false
local bool
is_mayus = false
local bool
is_symbols = false
local bool
is_numbers = false

local symbols = { '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '=', '-', '{', '}', '[', ']', '|', ':',
  ';', "'", '"', '<', '>', ',', '.', '?' }
local lower_case_Letters = { 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
  's', 't', 'u', 'v', 'w', 'x', 'y', 'z' }
local uppercase_letters = { 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
  'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' }
local numbers = { '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' }

function long_menu()
  print("--------------------------------------------")
  print("Generador de contraseñas elija una opción")
  print("1. Contraseña de 8 caracteres ")
  print("2. Contraseña de 16 caracteres ")
  print("--------------------------------------------")
  print("\n\n")
  _ = io.read("*n")

  if _ == 1 then
    is_long_16 = true
    passwd_long = 8
  else
    is_long_16 = false
    passwd_long = 16
  end
  print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
  print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
  print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
  print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
  menu_mayus()
end

function menu_mayus()
  print("--------------------------------------------")
  print("Generador de contraseñas elija una opción")
  print("1. Letras mayúsculas")
  print("2. Letras minusculas")
  print("--------------------------------------------")
  print("\n\n")
  _ = io.read("*n")

  if _ == 1 then
    is_long_16 = true
  else
    is_long_16 = false
  end
  print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
  print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
  print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
  print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
  menu_numbers()
end

function menu_numbers()
  print("--------------------------------------------")
  print("Generador de contraseñas elija una opción")
  print("1. Con Numeros")
  print("2. Sin Numeros ")
  print("--------------------------------------------")
  print("\n\n")
  _ = io.read("*n")

  if _ == 1 then
    is_numbers = true
  else
    is_numbers = false
  end
  print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
  print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
  print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
  print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")


  menu_symbols()
end

function menu_symbols()
  print("--------------------------------------------")
  print("Generador de contraseñas elija una opción")
  print("1. Con simbolos")
  print("2. Sin simbolos")
  print("--------------------------------------------")

  print("\n\n")
  _ = io.read("*n")

  if _ == 1 then
    is_numbers = true
  else
    is_numbers = false
  end
end

function passwd_builder()
  long_menu()

  local characters = {}

  if not is_mayus then
    for _, char in ipairs(lower_case_Letters) do
      table.insert(characters, char)
    end
  end

  if is_mayus then
    for _, char in ipairs(uppercase_letters) do
      table.insert(characters, char)
    end
  end

  if is_symbols then
    for _, char in ipairs(symbols) do
      table.insert(characters, char)
    end
  end

  if is_numbers then
    for _, char in ipairs(numbers) do
      table.insert(characters, char)
    end
  end

  local passwd = {}

  for i = 1, passwd_long do
    local randomIndex = math.random(1, #characters)
    table.insert(passwd, characters[randomIndex])
  end

  local generatedpasswd = table.concat(passwd)

  print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
  print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
  print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
  print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
  print(string.format("Contraseña generada: [ %s ]",generatedpasswd))
end

passwd_builder()
