"""
/*
 * Crea un programa que analice texto y obtenga:
 * - Número total de palabras.
 * - Longitud media de las palabras.
 * - Número de oraciones del texto (cada vez que aparecen un punto).
 * - Encuentre la palabra más larga.
 *
 * Todo esto utilizando un único bucle.
 */
"""
import re

def analyze_text(text: str):
    words = []
    sentences = 0
    longest = {0: ""}
    aux = ""
    nwords = 0
    length = 0

    for letter in text:
        if re.search(r"[?.!]+", letter):
            sentences += 1
            words.append(aux)
            length += len(aux)
            nwords += 1
            
            if len(aux) > list(longest.keys())[0]:
                longest = {
                    len(aux): [aux]
                }
            elif len(aux) == list(longest.keys())[0]:
                longest[len(aux)].append(aux)
            aux = ""
        elif letter == " ":
            if aux != "":
                words.append(aux)
                length += len(aux)
                nwords += 1
                
                if len(aux) > list(longest.keys())[0]:
                    longest = {
                        len(aux): [aux]
                    }
                elif len(aux) == list(longest.keys())[0]:
                    longest[len(aux)].append(aux)
                else:
                    pass
                
                aux = ""
        elif re.search(r"[¿|:()/@%$,]+", letter):
            pass
        else:
            aux = aux + letter
    
    average = round(length/nwords, 2)

    print(f"> Total Words = {nwords}")
    print(f"> Average length = {average}")
    print(f"> Number of senteces = {sentences}")
    print(f"> Longest word/words ({list(longest.keys())[0]} letters) = {list(longest.values())[0]}")
    print()
  

text = (
    "Hello."
    "World!"
)
analyze_text(text)

text = (
    "Crea un programa que analice texto y obtenga:."
    "Número total de palabras."
    "Longitud media de las palabras."
    "Número de oraciones del texto (cada vez que aparecen un punto)."
    "Encuentre la palabra más larga."
    "Todo esto utilizando un único bucle."
)
analyze_text(text)

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis condimentum mauris non enim mollis dictum. In " \
       "feugiat ut justo in vulputate. Aliquam erat volutpat. Vivamus porttitor commodo felis, sed gravida eros " \
       "fermentum non. Mauris sagittis id neque sit amet ullamcorper. Sed eu pretium ex, ut ornare quam. Maecenas " \
       "consectetur elit a nisi maximus, et vehicula lorem finibus. Duis sapien justo, placerat in vestibulum a, " \
       "vestibulum non lacus. Sed egestas, nisi."

analyze_text(text)