# frozen_string_literal: true

def url_params(url)
  return [] unless url.count('?') == 1

  params = divide_string(url, '?')
  values = []

  params.split('&').each do |param|
    values.push(divide_string(param, '=')) if param.match?(/\D+(={1})\w+/)
  end
  values
end

def divide_string(string, char)
  params_idx = string.rindex(char)
  string.slice(params_idx + 1..string.size)
end

TESTS = { 'input' => ['https://retosdeprogramacion.com?year=2023&challenge=0',
                      'https://retosdeprogramacion.com/search?year=2023',
                      'https://retosdeprogramacion.com/params/name/lastname',
                      'retosdeprogramacion.com/search?',
                      ''],
          'output' => [%w[2023 0],
                       %w[2023],
                       [],
                       [],
                       []] }.freeze

errors = 0
TESTS['input'].each_with_index do |test, index|
  resp = url_params(test)
  expected = TESTS['output'][index]
  next if resp == expected

  errors += 1
  puts "\n\noriginal: #{test}"
  puts resp
  puts "expected: #{expected}"
end

puts "\nTests#{errors != 0 ? ' not ' : ' '}passed, #{errors} errors\n"
