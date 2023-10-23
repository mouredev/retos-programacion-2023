from string import ascii_uppercase


def excel_column(column: str) -> int:
    result = ascii_uppercase.find(column[-1]) + 1
    if len(column) == 1:
        return result
    for i, chr in enumerate(column[::-1]):
        result += 26 * i * (ascii_uppercase.find(chr) + 1)
    return result


print(excel_column("A"))
print(excel_column("Z"))
print(excel_column("AA"))
print(excel_column("CA"))
print(excel_column("FE"))
print(excel_column("RF"))
