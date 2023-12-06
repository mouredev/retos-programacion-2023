def infiltrado(texto1:str,texto2:str):
    infiltrados=[]
    if len(texto1) == len(texto2):
      for tupla in zip(texto1,texto2):
          if tupla[0] != tupla[1]:
              infiltrados.append(tupla[0])
    else:
        return print('Los textos no tienen el mismo tamaño')
    return print(infiltrados)

infiltrado('abc','abdc')
infiltrado('Me llamo mouredev','Me llemo mouredov')
infiltrado('Me llamo.Brais Moure','Me llamo brais moure')