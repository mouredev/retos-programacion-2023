for i=1,100 do
  if i % 3 == 0 and i % 5 == 0 then
    print("fizzbuzz")
  elseif i % 3 == 0 then
      print("fizz")
  elseif i % 5 == 0 then
      print("buzz")
  else
    print(i)
  end
end