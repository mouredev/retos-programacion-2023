# frozen_string_literal: true

CONTENDERS = { '✀' => { 'win' => ['📄', '🦎'],
                        'lose' => ['🖖', '🗿'] },
               '📄' => { 'win' => ['🗿', '🖖'],
                        'lose' => ['✀', '🦎'] },
               '🗿' => { 'win' => ['🦎', '✀'],
                        'lose' => ['📄', '🖖'] },
               '🦎' => { 'win' => ['🖖', '📄'],
                        'lose' => ['🗿', '✀'] },
               '🖖' => { 'win' => ['✀', '🗿'],
                        'lose' => ['🦎', '📄'] } }.freeze

def game(arr)
  resp = [0, 0]
  arr.each do |p1, p2|
    resp[0] += 1 if CONTENDERS[p1]['win'].include? p2
    resp[1] += 1 if CONTENDERS[p1]['lose'].include? p2
  end
  resp
end

def rock_paper_scissors_lizzard_spock(input)
  resp = game(input)
  return 'Tie' if resp[0] == resp[1]

  if resp[0] > resp[1]
    'Player1'
  else
    'Player2'
  end
end

TESTS = { 'input' => [[['🗿', '✀'], ['✀', '🗿'], ['📄', '✀']],
                      [['🖖', '🗿'], ['🗿', '🦎'], ['🦎', '✀']],
                      [['📄', '📄'], ['🗿', '🗿'], ['🖖', '🖖']],
                      [['🗿', '✀'], ['🦎', '✀'], '🖖', '🖖']],
          'output' => %w[Player2 Player1 Tie Tie] }.freeze
errors = 0
TESTS['input'].each_with_index do |test, index|
  resp = rock_paper_scissors_lizzard_spock(test)
  expected = TESTS['output'][index]
  next if resp == expected

  errors += 1
  puts "\n\noriginal: #{test}"
  puts resp
  puts "expected: #{expected}"
end

puts "\nTests#{errors != 0 ? ' not ' : ' '}passed, #{errors} errors\n"
