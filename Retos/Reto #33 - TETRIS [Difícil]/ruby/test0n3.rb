#
# Crea un programa capaz de gestionar una pieza de Tetris.
# - La pantalla de juego tiene 10 filas y 10 columnas representadas por símbolos 🔲
# - La pieza de tetris a manejar será la siguiente (si quieres, puedes elegir otra):
#   🔳
#   🔳🔳🔳
# - La pieza aparecerá por primera vez en la parte superior izquierda de la pantalla de juego.
#   🔳🔲🔲🔲🔲🔲🔲🔲🔲🔲
#   🔳🔳🔳🔲🔲🔲🔲🔲🔲🔲
#   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
#   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
#   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
#   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
#   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
#   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
#   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
#   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
# - Debes desarrollar una función capaz de desplazar y rotar la pieza en el tablero,
#   recibiendo una acción cada vez que se llame, mostrando cómo se visualiza en la pantalla de juego.
# - Las acciones que se pueden aplicar a la pieza son: derecha, izquierda, abajo, rotar.
# - Debes tener en cuenta los límites de la pantalla de juego.

# frozen_string_literal: true

require 'io/console'

# Class Tetris
class Tetris
  BOARD_ICONS = { 0 => '🔲', 1 => '🔳' }.freeze
  KEYBOARD_MAP = { ' ' => 'rotate', "\e[B" => 'down', "\e[C" => 'right',
                   "\e[D" => 'left', "\e" => 'Esc' }.freeze

  def initialize
    @board = Array.new(10) { Array.new(10, 0) }
    @pos = [0, 0]
    @figure = Figure.new
    @continue_input = true
    @user_input = ''
  end

  def play
    while @continue_input
      insert_figure
      draw_board
      read_input
      update_figure
    end
  end

  def draw_board
    @board.each do |row|
      row.each do |piece|
        print BOARD_ICONS[piece]
      end
      print "\n"
    end
  end

  def update_figure
    if @user_input == 'rotate'
      rotate_figure
    else
      move_piece
    end
    puts "@pos:#{@pos}, @continue_input: #{@continue_input}, @user_input: #{@user_input}"
  end

  def move_piece
    @pos = [@pos[0], @pos[1] - 1] if @user_input == 'left' && move_posible?

    @pos = [@pos[0], @pos[1] + 1] if @user_input == 'right' && move_posible?

    @pos = [@pos[0] + 1, @pos[1]] if @user_input == 'down' && move_posible?
  end

  def move_posible?
    return false if @user_input == 'left' && @board.transpose[0].any?(1)
    return false if @user_input == 'right' && @board.transpose[9].any?(1)
    return false if @user_input == 'down' && @board[9].any?(1)

    true
  end

  def rotate_posible?
    return false if @board[9].any?(1)
    return false if @board.transpose[9].any?(1)

    true
  end

  def rotate_figure
    @figure.rotate if rotate_posible?
  end

  def insert_figure
    @board = Array.new(10) { Array.new(10, 0) }
    @figure.figure_matrix.each_with_index do |row, row_index|
      row.each_with_index do |piece, col_index|
        @board[@pos[0] + row_index][@pos[1] + col_index] = piece
      end
    end
  end

  def read_input
    char = read_char
    @user_input = KEYBOARD_MAP[char]
    @continue_input = false if /Esc/.match?(@user_input)
  end

  private

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
end

# class for figure
class Figure
  FIGURES = { 0 => [[1, 0, 0], [1, 1, 1]] }.freeze

  attr_reader :figure
  attr_accessor :figure_matrix

  def initialize(figure = 0)
    @figure_matrix = FIGURES[figure]
    @figure = figure
  end

  def rotate
    @figure_matrix = @figure_matrix.reverse.transpose
  end
end

Tetris.new.play
