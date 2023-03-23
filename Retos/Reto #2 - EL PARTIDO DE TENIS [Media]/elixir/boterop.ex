defmodule Reto2.Boterop do
  @type player :: :p1 | :p2
  @type players_list :: list(player())
  @type status :: :deuce | :win | :ad
  @type score :: integer()
  @type game_result :: status() | [{player(), status()}] | [{player(), score()}]
  @type results :: list(game_result())

  @spec play(list :: players_list()) :: results()
  def play(list, result \\ [])
  def play([], result), do: result

  def play([player | tail], result) do
    result
    |> Kernel.++([update_score(player, result)])
    |> (&play(tail, &1)).()
  end

  defp update_score(player, results) do
    results
    |> List.last()
    |> case do
      [{p, :win}] = result -> result
      [:deuce] -> [{player, :ad}]
      [{p, :ad}] -> get_result(player, p)
      [p1: _score1, p2: _score2] = result -> get_score(player, result)
      nil -> get_score(player, p1: :love, p2: :love)
    end
  end

  defp get_result(player1, player2) when player1 == player2, do: [{player1, :win}]
  defp get_result(_player1, _player2), do: [:deuce]

  defp get_score(:p1, p1: 30, p2: 40), do: [:deuce]
  defp get_score(:p2, p1: 40, p2: 30), do: [:deuce]

  defp get_score(player, result), do: Keyword.update(result, player, 15, &valid_score(&1))

  defp valid_score(:love), do: 15
  defp valid_score(15), do: 30
  defp valid_score(30), do: 40
end

[:p1, :p1, :p2, :p2, :p1, :p2, :p1, :p1]
|> Reto2.Boterop.play()
|> IO.inspect()
