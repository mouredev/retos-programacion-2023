#
# Los primeros dispositivos móviles tenían un teclado llamado T9
# con el que se podía escribir texto utilizando únicamente su
# teclado numérico (del 0 al 9).
#
# Crea una función que transforme las pulsaciones del T9 a su
# representación con letras.
# - Debes buscar cuál era su correspondencia original.
# - Cada bloque de pulsaciones va separado por un guión.
# - Si un bloque tiene más de un número, debe ser siempre el mismo.
# - Ejemplo:
#     Entrada: 6-666-88-777-33-3-33-888
#     Salida: MOUREDEV
#

# frozen_string_literal: true

# class cellphone dial
class CellphoneDial
  attr_reader :input, :translated

  DIAL = { '1' => '1', '2' => 'ABC2', '3' => 'DEF3', '4' => 'GHI4', '5' => 'JKL5',
           '6' => 'MNO6', '7' => 'PQRS7', '8' => 'TUV8', '9' => 'WXYZ9',
           '0' => ' 0', '*' => '*', '#' => '#' }.freeze

  def initialize(input)
    @input = input.split('-')
    @translated = translate
  end

  def translate
    @input.map do |char|
      char_pos = (char.length % DIAL[char[0]].length) - 1
      DIAL[char[0]][char_pos]
    end.join('')
  end
end

puts "cellphone dial: #{CellphoneDial.new('6-666-88-777-33-3-33-888').translated}"
puts "cellphone dial: #{CellphoneDial.new('6-99999999-0-8-33-777777777-8').translated}"
