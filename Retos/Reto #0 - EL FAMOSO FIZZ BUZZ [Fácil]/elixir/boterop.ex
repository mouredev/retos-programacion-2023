defmodule Reto0.Boterop do
  def fizz_buzz(result_list \\ [], number \\ 1)
  def fizz_buzz(result_list, number) when number > 100, do: result_list

  def fizz_buzz(result_list, number) do
    number
    |> solve()
    |> IO.inspect()
    |> (&Kernel.++(result_list, [&1])).()
    |> fizz_buzz(number + 1)
  end

  def solve(number) when rem(number, 3) == 0 and rem(number, 5) == 0, do: "fizzbuzz"
  def solve(number) when rem(number, 3) == 0, do: "fizz"
  def solve(number) when rem(number, 5) == 0, do: "buzz"
  def solve(number), do: number
end

Reto0.Boterop.fizz_buzz()
