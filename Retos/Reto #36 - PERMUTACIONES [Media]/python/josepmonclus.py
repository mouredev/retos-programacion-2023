'''
Crea un programa que sea capaz de generar e imprimir todas las 
permutaciones disponibles formadas por las letras de una palabra.
- Las palabras generadas no tienen por qué existir.
- Deben usarse todas las letras en cada permutación.
- Ejemplo: sol, slo, ols, osl, los, lso 
'''

def do_permute(permutes_list, permuted, to_permute):
    if len(to_permute) == 1:
        permutes_list.append(permuted + to_permute)
    else:
        for pos in range(0, len(to_permute)):
            # print(to_permute[pos], ' ', to_permute[:pos] + to_permute[pos + 1:])
            do_permute(permutes_list, permuted + to_permute[pos], to_permute[:pos] + to_permute[pos + 1:])
    
        
def get_permutes(word: str):
    if len(word) > 0:
        permutes_list = []
                
        do_permute(permutes_list, '', word)
            
        print('Permutaciones de la palabra: ', word) 
        print(permutes_list)
        
        print('Sin repeticiones: ')
        print(list(set(permutes_list)))
    else:
        print('La palabra a permutar tiene que contener una letra como mínimo')
    
get_permutes('sol')
get_permutes('moure')
get_permutes('')