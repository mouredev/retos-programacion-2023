import re

# ! Coded by Garkatron
# ! https://github.com/Garkatron

# ? -------------------------------------------------------------------------------------- ? #

# * Crea un programa que analice texto y obtenga:
# ! Número total de palabras. V
# ! Longitud media de las palabras. V
# ! Número de oraciones del texto (cada vez que aparecen un punto). V
# ! Encuentre la palabra más larga. V
# Todo esto utilizando un único bucle.

# ? -------------------------------------------------------------------------------------- ? #

# ! Functions

def get_words(text:str)->[]:
    words=re.split(r'[\s,;.:]+',text)
    return words

def max_length_word(words:list)->int:
    return max(words, key=lambda v: len(v))

def get_sentences(text:str)->int:
    return text.split(".")

def word_mean(words:list)->int:
    return sum(map(lambda w: len(w),words))/len(words)


# ! To execute

if __name__=="__main__":
    
    # ! Getting the values
    text=input("Insert text: ")
    words=get_words(text)
    words_count=len(words)
    mean_word_lenght=word_mean(words)
    sentences=get_sentences(text)
    sentences_number=len(sentences)
    max_length_word=max_length_word(words)
    
    # ! Printing values
    print("----------------------------------------")
    print("Analisyng text: ", text)
    print("----------------------------------------", "\n")
    
    print("Words: ", words)
    print("Words count: ", words_count)
    print("Max length word: ", max_length_word)
    print("Mean word length: " ,mean_word_lenght, "\n")
    
    print("Sentences: ", sentences)
    print("Sentences count: ", sentences_number, "\n")
