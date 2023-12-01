#
# Escribe un programa que muestre por consola (con un print) los
# números de 1 a 100 (ambos incluidos y con un salto de línea entre
# cada impresión), sustituyendo los siguientes:
# - Múltiplos de 3 por la palabra "fizz".
# - Múltiplos de 5 por la palabra "buzz".
# - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
#

 def fizzbuzz(limit : Int32)
   (1..limit).each do |number|
     if number % 3 == 0 && number % 5 == 0
       puts "fizzbuzz"
     elsif number % 3 == 0
       puts "fizz"
     elsif number % 5 == 0
       puts "buzz"
     else 
       puts number.to_s
     end
   end
 end



 # Call the funcion with limit
 fizzbuzz(100)
