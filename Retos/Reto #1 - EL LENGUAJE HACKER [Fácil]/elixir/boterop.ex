defmodule Reto1.Boterop do
  @type text :: String.t()

  @dictionary [
    a: "4",
    b: "I3",
    c: "[",
    d: ")",
    e: "3",
    f: "|=",
    g: "&",
    h: "#",
    i: "1",
    j: ",_|",
    k: ">|",
    l: "1",
    m: "/\\/\\",
    n: "^/",
    o: "0",
    p: "|*",
    q: "(_,)",
    r: "I2",
    s: "5",
    t: "7",
    u: "(_)",
    v: "\\/",
    w: "\\/\\/",
    x: "><",
    y: "j",
    z: "2",
    "1": "L",
    "2": "R",
    "3": "E",
    "4": "A",
    "5": "S",
    "6": "b",
    "7": "T",
    "8": "B",
    "9": "g",
    "0": "o"
  ]

  @spec translate(text :: text()) :: text()
  def translate(text) do
    dictionary_map = list_to_map(@dictionary)

    text
    |> String.downcase()
    |> String.graphemes()
    |> Enum.map(fn letter -> letter |> String.to_atom() |> convert(dictionary_map) end)
    |> List.to_string()
  end

  defp list_to_map(list),
    do: Enum.into(list, %{}, fn {key, value} -> {key, value} end)

  defp convert(letter, dictionary) when is_map_key(dictionary, letter),
    do: Keyword.get(@dictionary, letter)

  defp convert(not_translatable, _dictionary), do: Atom.to_string(not_translatable)
end

"Esto es 1 prueba para verificar QUE convierte con éxito a hacker, tambien numeros del 0 al 9 como son (1234567890)"
|> Reto1.Boterop.translate()
|> IO.inspect()
