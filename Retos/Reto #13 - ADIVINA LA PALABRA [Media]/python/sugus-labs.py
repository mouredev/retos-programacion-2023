import random
import math

def guess_the_word(word_list):
    
    num_guesses = 3
    
    def select_and_hide_the_word(word_list):
        
        selected_word = random.choice(word_list).lower()
        hidden_word_list = list(selected_word)
        selected_word = list(selected_word)
        num_chars = len(selected_word)
        num_hidden_chars = math.floor(0.6 * num_chars) 
        pos_list = [x for x in range(0, num_chars)]
        #print(selected_word, hidden_word, num_chars, 
        #    num_hidden_chars, pos_list)
        for pos in range(0, num_hidden_chars):
            selected_pos = random.choice(pos_list)
            pos_list.remove(selected_pos)
            hidden_word_list[selected_pos] = "_"
               
        return selected_word, hidden_word_list
    
    selected_word, hidden_word_list = select_and_hide_the_word(word_list)
    
    def check_input_and_rewrite_the_word(
        selected_word, hidden_word_list, num_guesses):
        
        is_winner = False
        
        while num_guesses > 0:
            if "_" in hidden_word_list:
                guess_word = input(f"Try to guess one character or the complete word! You have {hidden_word_list}")
                guess_word = guess_word.lower()
                if len(guess_word) == 1:
                    print(f"You selected the character: {guess_word}")
                    if (guess_word in selected_word):
                        idx_list = []
                        for num, elem in enumerate(selected_word):
                            if elem == guess_word:
                                idx_list.append(num)
                        for idx in idx_list:
                            hidden_word_list[idx] = guess_word
                        print(f"You guess! Now you have this: {hidden_word_list}")
                    else:
                        num_guesses = num_guesses - 1                      
                else:
                    print(f"You think that the word to guess is: {guess_word}")   
                    if list(guess_word) == selected_word:
                        is_winner = True
                        break
                    else:
                        print(f"The word is not: {guess_word}")  
                        num_guesses = num_guesses - 1          
            else:
                break                   
            if num_guesses == 0:
                print(f"You LOST!. The word was: {selected_word}")
                break   
                
        if is_winner == True:
            print(f"You WIN!. The word was: {selected_word}")   
        
        #return
    
    check_input_and_rewrite_the_word(
        selected_word, hidden_word_list, num_guesses)
            
    return selected_word, hidden_word_list

                                              
if __name__ == "__main__":

    word_list = [
        "sugus", "mouredev", "flinstones"]
    selected_word, hidden_word_list = guess_the_word(word_list)
    #print(f"{dt} is friday?: {is_friday}")
    #print(selected_word, hidden_word_list)