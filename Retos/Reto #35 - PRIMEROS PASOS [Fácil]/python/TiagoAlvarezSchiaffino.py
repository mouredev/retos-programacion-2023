# Hello world
print("Hello, Python!")

# Variables
variable_string = "String variable"
variable_integer = 4
variable_float = 8.34
variable_boolean = True

# Constant
CONSTANT = "Still a variable, but uppercase is used as a constant"

# if | else if | else
if variable_boolean:
    print("Its value is true")
elif variable_float > 10:
    print("Its value is greater than 10")
else:
    print("None of the above conditions were met")

# Structures
list_example = [0, 1, 2, "three"]
tuple_example = (0, 1, 2, "two + 1")
set_example = {0, 1, 2, "three"}
dictionary_example = {"key_1": "value_1", "key_2": "value_2"}

# for | foreach | while
for i in range(5):
    print(i)

for element in list_example:
    print(element)

i = 0
while i < 5:
    print(i)
    i += 1

# Functions
def function_with_parameters(param_1: str, param_2: float):
    print(f"You passed: {param_1} and {param_2}")

def function_without_parameters():
    print("You just need to call this function")

def function_with_return(value: int) -> int:
    return value + 1

function_with_parameters("Hello", 3.3)
function_without_parameters()
print(function_with_return(3))

# Classes
class MyClass:
    def __init__(self, identifier: str):
        self.identifier = identifier

    def show_identifier(self):
        print(self.identifier)

MyClass("Mark").show_identifier()

# Exception handling
try:
    print(3 / 0)
except ZeroDivisionError:
    print("Cannot divide by 0")
finally:
    print("This part runs with or without an error")
