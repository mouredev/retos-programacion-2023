# frozen_string_literal: true

# class TriForce
class TriForce
  TRIFORCE = { head: '*', body: '***' }.freeze
  def initialize(input)
    @nro_row = input
    @padding = (@nro_row * 4 - 1) / 2
    @iter = 1
    @triforce = ''
  end

  def draw_triforce
    @nro_row.times do
      print_heads
      print_tails
    end
    @triforce
  end

  def print_heads
    @triforce += ' ' * @padding
    @iter.times do
      @triforce += '*   '
    end
    @triforce += "\n"
    @padding -= 1
  end

  def print_tails
    @triforce += ' ' * @padding
    @iter.times do
      @triforce += '*** '
    end
    @triforce += "\n"
    @iter += 1
    @padding -= 1
  end
end

# puts TriForce.new(2).draw_triforce
