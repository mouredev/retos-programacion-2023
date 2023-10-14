def print_mult_table(num: int):
    if num < 1 or num > 10:
        raise ValueError("Introduce a number between 1 and 10")
    
    print("\n".join([f"{num} x {n} = {num * n}" for n in range(1, 11)]))


if __name__ == "__main__":
    num = int(input("Input a number: "))
    print_mult_table(num)