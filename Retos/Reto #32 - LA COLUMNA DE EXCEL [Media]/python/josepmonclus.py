
'''
 Crea una función que calcule el número de la columna de una hoja de Excel
 teniendo en cuenta su nombre.
 - Las columnas se designan por letras de la "A" a la "Z" de forma infinita.
 - Ejemplos: A = 1, Z = 26, AA = 27, CA = 79.
'''

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 
                'H', 'I', 'J', 'K', 'L', 'M', 'N', 
                'O', 'P', 'Q', 'R', 'S', 'T', 'U', 
                'V', 'W', 'X', 'Y', 'Z']

def calculate_excel_colum(col_num: int) -> str:    
    column = ''
    
    while True:
        div = (col_num - 1) // len(alphabet)
        mod = (col_num - 1) % len(alphabet)
        
        column = alphabet[mod] + column
        
        if div == 0:
            break
        else:
            col_num = div
    
    return column

def calculate_col_num(column: str) -> int:
    col_num = 0
    
    for i in range(len(column) -1, -1, -1):
        pos = alphabet.index(column[i]) + 1
        col_num += pos * (26 ** (len(column) - 1 - i))
    
    return col_num
    
# leí mal el enunciado, inicialmente lo hice de número a letras (xD)
print('4      => ', calculate_excel_colum(4))       # D
print('29     => ', calculate_excel_colum(29))      # AC
print('53     => ', calculate_excel_colum(53))      # BA
print('702    => ', calculate_excel_colum(702))     # ZZ
print('703    => ', calculate_excel_colum(703))     # AAA
print('18981  => ', calculate_excel_colum(18981))   # ABBA

print('-------------------------')

# casos de prueba de letras a número (lo que realmente pide el enunciado)
print('A      => ', calculate_col_num('A'))         #1
print('AC     => ', calculate_col_num('AC'))        # 29
print('BA     => ', calculate_col_num('BA'))    # 53
print('ZZ     => ', calculate_col_num('ZZ'))    # 702
print('AAA    => ', calculate_col_num('AAA'))   # 703
print('ABBA   => ', calculate_col_num('ABBA'))  # 18981