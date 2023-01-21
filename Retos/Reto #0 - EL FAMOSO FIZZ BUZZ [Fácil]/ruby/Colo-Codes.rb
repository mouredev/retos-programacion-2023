=begin
  Escribe un programa que muestre por consola (con un print) los
  números de 1 a 100 (ambos incluidos y con un salto de línea entre
  cada impresión), sustituyendo los siguientes:
  - Múltiplos de 3 por la palabra "fizz".
  - Múltiplos de 5 por la palabra "buzz".
  - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
=end
# Fuerza bruta:
=begin
for i in 1..100 do
    if i % 3 == 0 && i % 5 == 0
        p 'fizzbuzz'
    elsif i % 3 == 0
        p 'fizz'
    elsif i % 5 == 0
        p 'buzz'
    else
        p "#{i}"
    end
end
=end

# Más eficiente
100.times do |i|
  i += 1
  output = "#{(i % 3).zero? ? 'fizz' : ''}#{(i % 5).zero? ? 'buzz' : ''}#{!(i % 3).zero? && !(i % 5).zero? ? i : ''}"
  p output
end
