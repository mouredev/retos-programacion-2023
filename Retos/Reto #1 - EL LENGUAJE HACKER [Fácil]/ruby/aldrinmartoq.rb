# Aldrin Martoq - Reto 1
# 
# Esta implementación agrega el método `String#to_1ee7` a cualquier String del programa.
TABLA_1337 = <<~'FIN'.split("\n").map(&:split).to_h
  a 4
  b I3
  c [
  d )
  e 3
  f |=
  g &
  h #
  i 1
  j ,_|
  k >|
  l 1
  m /\/\
  n ^/
  o 0
  p |*
  q (_,)
  r I2
  s 5
  t 7
  u (_)
  v \/
  w \/\/
  x ><
  y j
  z 2
  1 L
  2 R
  3 E
  4 A
  5 S
  6 b
  7 T
  8 B
  9 g
  0 o
FIN

class String
  def to_1337
    each_char.map { |char| TABLA_1337[char.downcase] || char }.join
  end
end

# Ejemplos de uso:
puts 'EL "LENGUAJE HACKER"'.to_1337
# => "31 \"13^/&(_)4,_|3 #4[>|3I2\""

print 'Ingrese un texto: '.to_1337
puts gets.to_1337
