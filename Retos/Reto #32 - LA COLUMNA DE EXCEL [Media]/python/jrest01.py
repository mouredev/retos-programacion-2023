import string

def number_for_excel_column(column):
    list_alphabet = (list(string.ascii_uppercase))
    column = column.upper()
    
    column_number = 0
    
    for i in column:
        value = list_alphabet.index(i) + 1
        column_number = column_number * 26 + value
    return column_number
        
    
    
if __name__ == '__main__':
    print(number_for_excel_column('ca'))
    #  * - Ejemplos: A = 1, Z = 26, AA = 27, CA = 79.