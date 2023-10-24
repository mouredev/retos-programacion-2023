def get_table(number: int) -> list:
    result = []
    for i in range(0, 10):
        result.append((i+1)*number)

    return result

def request_input() -> int:
    try:
        number = int(input('Enter an integer to write the multiplication table: '))
        return number
    except ValueError:
        print('Not integer value detected...')

    return number

def print_table(number: int):
    table = get_table(number)
    for idx, value in enumerate(table):
        print(f"{number} x {idx + 1} = {value}")

number = request_input()
print_table(number)
