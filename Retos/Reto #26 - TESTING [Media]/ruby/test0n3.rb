# Hay dos formas de probar esta función:
# - sin usar alguna librería/framework para las pruebas
# - usando alguna librería/framework para las pruebas
#
# lo relevante es tener claro los inputs y las respuestas esperadas.
# en este caso se prueban las siguientes datos:
# - fecha pasada sin viernes 13
# - fecha futura sin viernes 13
# - fecha pasada con viernes 13
# - fecha futura con viernes 13

# frozen_string_literal: true

require_relative '../../Reto #12 - VIERNES 13 [Fácil]/ruby/test0n3'
# importando código con la función para probar.

# ----------------- Sin usar librerías/framework -----------------

SOME_TESTS = { 'input' => [[2022, 4], [2024, 8], [2022, 5], [2024, 9]],
               'output' => [false, false, true, true] }.freeze

errors = 0

SOME_TESTS['input'].each_with_index do |test, index|
  resp = friday13?(test)
  expected = SOME_TESTS['output'][index]
  next if resp == expected

  errors += 1
  puts "\n\noriginal: #{test}"
  puts resp
  puts "expected: #{expected}"
end

puts "\nTests#{errors != 0 ? ' not ' : ' '}passed, #{errors} errors\n"

# ----------------- Usando librerías/framework -----------------

# gem 'minitest', '~> 5.4'
# require 'minitest/autorun'
# require 'minitest/pride'

# # class to test friday13
# class Fridat13Test < Minitest::Test
#   def test_past_not_friday13
#     # skip
#     input = [2022, 4]
#     expected = false
#     assert_equal expected, friday13?(input)
#   end

#   def test_future_not_friday13
#     # skip
#     input = [2024, 8]
#     expected = false
#     assert_equal expected, friday13?(input)
#   end

#   def test_past_friday13
#     # skip
#     input = [2022, 5]
#     expected = true
#     assert_equal expected, friday13?(input)
#   end

#   def test_future_friday13
#     # skip
#     input = [2024, 9]
#     expected = true
#     assert_equal expected, friday13?(input)
#   end
# end
