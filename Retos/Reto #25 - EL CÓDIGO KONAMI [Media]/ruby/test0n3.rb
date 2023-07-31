# frozen_string_literal: true

require 'io/console'

# Reads keypresses from the user including 2 and 3 escape character sequences.
# def read_char
#   $stdin.echo = false
#   $stdin.raw!

#   input = $stdin.getc.chr
#   if input == "\e"
#     begin
#       input << $stdin.read_nonblock(3)
#     rescue StandardError
#       nil
#     end
#     begin
#       input << $stdin.read_nonblock(2)
#     rescue StandardError
#       nil
#     end
#   end
# ensure
#   $stdin.echo = true
#   $stdin.cooked!

#   return input
# end

# # original case statement from:
# # http://www.alecjacobson.com/weblog/?p=75
# def show_single_key
#   c = read_char

#   case c
#   when ' '
#     print ' '
#   when "\t"
#     print '  '
#   when "\r"
#     puts "\r"
#   when "\n"
#     puts "\n"
#   when "\e"
#     puts 'Esc'
#   when "\e[A"
#     print '⇧'
#   when "\e[B"
#     print '⇩'
#   when "\e[C"
#     print '⇨'
#   when "\e[D"
#     print '⇦'
#   when "\177"
#     print "\177"
#   when "\004"
#     print "\004"
#   when "\e[3~"
#     print 'ALTERNATE DELETE'
#   when "\u0003"
#     print 'CONTROL-C'
#     exit 0
#   # when /^.$/
#   #   print "SINGLE CHAR HIT: #{c.inspect}"
#   when /^.$/
#     print c.upcase
#   else
#     print "SOMETHING ELSE: #{c.inspect}"
#   end
# end

# show_single_key while true

# class to read keyboard input
class KeyboardReader
  KEYBOARD_MAP = { "\t" => "\t", "\n" => '↲', "\e" => 'Esc', "\e[A" => '⇧', "\e[B" => '⇩', "\e[C" => '⇨', "\e[D" => '⇦',
                   "\u0003" => "\u0003", ' ' => ' ', ',' => ',', '.' => '.' }.freeze

  def initialize
    @continue_input = true
    @char_collector = ''
  end

  def start
    while @continue_input
      show_single_key
      check_char_collector
    end
  end

  def read_char
    $stdin.echo = false
    $stdin.raw!

    input = $stdin.getc.chr
    if input == "\e"
      begin
        input << $stdin.read_nonblock(3)
      rescue StandardError
        nil
      end
      begin
        input << $stdin.read_nonblock(2)
      rescue StandardError
        nil
      end
    end
  ensure
    $stdin.echo = true
    $stdin.cooked!

    return input
  end

  def show_single_key
    char = read_char
    # puts "char: #{char}, @char_collector: #{@char_collector}"
    if KEYBOARD_MAP[char].nil?
      @char_collector += char.upcase
      print char.upcase
    else
      @char_collector += KEYBOARD_MAP[char]
      print KEYBOARD_MAP[char]
    end
  end

  def check_char_collector
    if /(⇧⇧⇩⇩⇦⇨⇦⇨BA)/.match?(@char_collector)
      puts "\nKonami Code!!"
      @continue_input = false
    end

    if /(EscEsc)|(\u0003)/.match?(@char_collector)
      puts "\nExiting"
      @continue_input = false
    end
  end
end

KeyboardReader.new.start
