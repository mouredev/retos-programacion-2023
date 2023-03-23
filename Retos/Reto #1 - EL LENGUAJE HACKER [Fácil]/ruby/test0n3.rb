# frozen_string_literal: true

HACKER_ALPHABET = { 'A': '4', 'B': 'I3', 'C': '[', 'D': ')', 'E': '3', 'F': '|=',
                    'G': '&', 'H': '#', 'I': '1', 'J': ',_|', 'K': '>|', 'L': '1',
                    'M': '/\\/\\', 'N': '^/', 'O': '0', 'P': '|*', 'Q': '(_,)',
                    'R': 'I2', 'S': '5', 'T': '7', 'U': '(_)', 'V': '\/', 'W': '\/\/',
                    'X': '><', 'Y': 'j', 'Z': '2', '1': 'L', '2': 'R', '3': 'E', '4': 'A',
                    '5': 'S', '6': 'b', '7': 'T', '8': 'B', '9': 'g', '0': 'o' }.freeze

def hacker_lang(input)
  input.upcase.chars.map do |char|
    if HACKER_ALPHABET.keys.include? char.to_sym
      HACKER_ALPHABET[char.to_sym]
    else
      char
    end
  end.join
end

TESTS = { input: ['some words', 'SOME WORDS', 'mixEd wOrdS and num63|22',
                  'wOrdS, num63|22; and punctuation.'],
          output: ['50/\\/\\3 \/\/0I2)5',
                   '50/\\/\\3 \/\/0I2)5',
                   '/\\/\\1><3) \/\/0I2)5 4^/) ^/(_)/\\/\\bE|RR',
                   '\/\/0I2)5, ^/(_)/\\/\\bE|RR; 4^/) |*(_)^/[7(_)4710^/.'] }.freeze

errors = 0
TESTS[:input].each_with_index do |test, index|
  resp = hacker_lang(test)
  expected = TESTS[:output][index]
  next unless resp != expected

  errors += 1
  puts "\noriginal: ", test
  puts resp
  puts 'expected:', expected
end

puts "Tests#{errors != 0 ? ' not ' : ' '}passed, #{errors} errors"
