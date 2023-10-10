def diff_chars(first_text: str, second_text: str):
    
    if not isinstance(first_text, str) or not isinstance(second_text, str):
        raise ValueError("We need only strings!")
    
    if len(first_text) != len(second_text):
        raise ValueError("The  two text needs to have the same length!")  
    
    error_list = []
    
    for c1, c2 in zip(first_text, second_text):
        if c1 != c2:
            error_list.append((c1, c2))
        #print(c1, c2)  
    
    return error_list
                                              
if __name__ == "__main__":

    first_text = "Me llamo.Brais Moure"
    second_text = "Me llamo brais moure"
    result_list = diff_chars(first_text, second_text)
    print(result_list)