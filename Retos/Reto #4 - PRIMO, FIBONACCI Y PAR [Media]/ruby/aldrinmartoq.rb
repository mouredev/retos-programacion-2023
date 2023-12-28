# Aldrin Martoq - Reto 4
# 
# Esta implementación agrega el método `Integer#reto4` a cualquier entero del programa,
# así como #primicidad #fibonaccidad y #paridad que retornan el mensaje de cada prueba en particular.
class Integer
  def reto4 = "#{self} #{primicidad}, #{fibonaccidad} y #{paridad}"

  # implementación LENTA; pero ilustrativa
  def fibonaccidad
    a = 0
    b = c = 1
    while a < self
      c = b + a
      b, a = c, b
    end

    a == self ? 'es fibonacci' : 'NO es fibonacci'
  end

  # iteramos desde 2 hasta √n, con n ≥ 2
  def primicidad = (self < 2 || (2..Math.sqrt(self).floor).find { |factor| self % factor == 0 }) ? 'NO es primo' : 'es primo'

  # convierte odd? al texto pedido
  def paridad = odd? ? 'es impar' : 'NO es impar'
end

# ejemplos de uso:
puts 1.reto4          # => "1 es primo, es fibonacci y es impar"
puts 123456789.reto4  # => "123456789 NO es primo, NO es fibonacci y es impar"

print 'Ingrese un número: '
puts gets.to_i.reto4
