# frozen_string_literal: true

# class TriForce
class TriForce
  # def initialize(input)
  #   @nro_row = input
  #   @padding = (@nro_row * 4 - 1) / 2
  #   @iter = 1
  #   @triangle = ''
  # end

  # def draw_triangles
  #   @nro_row.times do
  #     print_heads
  #     print_tails
  #   end
  #   @triangle
  # end

  # def print_heads
  #   @triangle += ' ' * @padding
  #   @iter.times do
  #     @triangle += '*   '
  #   end
  #   @triangle += "\n"
  #   @padding -= 1
  # end

  # def print_tails
  #   @triangle += ' ' * @padding
  #   @iter.times do
  #     @triangle += '*** '
  #   end
  #   @triangle += "\n"
  #   @iter += 1
  #   @padding -= 1
  # end

  def initialize(input)
    @nro_rows = input
    @element_width = 2 * @nro_rows - 1
    @max_length = @element_width * 2 + 1
    @external_padding = @max_length / 2
    @triforce = ''
  end

  def draw_triforce
    print_head
    print_base
    @triforce
  end

  def print_head
    @nro_rows.times do |i|
      @triforce += "#{' ' * @external_padding}#{gen_stars(i)}\n"
      @external_padding -= 1
    end
  end

  def print_base
    @nro_rows.times do |i|
      @triforce += "#{' ' * @external_padding}#{gen_stars(i)}#{' ' * @element_width}#{gen_stars(i)}\n"
      @external_padding -= 1
      @element_width -= 2
    end
  end

  private

  def gen_stars(row)
    '*' * (row * 2 + 1)
  end
end

# puts TriForce.new(1).draw_triforce
# puts TriForce.new(2).draw_triforce
# puts TriForce.new(3).draw_triforce
# puts TriForce.new(4).draw_triforce
# puts TriForce.new(5).draw_triforce
