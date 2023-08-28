
# Variables
name: str = "kevin"
age: int = 22
money_in_the_bank: float = 1.0
married: bool = True

# Constant
PI_VALUE = 3.1416

# Conditionals
if age >= 18:
    print("eres mayor de edad")
else:
    print("eres menor de edad")

if married:
    print("esta casado")
elif not married:
    print("no esta casado")
    
# Structures
names: list = ["kevin", "damian"]
person: dict =  {"name": "kevin", "age": 22}
unique_values: set = {"kevined11", "dani123", "kevined11"}
person_values: tuple = (person.get("name"), person.get("age")) 


# Loops
for value in person_values:
    print(value)

counter = 1
while counter <= 10:
    print(counter)
    counter += 1

# functions
def print_names(names: list) -> None:
    for name in names:
        print(names)

def hello():
    print("hello world")
  
def name1() -> str:
    return "kevin"


# Class
class Person:
    def __init__(self, name, age):
        self.nam = name
        self.age = age
      
# Exceptions
def is_person(person: dict) -> dict:
    if not isinstance(person, dict):
        raise TypeError("solo debes pasar diccionarios")
    
    return person


try:
    is_person(person)
except TypeError as err:
    print(err)
    