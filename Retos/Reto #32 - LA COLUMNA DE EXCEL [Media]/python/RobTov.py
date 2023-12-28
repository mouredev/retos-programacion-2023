def excel_column(col: str) -> int:
    result = 0
    for c in [ord(cc) - 64 for cc in col]:
        result = result * 26 + c
    return result


if __name__ == '__main__':
    print(excel_column('A'))
    print(excel_column('Z'))
    print(excel_column('AA'))
    print(excel_column('CA'))
    print(excel_column('ZZA'))
