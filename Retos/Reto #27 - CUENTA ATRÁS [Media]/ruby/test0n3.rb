# frozen_string_literal: true

# Class for counting down
class CountDown
  attr_reader :start, :shift

  def initialize(start, shift)
    @start_point = start
    @shift = shift
  end

  def start_countdown
    if @start_point < 1 || @shift < 1
      puts 'Invalid Input'
      return 0
    end

    # final_time = Time.now.to_i + (@start_point * @shift)
    # current_time = Time.now.to_i
    # until current_time > final_time
    #   next unless Time.now.to_i == current_time

    #   puts @start_point
    #   @start_point -= 1
    #   current_time += shift
    # end

    while @start_point >= 0
      puts @start_point
      sleep @shift unless @start_point.zero?
      @start_point -= 1
    end
  end
end

CountDown.new(5, 3).start_countdown
CountDown.new(5, -1).start_countdown
CountDown.new(-4, 3).start_countdown
CountDown.new(0, 3).start_countdown
CountDown.new(3, 10).start_countdown
