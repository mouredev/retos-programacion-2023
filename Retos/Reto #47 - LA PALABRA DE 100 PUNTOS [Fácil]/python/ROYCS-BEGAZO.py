import string
abcd = list(string.ascii_lowercase)
abcd.insert(14,'ñ')
d_abcd = {letter:i for i,letter in enumerate(abcd,1)}
def word_value(word:str) -> int:
    return sum([d_abcd[n] for n in word])

while True:
    try:
        word = input('ingrese una palabra ').lower()
        if not all(c in d_abcd for c in word):
            raise Exception('ingrese solo letras validas')
        value = word_value(word)
        print(value)
        if value == 100:
            print('Has introducido una palabra de 100 puntos! El programa finalizará.')
            break
    except Exception as e:
        print(f'ocurrio un error :{e}, trate de nuevo')