
--   Escribe un programa que muestre por consola (con un print) los
--   números de 1 a 100 (ambos incluidos y con un salto de línea entre
--   cada impresión), sustituyendo los siguientes:

--    Múltiplos de 3 por la palabra "fizz".
--    Múltiplos de 5 por la palabra "buzz".
--    Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".

for i = 1, 100 do
	local output = "" 

	if i % 3 == 0 then
			output = "fizz"
	end

	if i % 5 == 0 then
			output = output .. "buzz"
	end

	if output == "" then
			output = tostring(i)
	end

	print(output)
end
