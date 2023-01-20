print('*************************************')
print(' CODIFICAR FRASES AL LENGUAJE HACKER ')
print('*************************************')

frase = input('\nBienvenido\nPorfavor escribe una frase para codificarla\n\n').lower()

# Creacion de diccionario: 2 listas, crear tuplas, volverlas diccionario
normal_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
leet_letters = ['4','I3','[',')','3','|=','&','#','!',',_|','>|','1','|V|','^/','0','|*','(_,)','|2','5','7','(_)','\/','\/\/','><','j','2']
code_dict = dict(zip(normal_letters.lower(), leet_letters))

# Recorrer cada llave del diccionario y reemplazar en valor por el correspondiente en la lista leet_letters
for letter in code_dict.keys():
    frase = frase.replace(letter, code_dict[letter])


print(f'\nLa Nueva frase es:\n\n{frase}\n')
