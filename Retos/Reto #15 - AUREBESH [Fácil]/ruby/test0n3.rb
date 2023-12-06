# frozen_string_literal: true

AUREBESH = { 'a' => 'aurek', 'ae' => 'enth', 'b' => 'besh', 'c' => 'cresh', 'ch' => 'cherek',
             'd' => 'dorn', 'e' => 'esk', 'eo' => 'onith', 'f' => 'forn', 'g' => 'grek',
             'h' => 'herf', 'i' => 'isk', 'j' => 'jenth', 'k' => 'krill', 'kh' => 'krenth',
             'l' => 'leth', 'm' => 'mern', 'n' => 'nern', 'ng' => 'nen', 'o' => 'osk', 'oo' => 'orenth',
             'p' => 'peth', 'q' => 'qek', 'r' => 'resh', 's' => 'senth', 'sh' => 'shen',
             't' => 'trill', 'th' => 'thesh', 'u' => 'usk', 'v' => 'vev', 'w' => 'wesk',
             'x' => 'xesh', 'y' => 'yirt', 'z' => 'zerek', ',' => ',', '.' => '.',
             '?' => '?', '!' => '!', ':' => ':', ';' => ';', '-' => '-', '"' => '"',
             '\'' => '\'', '(' => '(', ')' => ')', '/' => '/', '$' => '$' }.freeze

def to_aurebesh(word)
  output = ''
  idx = 0
  while idx < word.length
    options = gather_to_aurebesh_options(word[idx])
    char = options[word[idx]] || word[idx]

    if idx + 1 < word.length && !options[word[idx] + word[idx + 1]].nil?
      char = options[word[idx] + word[idx + 1]]
      idx += 1
    end

    output += char
    idx += 1
  end
  output
end

def from_aurebesh(word)
  output = ''
  idx = 0
  while idx < word.length
    char = word[idx]
    options = gather_from_aurebesh_options(char)

    options.map do |key, value|
      next unless word[idx, value.length] == value

      char = key
      idx += value.length
    end
    output += char
    idx += 1 if options.length.zero? || char == word[idx]

  end
  output
end

def gather_to_aurebesh_options(char)
  AUREBESH.select { |key, _| /^#{char}/.match?(key) }
end

def gather_from_aurebesh_options(char)
  AUREBESH.select { |_, value| /^#{char}/.match?(value) }
end

# p "to_aurebesh: #{to_aurebesh('áb é, ñ')}"
# p "to_aurebesh: #{to_aurebesh('biux')}"
# p "to_aurebesh: #{to_aurebesh('bars')} \n"
# p "to_aurebesh: #{to_aurebesh('barsh')} \n"

# p "from_aurebesh: #{from_aurebesh('ábesh, é, ñ')}"
# p "from_aurebesh: #{from_aurebesh('beshiskuskxesh')}"
# p "from_aurebesh: #{from_aurebesh('beshaurekreshsenth')}"
# p "from_aurebesh: #{from_aurebesh('beshaurekreshshen')}"
# p "from_aurebesh: #{from_aurebesh('some text')}"
