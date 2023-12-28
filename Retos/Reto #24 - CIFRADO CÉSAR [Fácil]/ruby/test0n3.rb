# frozen_string_literal: true

# class CaesarCypher
class CaesarCipher
  attr_accessor :input

  ALPHABET = { 'a' => 0, 'b' => 1, 'c' => 2, 'd' => 3, 'e' => 4, 'f' => 5, 'g' => 6, 'h' => 7,
               'i' => 8, 'j' => 9, 'k' => 10, 'l' => 11, 'm' => 12, 'n' => 13, 'ñ' => 14, 'o' => 15,
               'p' => 16, 'q' => 17, 'r' => 18, 's' => 19, 't' => 20, 'u' => 21, 'v' => 22,
               'w' => 23, 'x' => 24, 'y' => 25, 'z' => 26 }.freeze

  SWIFT_DIRECTIONS = { 'positive' => 1, 'negative' => -1 }.freeze

  def initialize(input = { text: nil, action: nil })
    @input = input
    @text = input[:text]
    @action = input[:action]
    @swift_direction = SWIFT_DIRECTIONS['positive']
    @swift_number = 3
  end

  def act
    return 'input missing' if @action.nil? || @input.nil?

    process_text
  end

  def process_text
    @text.chars.map do |letter|
      pos = ALPHABET[letter.downcase]
      if pos.nil?
        letter
      else
        new_value = ALPHABET.key(new_position(pos)).dup
        upcase?(letter) ? new_value.upcase! : new_value
      end
    end.join
  end

  private

  def upcase?(character)
    character == character.upcase
  end

  def new_position(position)
    offset = @swift_direction * @swift_number
    offset *= -1 if @action == 'decipher'

    (position + offset) % ALPHABET.size
  end
end

# puts CaesarCipher.new({ text: 'The quick brown fox jumps over the lazy dog.', action: 'cipher' }).act
# puts CaesarCipher.new({ text: 'Wkh txlfn eurzp ira mxosv ryhu wkh ñdcb grj.', action: 'decipher' }).act
# puts CaesarCipher.new.act
