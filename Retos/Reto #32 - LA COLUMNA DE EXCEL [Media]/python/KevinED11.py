

def column_name_to_number(column_name: str) -> int:
    result = 0
    for i in range(len(column_name)):
        char_value = ord(column_name[i]) - ord('A') + 1
        result = result * 26 + char_value
    return result


if __name__ == "__main__":
  print(column_name_to_number("A"))   # Debería imprimir 1
  print(column_name_to_number("Z"))   # Debería imprimir 26
  print(column_name_to_number("AA"))  # Debería imprimir 27
  print(column_name_to_number("CA"))  # Debería imprimir 79
