def print_stairs(quantity: int):
    if (quantity == 0):
        print("__")
        return

    blank = " "

    if quantity < 0:
        stair = "|_"
        print("_")

    if quantity > 0:
        stair = "_|"
        print(f"{blank*(quantity * 2)}_")

    counter = 1
    while counter <= abs(quantity):
        spaces = blank * (counter * 2 - 1) if quantity < 0 else blank * (
            (quantity - counter) * 2
        )
        print(f"{spaces}{stair}")
        counter += 1


print_stairs(0)
print_stairs(-5)
print_stairs(5)
