def cal_column_number(col_name : str) -> int:
    col_num = 0
    for letter in col_name.upper():
        col_num = col_num * 26 + (ord(letter)- ord('A')+1)
    return col_num
print(cal_column_number('zzzz'))