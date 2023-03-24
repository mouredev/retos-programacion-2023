# frozen_string_literal: true

require 'date'

def friday13?(date)
  Date.new(*date, 13).friday?
end

TESTS = { 'input' => [[2023, 3], [2023, 10], [2024, 9], [2023, 2]],
          'output' => [false, true, true, false] }.freeze

errors = 0

TESTS['input'].each_with_index do |test, index|
  resp = friday13?(test)
  expected = TESTS['output'][index]
  next if resp == expected

  errors += 1
  puts "\n\noriginal: #{test}"
  puts resp
  puts "expected: #{expected}"
end

puts "\nTests#{errors != 0 ? ' not ' : ' '}passed, #{errors} errors\n"
