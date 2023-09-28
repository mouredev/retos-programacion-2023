def column(name: str) -> int:
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number = int()
    
    for letter in name:
        number = number * 26 + alphabet.index(letter) + 1
    
    return number


print(column("A"))
print(column("Z"))
print(column("AA"))
print(column("CA"))
print(column("ABC"))
