from statistics import mean

def analyze_text(text):

    text_list = text.split(" ")
    #print(text_list)
    word_length_list = []
    num_words = 0
    num_sentences = 0
    num_words_longest_word = 0
    longest_word = None
    for word in text_list:
        if word != "\n" and word != "":
            num_words = num_words + 1
            word_length = len(
                word.replace(".", "") \
                    .replace(",", "") \
                    .replace(":", ""))
            word_length_list.append(word_length)
            if word_length > num_words_longest_word:
                longest_word = word.replace(".", "") \
                    .replace(",", "") \
                    .replace(":", "")
                num_words_longest_word = word_length
        if "." in word:
            num_sentences = num_sentences + 1
    mean_length_words = int(mean(word_length_list))
        
    return (
        num_words, mean_length_words,
        num_sentences, longest_word)
    
            
if __name__ == "__main__":
    
    text = """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
        sed do eiusmod tempor incididunt ut labore et dolore magna 
        aliqua. Ut enim ad minim veniam, quis nostrud exercitation 
        ullamco laboris nisi ut aliquip ex ea commodo consequat. 
        Duis aute irure dolor in reprehenderit in voluptate velit 
        esse cillum dolore eu fugiat nulla pariatur. Excepteur sint 
        occaecat cupidatat non proident, sunt in culpa qui officia 
        deserunt mollit anim id est laborum."""
    analytics = analyze_text(text)
    print(text + "\n")
    print(f"""Analytics for the text.
             - Number of words: {analytics[0]}
             - Mean lenght of words: {analytics[1]}
             - Number of sentences: {analytics[2]}
             - Longest word: {analytics[3]}
             """)
