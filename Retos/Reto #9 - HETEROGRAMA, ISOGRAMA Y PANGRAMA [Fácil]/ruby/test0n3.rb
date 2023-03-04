# frozen_string_literal: true

# Heterograma (del griego héteros, 'diferente' y gramma, 'letra') es una palabra
# o frase que no contiene ninguna letra repetida.

# Isograma (del griego isos, 'igual' y gramma, 'letra') es una palabra o frase
# en la que cada letra aparece el mismo número de veces.

# Pangrama (del griego pan, 'todo' y gramma, 'letra') es una frase en la que
# aparecen todas las letras del abecedario.

# TestString checks if string is an heterogram, isogram or pangram
class TestStrings
  def initialize(str)
    @string = str
    @unique_characters = count_chars
  end

  def count_chars
    @string.downcase
           .tr('áéíóúüñ', 'aeiouun')
           .tr('.,;:\-\" ', '')
           .chars
           .each_with_object(Hash.new(0)) do |value, key|
      key[value] += 1
    end
  end

  def heterogram?
    return false if @unique_characters.empty?

    @unique_characters.values.all?(1)
  end

  def isogram?
    return false if @unique_characters.empty?

    @unique_characters.values.all?(@unique_characters.values.min)
  end

  def pangram?
    alphabet = ('a'..'z').to_a
    @unique_characters.keys.sort == alphabet
  end

  def string_features
    [heterogram?, isogram?, pangram?]
  end
end

TESTS = { 'input' => ['centrifugadlos',
                      'shanghaiings',
                      'nana',
                      'a',
                      '',
                      'Benjamín pidió una bebida de kiwi y fresa. Noé, sin vergüenza, la más exquisita champaña del menú'],
          'output' => [[true, true, false],
                       [false, true, false],
                       [false, true, false],
                       [true, true, false],
                       [false, false, false],
                       [false, false, true]] }.freeze

errors = 0
TESTS['input'].each_with_index do |test, index|
  resp = TestStrings.new(test).string_features
  expected = TESTS['output'][index]
  next if resp == expected

  errors += 1
  puts "\n\noriginal: #{test}"
  puts resp
  puts "expected: #{expected}"
end

puts "\nTests#{errors != 0 ? ' not ' : ' '}passed, #{errors} errors\n"
