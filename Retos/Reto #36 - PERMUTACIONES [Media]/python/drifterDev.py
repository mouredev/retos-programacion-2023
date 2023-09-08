def unir_permutaciones(permutaciones:list[str])->str:
   return ", ".join(permutaciones)


def generar_permutaciones(palabra:str)->str:
    permutaciones=[]
    if len(palabra)==1:
       return [palabra]
    elif len(palabra)==2:
       return [palabra, palabra[::-1]]
    else:
         for i in range(len(palabra)):
            for x in generar_permutaciones(palabra[:i]+palabra[i+1:]):
                permutaciones.append(palabra[i]+x)
    return permutaciones


def main():
  # Como el algoritmo es O(n!) es recomendable testear con palabras de 7 caracteres o menos
  print(unir_permutaciones(generar_permutaciones("sol")))
  print(unir_permutaciones(generar_permutaciones("gato")))
  print(unir_permutaciones(generar_permutaciones("pedro")))


if __name__=="__main__":
  main()
