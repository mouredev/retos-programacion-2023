import string

def caesar_cypher_decypher(text, _type, movement, num_positions, alphabet_list):
    
    text_list = text.lower().split(" ")   
    new_alphabet_list = []
    magic_num = 0
    
    if movement == "R":
        if _type == "cypher":
            magic_num = num_positions
        else:
            magic_num = -1 * num_positions
    elif movement == "L":
        if _type == "cypher":
            magic_num = -1 * num_positions
        else:
            magic_num = num_positions
        
    #for num, c in enumerate(alphabet):
    #    new_alphabet_list = alphabet[num + magic_num]
    
    for word in text_list:
        new_word_list = [] 
        for elem in word:     
            source_idx = alphabet_list.index(elem)
            dest_idx = (source_idx + magic_num) % 27
            new_word_list.append(alphabet_list[dest_idx])
        new_alphabet_list.append("".join(c for c in new_word_list))
        
    edited_text = " ".join(c for c in new_alphabet_list)
    return edited_text
     
if __name__ == "__main__":
    
    alphabet = string.ascii_lowercase
    alphabet_list = list(alphabet)
    #print(alphabet)
    text = "HELLO WORLD"
    movement = "R"
    num_positions = 2
    _type = "cypher"
    cyphered_text = caesar_cypher_decypher(
        text, _type, movement, num_positions, alphabet_list)
    print(cyphered_text)
    _type = "decypher"
    decyphered_text = caesar_cypher_decypher(
        cyphered_text, _type, movement, num_positions, alphabet_list)
    print(decyphered_text)

