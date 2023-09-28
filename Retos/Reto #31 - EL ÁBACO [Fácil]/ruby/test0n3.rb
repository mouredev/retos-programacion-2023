# frozen_string_literal: true

#
#  Crea una función que sea capaz de leer el número representado por el ábaco.
#  - El ábaco se representa por un array con 7 elementos.
#  - Cada elemento tendrá 9 "O" (aunque habitualmente tiene 10 para realizar operaciones)
#    para las cuentas y una secuencia de "---" para el alambre.
#  - El primer elemento del array representa los millones, y el último las unidades.
#  - El número en cada elemento se representa por las cuentas que están a la izquierda del alambre.
#
#  Ejemplo de array y resultado:
#  ["O---OOOOOOOO",
#   "OOO---OOOOOO",
#   "---OOOOOOOOO",
#   "OO---OOOOOOO",
#   "OOOOOOO---OO",
#   "OOOOOOOOO---",
#   "---OOOOOOOOO"]
#
#   Resultado: 1.302.790
#

# class Abacus
class Abacus
  attr_reader :input, :arabic_number

  def initialize(input)
    @input = input
    @arabic_number = abacus_to_arabic
  end

  def abacus_to_arabic
    return 'Invalid input' if @input.length.zero?

    string_number = ''
    # ATTENTION: reverse solution
    # @input.reverse_each.with_index do |elem, index|
    #   return string_number = 'Invalid input' unless valid_string?(elem)

    #   string_number = ".#{string_number}" if index >= 3 && (index % 3).zero?

    #   string_number = "#{elem.slice(0, elem.index('---')).length}#{string_number}"
    # end

    # ATTENTION: solution with each_with_index
    @input.each_with_index do |elem, index|
      return string_number = 'Invalid input' unless valid_string?(elem)

      string_number = "#{string_number}#{elem.slice(0, elem.index('---')).length}"
      string_number = "#{string_number}." if (index % 3).zero? && @input.length - 1 != index
    end
    string_number
  end

  def valid_string?(string)
    string.length == 12 && string.include?('---')
  end
end

# puts Abacus.new([]).arabic_number

# puts Abacus.new(['000---000000',
#                  '00000---0000',
#                  '000000---000',
#                  '---000000000']).arabic_number
