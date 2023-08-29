import string

def test_string(text):
    
    text = text.lower()
    
    def count_words(text):
        count_dict = dict()
        is_heterogram = True
        for c in text:
            if c in list(string.ascii_lowercase):
                if count_dict.get(c):
                    count_dict[c] = count_dict[c] + 1
                    is_heterogram = False
                else:
                    count_dict[c] = 1
        return count_dict, is_heterogram
             
    def heterogram(text):
        _, is_heterogram = count_words(text)
        return is_heterogram
    
    def isogram(text):
        count_dict, _ = count_words(text)
        master_val = 0
        is_isogram = True
        for iter, val in enumerate(count_dict.values()):
            if iter == 0:
                master_val = val
            else:
                if val != master_val:
                    is_isogram = False
                    break
        return is_isogram 
            
    def pangram(text):
        is_pangram = False
        count_dict, _ = count_words(text)
        text_list = list(count_dict.keys())
        text_list.sort()
        alphabet_list = list(string.ascii_lowercase)
        if text_list == alphabet_list:
            is_pangram = True
        return is_pangram
        
    return heterogram(text),  isogram(text), pangram(text)
                                              
if __name__ == "__main__":

    text = "supercalifragilisticoespialidoso"
    hete, iso, pan = test_string(text)
    print(f"The string {text}\n- heterogram: {hete}\n- isogram: {iso}\n- pangram: {pan}") 