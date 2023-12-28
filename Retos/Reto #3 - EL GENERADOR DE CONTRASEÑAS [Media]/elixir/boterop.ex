defmodule Reto3.Boterop do
  @type password :: String.t()
  @type size :: integer()
  @type capital? :: boolean()
  @type number? :: boolean()
  @type symbols? :: boolean()
  @type configurable :: [
          size: size(),
          capital?: capital?(),
          number?: number?(),
          symbols?: symbols?()
        ]

  @letters_range 97..122
  @capital_range 65..90
  @number_range 48..57
  @symbols_range 35..64

  @spec gen_password(config :: configurable()) :: {:ok, password()}
  def gen_password(size, args \\ [], result \\ [])

  def gen_password(size, _opts, result) when length(result) >= size,
    do: {:ok, List.to_string(result)}

  def gen_password(size, args, result) do
    capital? = Keyword.get(args, :capitals, false)
    number? = Keyword.get(args, :numbers, false)
    symbols? = Keyword.get(args, :symbols, false)

    # option = 0: size, 1: capital, 2: number, 3: symbol
    option = random(0..3)

    new_character =
      cond do
        option == 0 -> gen_letter()
        option == 1 && capital? -> gen_capital()
        option == 2 && number? -> gen_number()
        option == 3 && symbols? -> gen_symbol()
      end

    gen_password(size, args, result ++ [new_character])
  end

  defp gen_letter() do
    @letters_range
    |> random()
    |> (&<<&1::utf8>>).()
  end

  defp gen_capital() do
    @capital_range
    |> random()
    |> (&<<&1::utf8>>).()
  end

  defp gen_number() do
    @number_range
    |> random()
    |> (&<<&1::utf8>>).()
  end

  defp gen_symbol() do
    with result_number <- random(@symbols_range),
         false <- result_number in @letters_range,
         false <- result_number in @capital_range,
         false <- result_number in @number_range do
      <<result_number::utf8>>
    else
      true -> gen_symbol()
    end
  end

  defp random(range), do: Enum.random(range)
end

Reto3.Boterop.gen_password(100, capitals: true, numbers: true, symbols: true)
|> IO.inspect()
