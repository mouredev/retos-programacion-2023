# frozen_string_literal: false

# class for game Hangman
class Hangman
  def initialize(original_word)
    @original_word = original_word
    @missing_chars_pos = pick_blank_pos
    @attempts = @missing_chars_pos.length + 1
    @missing_chars = set_missing_chars
    @game_word = set_game_word
  end

  def pick_blank_pos
    max_missing_chars = Random.rand(@original_word.length * 6 / 10) + 1
    missing_pos = []
    while max_missing_chars.positive?
      char_pos = Random.rand(@original_word.length)
      next if (@original_word[char_pos] == ' ') || (missing_pos.include? char_pos)

      missing_pos.push(char_pos)
      max_missing_chars -= 1
    end
    missing_pos
  end

  def set_missing_chars
    @missing_chars_pos.map do |pos|
      @original_word[pos]
    end
  end

  def set_game_word
    game_word = @original_word.clone
    @missing_chars_pos.each do |pos|
      game_word[pos] = '_'
    end
    game_word
  end

  def check_char(user_input)
    return @attempts -= 1 unless @missing_chars.include? user_input

    pos_char = (0...@original_word.length).find_all { |i| @original_word[i] == user_input }

    @missing_chars_pos -= pos_char # TODO: not required if refactoring of pick_blank_pos, set_missing_chars, set_game_word
    @missing_chars -= [user_input]
    pos_char.each do |pos|
      @game_word[pos] = user_input
    end
    @attempts = 0 if @original_word == @game_word
  end

  def check_word(user_input)
    if @original_word == user_input
      @attempts = 0
      @game_word = user_input
    else
      @attempts -= 1
    end
  end

  def puts_user_request
    print "\nWord to complete is: #{@game_word}
    \nYou have #{@attempts} left, you can type a character or the whole word [a-z].
    \nWhat's your input?\t"
    gets.chomp
  end

  def win_message
    "You win!\nThe word is #{@game_word}"
  end

  def lose_message
    "You lose!\nThe expected word is #{@original_word}"
  end

  def end_game
    if @game_word == @original_word
      puts win_message
    else
      puts lose_message
    end
  end

  def start
    puts "Hangman game\n------------\nInput only characters, [a-z], to complete the word."

    while @attempts.positive?
      user_input = puts_user_request
      if user_input.length < 2
        check_char(user_input)
      else
        check_word(user_input)
      end
    end
    end_game
  end
end

Hangman.new('first try with a long sentence').start
