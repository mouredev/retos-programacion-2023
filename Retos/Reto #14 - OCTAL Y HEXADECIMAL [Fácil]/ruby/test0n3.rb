# frozen_string_literal: true

def transform_to_octal_hex(number)
  { octal: transform_to_octal(number), hex: transform_to_hex(number) }
end

def transform_to_octal(number)
  return '0' if number.zero? || !number.is_a?(Integer)

  octal = []
  quotient = number

  while quotient != 0
    quotient, remain = quotient.divmod(8)
    octal.unshift(remain.to_s)
  end
  octal.join('')
end

def transform_to_hex(number)
  hex_values = { 0 => '0', 1 => '1', 2 => '2', 3 => '3', 4 => '4', 5 => '5', 6 => '6', 7 => '7',
                 8 => '8', 9 => '9', 10 => 'A', 11 => 'B', 12 => 'C', 13 => 'D', 14 => 'E', 15 => 'F' }

  return '0' if number.zero? || !number.is_a?(Integer)

  hex = []
  quotient = number

  while quotient != 0
    quotient, remain = quotient.divmod(16)
    hex.unshift(hex_values[remain])
  end
  hex.join('')
end
