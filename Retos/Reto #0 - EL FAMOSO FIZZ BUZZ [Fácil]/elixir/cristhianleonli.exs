defmodule Main do
    def main() do
        1..100
        |> Enum.to_list()
        |> Enum.map(&fizbuzz/1)
        |> Enum.each(fn x -> IO.puts(x) end )
    end

    defp fizbuzz(number) do
        cond do
            rem(number, 3) == 0 and rem(number, 5) == 0 -> "fizbuzz"
            rem(number, 3) == 0 -> "fizz"
            rem(number, 5) == 0 -> "buzz"
            true -> Integer.to_string(number)
        end
    end
end

Main.main()