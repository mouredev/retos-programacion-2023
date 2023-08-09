
'''
 Crea una función que calcule el número de la columna de una hoja de Excel
 teniendo en cuenta su nombre.
 - Las columnas se designan por letras de la "A" a la "Z" de forma infinita.
 - Ejemplos: A = 1, Z = 26, AA = 27, CA = 79.
'''

def calculate_excel_colum(col_num: int) -> str:
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 
                'H', 'I', 'J', 'K', 'L', 'M', 'N', 
                'O', 'P', 'Q', 'R', 'S', 'T', 'U', 
                'V', 'W', 'X', 'Y', 'Z']
    
    column = ''
    
    #while col_num > 0:
    while True:
        div = (col_num - 1) // len(alphabet)
        mod = (col_num - 1) % len(alphabet)
        
        column = alphabet[mod] + column
        
        if div == 0:
            break
        else:
            col_num = div
    
    return column
    

print('4      => ', calculate_excel_colum(4)) #D
print('29     => ', calculate_excel_colum(29)) #AC
print('53     => ', calculate_excel_colum(53)) #BA
print('702    => ', calculate_excel_colum(702)) #ZZ
print('703    => ', calculate_excel_colum(703)) #AAA
print('18981  => ', calculate_excel_colum(18981)) #ABBA