def per(word):
    permutaciones=[]
    if len(word)==1:
        return [word]
    elif len(word)==2:
        return[word,word[1]+word[0]]    
    else:
        for i in range(len(word)):  #vamos a recorrer cada letra
            for j in per(word[:i]+word[i+1:]):  #cada j será una permutación de la palabra sin la letra i
               permutaciones.append(word[i]+j)  #a cada j le sumamos la letra i 

    return permutaciones


print(per('abcd'))