# frozen_string_literal: false

# Password generator
class Password
  CHARACTER_TYPE = { '0' => 'ascii', '1' => 'numbers', '2' => 'symbols' }.freeze
  CHARACTERS = 'abcdefghijklmnopqrstuvwxyz'.freeze
  NUMBERS = '0123456789'.freeze
  SYMBOLS = '-!().?[]_`~@#$^&*+='.freeze

  def initialize(num_char, uppercase, numbers, symbols)
    @num_char = check_pass_length(num_char)
    @uppercase = uppercase
    @numbers = numbers
    @symbols = symbols
  end

  def password_generator
    errors = 1
    while errors != 0
      pass_string = ''
      pass_string << set_character while pass_string.length < @num_char
      errors = check_result(pass_string)
    end

    pass_string
  end

  private

  def set_character
    char_type = CHARACTER_TYPE.keys.sample
    if char_type == '1' && @numbers
      letter = NUMBERS.split('').sample
    elsif char_type == '2' && @symbols
      letter = SYMBOLS.split('').sample
    else
      letter = CHARACTERS.split('').sample
      letter.upcase! if @uppercase && Random.rand(2).zero?
    end
    letter
  end

  def check_pass_length(required_length)
    return 8 if required_length < 8 || required_length.nil?
    return 16 if required_length > 16

    required_length
  end

  def check_result(pass_candidate)
    errors = 0

    errors += 1 if ['-', '.'].include? pass_candidate[0]
    errors += 1 if @uppercase && !pass_candidate.match?(/[A-Z]/)
    errors += 1 if @numbers && !pass_candidate.match?(/[0-9]/)
    errors += 1 if @symbols && !pass_candidate.match?(Regexp.new('[-!().?\[\]_`~@#$^&*+=]'))
    errors
  end
end

# caracteres tolerados para password:
# Lowercase characters {a-z}
# Uppercase characters {A-Z}
# Numbers {0-9}
# Exclamation point {!}
# Open parenthesis {(}
# Close parenthesis {)}
# Dash {-}; this character is not supported as the first character in the user ID or password
# Period {.}; this character is not supported as the first character in the user ID or password
# Question mark {?}
# Open bracket {[}
# Close bracket {]}
# Underscore {_};

# this is the only supported special character in IBM i:
# Grave accent {`}
# Tilde {~}
# Commercial at {@}
# Number sign {#}
# Dollar sign {$}
# Circumflex accent {^}
# Ampersand {&}
# Asterisk
# {*}
# Plus sign {+}
# Equals sign {=}

TESTS = [[8, true, false, false], [10, true, true, false], [10, true, true, true], [10, false, true, true],
         [10, false, false, true], [7, false, false, false], [18, false, false, false]].freeze

errors = 0
TESTS.each_with_index do |test, _index|
  resp = Password.new(*test).password_generator

  if test[0] < 8 && resp.length != 8
    errors += 1
  elsif test[0] > 16 && resp.length != 16
    errors += 1
  end

  errors += 1 if ['-', '.'].include? resp[0]
  errors += 1 if test[1] && !resp.match?(/[A-Z]/)
  errors += 1 if test[2] && !resp.match?(/[0-9]/)
  errors += 1 if test[3] && !resp.match?(Regexp.new('[-!().?\[\]_`~@#$^&*+=]'))

  print "\n\noriginal: ", test
  print "\n", resp
  puts "\nerrors: #{errors}"
end

puts "\n\nTests#{errors != 0 ? ' not ' : ' '}passed, #{errors} errors\n"
