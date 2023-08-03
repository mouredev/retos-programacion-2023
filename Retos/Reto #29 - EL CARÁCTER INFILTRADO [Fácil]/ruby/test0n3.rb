# frozen_string_literal: true

#
# Crea una función que reciba dos cadenas de texto casi iguales,
# a excepción de uno o varios caracteres.
# La función debe encontrarlos y retornarlos en formato lista/array.
# - Ambas cadenas de texto deben ser iguales en longitud.
# - Las cadenas de texto son iguales elemento a elemento.
# - No se pueden utilizar operaciones propias del lenguaje
#   que lo resuelvan directamente.
#
# Ejemplos:
# - Me llamo mouredev / Me llemo mouredov -> ["e", "o"]
# - Me llamo.Brais Moure / Me llamo brais moure -> [" ", "b", "m"]
#

# class Sentence get different characters between two sentences
class Sentence
  attr_accessor :sentence1, :sentence2

  def initialize(sentence1, sentence2)
    @sentence1 = sentence1
    @sentence2 = sentence2
    @diff = []
  end

  def find_diff
    return false if @sentence1.length != @sentence2.length

    @sentence1.length.times do |i|
      @diff << @sentence2[i] if sentence1[i] != sentence2[i]
    end
    @diff
  end
end

p Sentence.new('Me llamo mouredev', 'Me llemo mouredov').find_diff
p Sentence.new('Me llamo.Brais Moure', 'Me llamo brais moure').find_diff
p Sentence.new('first sentence', 'second sentence').find_diff
p Sentence.new('first  sentence', 'second sentence').find_diff
