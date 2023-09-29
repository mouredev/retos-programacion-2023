def diff(str1, str2);
  arr = []
  return "Different length" if str1.size != str2.size
  for n in 0..str1.size - 1
    arr << str2.chars[n] if str1.chars[n] != str2[n]
  end
  arr
end

p diff("Me llamo mouredev", "Me llemo mouredov")
