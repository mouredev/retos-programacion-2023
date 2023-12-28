# frozen_string_literal: true

#
# Crea una función que calcule el número de la columna de una hoja de Excel
# teniendo en cuenta su nombre.
# - Las columnas se designan por letras de la "A" a la "Z" de forma infinita.
#- Ejemplos: A = 1, Z = 26, AA = 27, CA = 79.
#
# class ColumnCounter return numeric position of input
class ColumnCounter
  attr_reader :input, :numeric_position

  # CELL_VALUES = { 'A' => 1, 'B' => 2, 'C' => 3, 'D' => 4, 'E' => 5, 'F' => 6,
  #                 'G' => 7, 'H' => 8, 'I' => 9, 'J' => 10, 'K' => 11, 'L' => 12,
  #                 'M' => 13, 'N' => 14, 'O' => 15, 'P' => 16, 'Q' => '17', 'R' => 18,
  #                 'S' => 19, 'T' => 20, 'U' => 21, 'V' => 22, 'W' => 23, 'X' => 24, 'Y' => 25, 'Z' => 26 }.freeze

  def initialize(input)
    @input = input.upcase
    @numeric_position = to_position
  end

  def to_position
    return 'invalid input' unless valid_input?

    # accum = 0
    # @input.each_char.with_index do |digit, index|
    #   accum += (26**(@input.length - 1 - index) * CELL_VALUES[digit])
    # end
    # accum.to_s

    @input.reverse.each_char.with_index.reduce(0) do |total, (digit, index)|
      total + (digit.ord - 64) * (26**index)
    end.to_s
  end

  def valid_input?
    @input.match?(/^[A-Z]+$/)
  end
end

puts ColumnCounter.new('A').numeric_position
puts ColumnCounter.new('CA').numeric_position
puts ColumnCounter.new('zza').numeric_position
