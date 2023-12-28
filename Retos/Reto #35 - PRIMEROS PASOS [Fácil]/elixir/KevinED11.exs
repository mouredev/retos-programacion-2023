# Hello World
IO.puts("Hello world from Elixir")

# Variables
name = "kevin"
married = true
age = 22
money = 1.0

# Constants
IO.puts("It doesn't have traditional constants.")

# Structures
list = [1, 2, 3]
IO.puts(list)
tuple = {"hello", "world"}
map = %{:a => 1, 2 => :b}


# Functions
sum = fn (a, b) -> a + b end

def function_name(arg1, arg2) do
  # Code
end

# Loops
for(i = 0; i < 10; i++) {
   IO.puts(i);
}

# Conditionals
if age >= 18 do
  IO.puts("Eres mayor de edad")
else
  IO.puts("Eres menor de edad")
end

if condition1 do
  # código para ejecutar si condition1 es verdadera
elsif condition2 do
  # código para ejecutar si condition2 es verdadera
else
  # código para ejecutar si ninguna de las condiciones anteriores es verdadera
end

cond do
  age >= 18 ->
    IO.puts("Eres mayor de edad")
  age < 18 ->
    IO.puts("Eres menor de edad")
  true ->
    # default case


# Class
IO.puts("Elixir is a functional programming language in which classes as such do not exist, but modules are used instead. Modules serve as containers to group related functions.")


# Exeptions
def divide(a, b) do
  if b === 0 do
    {:error, "Divisor no puede ser cero"}
  else
    {:ok, a / b}
  end
end
