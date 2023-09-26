import re

def text_processor(text: str) -> str:
    list_text = text.split()
    word_counter = 0
    word_length = []
    sentence_count = 0
    for word in list_text:
        word_counter += 1
        word_length.append(len(re.findall("(\\w+)", word)[0]))
        if "." in word:
            sentence_count += 1

    return f"""Número total de palabras: {word_counter}
Longitud media de las palabras: {sum(word_length)/word_counter}
Número de oraciones del texto: {sentence_count}
La palabra más larga: {list_text[word_length.index(max(word_length))]}"""

if __name__ == "__main__":
    text_to_process = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut 
labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex
ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla 
pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui oficia deserunt mollit anim id est 
laborum."""
    print(text_processor(text_to_process))