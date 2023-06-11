import random

class Game:
    def __init__(self,word:int,intentos:int):
        self.word: str =word.lower()
        self.intentos: int =intentos
        self.running: bool = True
        self.hidden_characters,self.gameword = self.prepare_word()
        self.print_current_status()

    def prepare_word(self)->tuple:
        index_list_words_to_hide: list =self.get_index_list_to_hide()
        gameword: str=self.word
        hidden_chars:dict = {}
        for i in index_list_words_to_hide:
            if hidden_chars.get(gameword[i]):
                hidden_chars[gameword[i]].append(i)
            else:
                hidden_chars[gameword[i]]=[i]
            gameword = self.replace_character(gameword,i,"_")
        return hidden_chars,gameword
            
    def get_index_list_to_hide(self):
        number_of_character_to_hide: int = len(self.word) * 60 //100
        return random.sample(range(0,len(self.word)),number_of_character_to_hide) 
    
    @staticmethod
    def replace_character(word:str,index:int,new_character:str)->str:
        # new_word:str = word
        # new_word[index]="_"
        # return new_word
        return word[:index] + new_character +word[index+1:]
    
    def test_character(self,text_to_test)->bool or int:
        if index:=self.hidden_characters.get(text_to_test):
            return index.pop()
        return False
    
    def attempt(self,text_to_test)->None:
        if text_to_test == self.word:
            self.gameword = text_to_test
        elif (index:=self.test_character(text_to_test)) is not False:
            self.gameword = self.replace_character(self.gameword,index,text_to_test)
        else:
            print(f"{text_to_test} no se encuentra en la palabra")
            self.intentos -= 1
        self.checked_end()

    def checked_end(self)->None:
        if self.intentos <= 0:
            self.trigger_end(False)
        elif self.word == self.gameword:
            self.trigger_end(True)
        else:
            self.print_current_status()

    def trigger_end(self,win: bool) -> None:
        self.print_current_status()
        text = "ganado" if win else "perdido"
        print(f"Usted ha {text}")
        self.running = False

    def print_current_status(self) -> None:
        print("*"*40)
        print(f"Intentos: {self.intentos}")
        print(f"Palabra: {self.gameword}")

if __name__ == '__main__':
    words = ["software","hardware","cookies","memoria ram","router","malware","backend","frontend"]
    index = random.randint(0,len(words)-1)
    print("*"*40)
    print("Encuentra las letras faltantes en la palabra")
    game = Game(words[index],5)
    while game.running:
        new_char = input().lower()
        game.attempt(new_char)