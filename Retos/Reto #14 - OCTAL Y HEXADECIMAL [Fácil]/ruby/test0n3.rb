# frozen_string_literal: true

def transform_to_octal_hex(number)
  { octal: transform_to_octal(number), hex: transform_to_hex(number) }
end

def transform_to_octal(number)
  octal = []
  cocient = number

  return '0' if number.zero? || !number.is_a?(Integer)

  # num = number
  while cocient != 0
    remain = cocient % 8
    cocient = cocient.div(8)
    octal.unshift(remain.to_s)
  end
  octal.join('')
end

def transform_to_hex(number)
  hex = []
  cocient = number

  return '0' if number.zero? || !number.is_a?(Integer)

  while cocient != 0
    remain = cocient % 16
    cocient = cocient.div(16)
    hex.unshift(remain.to_s)
  end
  hex.join('')
end
