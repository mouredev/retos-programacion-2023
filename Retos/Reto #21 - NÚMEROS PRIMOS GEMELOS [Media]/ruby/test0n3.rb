# frozen_string_literal: true

# class for Prime Numbers
class PrimeNumber
  def initialize(limit)
    @limit = limit
  end

  def twin_primes
    temp = []
    twin_primes = []
    return "#{@limit} is not valid input" if !(@limit.is_a? Integer) || (@limit < 2)

    (2..@limit).to_a.each do |number|
      next unless prime?(number)

      temp.push(number)
      next unless temp.size == 2

      a, b = temp
      twin_primes.push([a, b]) if b - a == 2
      temp.shift
    end
    twin_primes
  end

  private

  def prime?(number)
    limit = Integer.sqrt(number)
    limit = number - 1 if limit <= 2
    (2..limit).none? { |divisor| (number % divisor).zero? }
  end
end

# puts "twin_primes: #{PrimeNumber.new(30).twin_primes}"
