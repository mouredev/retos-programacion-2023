
def fizzbuzz(range)
  (1..range).each do |number|
    if (number % 3).zero? && (number % 5).zero?
      puts 'FizzBuzz'
    elsif (number % 3).zero?
      puts 'fizz'
    elsif (number % 5).zero?
      puts 'buzz'
    else
      puts number
    end
  end
end

fizzbuzz(100)
