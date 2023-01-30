defmodule Reto4.Boterop do
  def check_number(number) when is_number(number) do
    {_num, result} =
      {number, "#{number} "}
      |> check_prime()
      |> check_fibonacci()
      |> check_even()

    result
  end

  defp is_prime?(2), do: true

  defp is_prime?(number) do
    limit =
      number
      |> :math.sqrt()
      |> Float.ceil()
      |> trunc

    possible_divisors = 2..limit

    !Enum.any?(possible_divisors, fn divisor -> rem(number, divisor) == 0 end)
  end

  defp check_prime({number, text}) do
    result =
      case is_prime?(number) do
        true -> "es primo, "
        false -> "no es primo, "
      end

    {number, text <> result}
  end

  defp fibonacci(0), do: 0
  defp fibonacci(1), do: 1
  defp fibonacci(n), do: fibonacci(n - 1) + fibonacci(n - 2)

  defp is_fibonacci?(number, count \\ 0, result \\ 1)
  defp is_fibonacci?(number, _count, result) when result == number, do: true
  defp is_fibonacci?(number, _count, result) when result > number, do: false

  defp is_fibonacci?(number, count, _result),
    do: is_fibonacci?(number, count + 1, fibonacci(count))

  defp check_fibonacci({number, text}) do
    result =
      case is_fibonacci?(number) do
        true -> "fibonacci "
        false -> "no es fibonacci "
      end

    {number, text <> result}
  end

  defp is_even?(number), do: rem(number, 2) == 0

  defp check_even({number, text}) do
    result =
      case is_even?(number) do
        true -> "y es par"
        false -> "y es impar"
      end

    {number, text <> result}
  end
end

Reto4.Boterop.check_number(2)
|> IO.inspect()

Reto4.Boterop.check_number(7)
|> IO.inspect()
