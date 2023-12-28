import re


def split_list_by(value: int, list_of_words: list) -> list:
    if not isinstance(value, int) or value <= 0:
        raise ValueError("value must be a positive integer")
    if not isinstance(list_of_words, list):
        raise ValueError("list_of_words must be a list")

    temp_list = list()
    for i in range(0, len(list_of_words), value):
        temp_list.append(list_of_words[i : i + value])
    return temp_list


def mathematical_expression(expression: str) -> bool:
    if not isinstance(expression, str) or not len(expression):
        return False

    list_of_words = re.findall(r"\S+|\s", expression)

    if len(list_of_words) < 5:
        return False

    number_pattern = r"^[-+]?(\d+|\d+(\.\d+)?)$"
    operator_pattern = r"^[-+*/%]$"

    split_list = split_list_by(4, list_of_words)
    filtered_array = [row for row in split_list if len(row) == 4]

    for row in filtered_array:
        for i in range(0, len(row), 2):
            if (
                not re.match(number_pattern, row[0])
                or not re.match(operator_pattern, row[2])
                or row[i + 1] != " "
            ):
                return False

    last_item = split_list[-1]
    if len(last_item) == 1 and re.match(number_pattern, last_item[0]):
        return True
    return False


""" 
expression = "+5 + 6 / 7 - 4"  # -> True
expression = "+ 5 + 6 / 7 - 4"  # -> False
expression = "5 + 6 / 7 - -4 / -2"  # -> True
expression = "  5 +  6 / 7 -  4  "  # -> False
expression = "-5 + 6 / 7 - 4"  # -> True

 """
expression = "5 + 6 / 7 - -4 / -2"

print(mathematical_expression(expression))

while True:
    expression = input("Expression: ")
    print(mathematical_expression(expression))
