import string 

def calculate_excel_column(column_name: str):

    for c in column_name:
        if c.isdigit():
            raise ValueError("The two imputs needs to be complete strings without numbers!")  

    #idx_value = ord("A") - 1
    alphabet_list = [c for c in string.ascii_uppercase]
    print(alphabet_list)
    column_pos = 0
    column_name = column_name.upper()
    column_name_prep = column_name[::-1]
     
    for n in range(len(column_name) - 1, - 1, -1):
        if n != 0:
            column_value = ((26 ** n) * (alphabet_list.index(column_name_prep[n]) + 1))
        else:
            column_value = alphabet_list.index(column_name_prep[n]) + 1
        column_pos = column_pos + column_value

    return column_pos

if __name__ == "__main__":
    
    column_name = "AAA"
    column_pos = calculate_excel_column(column_name)
    print(column_pos)