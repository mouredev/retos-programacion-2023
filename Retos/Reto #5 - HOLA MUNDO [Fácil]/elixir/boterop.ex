defmodule Reto5.Boterop do
  def hi(name), do: IO.inspect("Hola #{name}!")
end

Reto5.Boterop.hi("Mundo")
