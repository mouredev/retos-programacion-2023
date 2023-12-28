(1..100).map do |número|
  next 'fizzbuzz' if número % 15 == 0
  next 'fizz'     if número % 3 == 0
  next 'buzz'     if número % 5 == 0

  número
end.each do |número|
  puts número
end
