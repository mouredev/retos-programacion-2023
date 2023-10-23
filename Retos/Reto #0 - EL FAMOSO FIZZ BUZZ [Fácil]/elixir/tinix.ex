defmodule FizzBuzz do
  def fizzbuzz(n) when rem(n, 3) == 0 and rem(n, 5) == 0, do: "fizzbuzz"
  def fizzbuzz(n) when rem(n, 3) == 0, do: "fizz"
  def fizzbuzz(n) when rem(n, 5) == 0, do: "buzz"
  def fizzbuzz(n), do: Integer.to_string(n)
end

1..100
  |> Enum.map(&FizzBuzz.fizzbuzz/1)
  |> Enum.each(&IO.puts/1)
