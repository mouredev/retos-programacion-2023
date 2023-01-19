# frozen_string_literal: true

# source for scores: https://es.wikipedia.org/wiki/Tenis#Puntuaci%C3%B3n

# class TennisMatch
class TennisMatch
  SCORES = { '0' => 'love', '1' => '15', '2' => '30', '3' => '40', '4' => '50' }.freeze
  SCORE_TO_SPANISH = { 'advantage' => 'ventaja', 'game' => 'ha ganado el' }.freeze

  def initialize(input)
    @input = input
  end

  def game_score
    return [[-1, -1]] unless valid_input?

    scores = []
    @input.each do |player|
      temp = scores.last.dup || [0, 0]
      temp[0] += 1 if player == 'P1'
      temp[1] += 1 if player == 'P2'
      scores << temp
    end
    scores
  end

  def tennis_score
    resp = game_score
    return ['invalid input'] unless valid_score?(resp)

    resp.map do |p1, p2|
      diff = (p1 - p2).abs
      if ((p1 < 3) || (p2 < 3)) && (diff <= 3)
        [SCORES[p1.to_s], SCORES[p2.to_s]]
      elsif diff.zero?
        ['deuce']
      elsif diff == 1
        ["advantage #{p1 > p2 ? 'P1' : 'P2'}"]
      elsif p1.zero? || p2.zero? || diff > 1
        ["game #{p1 > p2 ? 'P1' : 'P2'}"]
      else
        raise 'I shall never be reached ;-)'
      end
    end
  end

  def print_game_score_es
    puts "\n\nJuego de Tennis\n===============\n\nP1  |  P2\n---------"
    if tennis_score == ['invalid input']
      puts 'input inválido'
    else
      tennis_score.each do |p1, p2|
        print translate_to_spanish(p1)
        print p2 ? "  |  #{translate_to_spanish(p2)}\n" : "\n"
      end
    end
  end

  private

  def valid_input?
    return false if @input.empty?

    @input.all? { |x| x =~ /(P1)|(P2)/ }
  end

  def valid_score?(scores)
    p1, p2 = scores.last
    diff = (p1 - p2).abs
    return true if (diff == 2) || (diff == 4 && [p1, p2].include?(0))

    false
  end

  def translate_to_spanish(score)
    return nil if score.nil?

    resp = nil
    SCORE_TO_SPANISH.each do |key, value|
      resp = score.gsub(/#{key}/, value.capitalize) if score.match?(/#{key}/)
    end
    resp ||= score.capitalize
  end
end

# Tests types
# 1. completo: válido P1 tiene +2 que P1 después de 3 puntos
# 2. completo: válido, P2 llega a 3 puntos primero
# 3. input inválido, vacio
# 4. input inválido, input tiene información puntaje extra
# 5. input inválido, input tiene información puntaje extra
# 6. input inválido, input incompleto
# 7. input inválido, input incorrecto

TESTS = { input: [%w[P1 P1 P2 P2 P1 P2 P1 P1],
                  %w[P2 P2 P2 P2],
                  %w[],
                  %w[P1 P1 P2 P2 P1 P2 P1 P1 P1],
                  %w[P2 P2 P2 P2 P2],
                  %w[P1 P1 P2 P2],
                  %w[P1 A2 p p2]],
          output: [[[1, 0], [2, 0], [2, 1], [2, 2], [3, 2], [3, 3], [4, 3], [5, 3]],
                   [[0, 1], [0, 2], [0, 3], [0, 4]],
                   [[-1, -1]],
                   [[1, 0], [2, 0], [2, 1], [2, 2], [3, 2], [3, 3], [4, 3], [5, 3], [6, 3]],
                   [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5]],
                   [[1, 0], [2, 0], [2, 1], [2, 2]],
                   [[-1, -1]]] }.freeze

errors = 0
TESTS[:input].each_with_index do |test, index|
  resp = TennisMatch.new(test).game_score
  expected = TESTS[:output][index]
  next unless resp != expected

  errors += 1
  print "\n\noriginal: ", test
  print "\n", resp
  print "\nexpected: ", expected
end

puts "\n\nTests#{errors != 0 ? ' not ' : ' '}passed, #{errors} errors\n"

TESTS[:input].each do |test|
  new_resp = TennisMatch.new(test)
  new_resp.print_game_score_es
end
