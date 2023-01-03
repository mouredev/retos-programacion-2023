# frozen_string_literal: true

def fizzbuzz
  (1..100).each do |num|
    resp = ''
    resp += num.to_s unless (num % 3).zero? || (num % 5).zero?
    resp += 'fizz' if (num % 3).zero?
    resp += 'buzz' if (num % 5).zero?
    puts resp
  end
end

fizzbuzz
