t9_dict={'1':',','11':'.','111':'?','1111':'!','2':'A','22':'B','222':'C','3':'D','33':'E','333':'F','4':'G','44':'H','444':'I','5':'J','55':'K','555':'L','6':'M','66':'N','666':'O','7':'P','77':'Q','777':'R','7777':'S','8':'T','88':'U','888':'V','9':'W','99':'X','999':'Y','9999':'Z','0':' '}

def convert_to_t9(texto:str):
    texto=texto.split('-')
    text_t9=''
    for bloque in texto:
        if bloque in t9_dict:
          text_t9+=t9_dict[bloque]  
        else:
           return print('Bloque de números no encontrado')
    return print(text_t9)

convert_to_t9('44-666-555-2-0-555-444-66-3-88-777-2-1111')