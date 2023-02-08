# frozen_string_literal: true

# module Number
module Number
  def self.prime_fibonacci_even(input)
    return "#{input} no es un número válido" unless input.instance_of? Integer

    "#{input}#{not_prime?(input) ? ' no ' : ' '}es primo,\
#{fibonacci?(input) ? ' es ' : ' no es '}fibonacci y es \
#{input.even? ? 'par' : 'impar'}"
  end

  def self.not_prime?(input)
    return true if input < 2

    limit = Integer.sqrt(input)
    limit = input - 1 if limit <= 2

    (2..limit).each do |i|
      return true if (input % i).zero?
    end
    false
  end

  def self.fibonacci?(input)
    return false if input.negative?

    perfect_square?(5 * input * input + 4) || perfect_square?(5 * input * input - 4)
  end

  def self.perfect_square?(num)
    square_root = Integer.sqrt(num)
    (square_root * square_root == num)
  end
end

# A prime number (or a prime) is a natural number greater than 1
# that is not a product of two smaller natural numbers.
# Solución número primo: https://en.wikipedia.org/wiki/Prime_number#Trial_division

# The Fibonacci sequence, in which each number is the sum of the two preceding ones.
# The sequence commonly starts from 0 and 1, although some authors start
# the sequence from 1 and 1 or sometimes (as did Fibonacci) from 1 and 2.
# Solución número fibonacci: https://www.geeksforgeeks.org/check-number-fibonacci-number/

TESTS = { 'input' => [1, 2, 3, 0, -10, 12.28, 999_999_999],
          'output' => ['1 no es primo, es fibonacci y es impar',
                       '2 es primo, es fibonacci y es par',
                       '3 es primo, es fibonacci y es impar',
                       '0 no es primo, es fibonacci y es par',
                       '-10 no es primo, no es fibonacci y es par',
                       '12.28 no es un número válido',
                       '999999999 no es primo, no es fibonacci y es impar'] }.freeze
errors = 0
TESTS['input'].each_with_index do |test, index|
  resp = Number.prime_fibonacci_even(test)
  expected = TESTS['output'][index]
  next if resp == expected

  errors += 1
  puts "\n\noriginal: #{test}"
  puts resp
  puts "expected: #{expected}"
end

puts "\nTests#{errors != 0 ? ' not ' : ' '}passed, #{errors} errors\n"
