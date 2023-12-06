# frozen_string_literal: true

#
# Crea una función que reciba una expresión matemática (String)
# y compruebe si es correcta. Retornará true o false.
# - Para que una expresión matemática sea correcta debe poseer
#   un número, una operación y otro número separados por espacios.
#   Tantos números y operaciones como queramos.
# - Números positivos, negativos, enteros o decimales.
# - Operaciones soportadas: + - * / %
#
# Ejemplos:
# "5 + 6 / 7 - 4" -> true
# "5 a 6" -> false
#

# class Calculator, check if string is a valid operation
class Calculator
  attr_accessor :operation

  def initialize(operation)
    @operation = operation.split(' ')
  end

  def valid_operation
    return false if invalid?

    @operation.each do |item|
      return false unless number?(item) || operator?(item)
    end
    true
  end

  def invalid?
    operation_length = @operation.length
    operation_length < 3 || operation_length.even?
  end

  def number?(string)
    !Float(string).nil?
  rescue StandardError
    false
  end

  def operator?(string)
    string.match?(%r{[+\-*/%]}) && string.length == 1
  end
end

# puts Calculator.new('-5 + 12%3').valid_operation
# puts Calculator.new('-5').valid_operation
# puts Calculator.new('5 / 3').valid_operation
# puts Calculator.new('5 / -3 * 2').valid_operation
