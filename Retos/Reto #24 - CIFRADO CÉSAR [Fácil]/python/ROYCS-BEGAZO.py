import string

abcd = {letter:i for i,letter in enumerate(list(string.ascii_lowercase),1)}
abcd_dict_reverso = {i:letter for i,letter in enumerate(list(string.ascii_lowercase),1)}

def cesar_code(txt:str, num:int):
    code_num = [abcd[i] for i in txt]
    return ''.join([abcd_dict_reverso[(n+num) % 27] for n in code_num ])

def cesar_decode(txt:str,num:int):
    code_num = [abcd[i] for i in txt]
    return ''.join([abcd_dict_reverso[(n-num) % 27] for n in code_num ])
