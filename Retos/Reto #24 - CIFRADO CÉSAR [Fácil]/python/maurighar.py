alfabeto_normal = 'abcdefghijklmnopqrstuvwxyz 1234567890'

def encode_cesar(message:str, shift:int) -> str:
    message = message.lower()
    message_cifer = ''
    for string in message:
        index = alfabeto_normal.find(string)
        if index >= 0:
            message_cifer += alfabeto_normal[index + shift]
        else:
            message_cifer += '#'

    return message_cifer

def decode_cesar(message:str, shift:int) -> str:
    message = message.lower()
    message_clear = ''
    for string in message:
        index = alfabeto_normal.find(string)
        if index >= 0:
            message_clear += alfabeto_normal[index - shift]
        else:
            message_clear += '#'

    return message_clear

if __name__ == "__main__":
    mensaje = 'te recomiendo que busques informacion para conocer en profundidad'
    mensaje = 'prueba 234, si (?/7Ú\),\n MAYUSCULAS'
    print(encode_cesar(mensaje, 3))

    mensaje = 'wh3uhfrplhqgr3txh3exvtxhv3lqirupdflrq3sdud3frqrfhu3hq3surixqglgdg'
    mensaje = 'suxhed3567#3vl3###0####3pd1xvfxodv'
    print(decode_cesar(mensaje, 3))
