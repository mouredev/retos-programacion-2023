from bs4 import BeautifulSoup
import requests
import re
import string

def download_aurebesh_alphabet():
    url = "https://www.dcode.fr/aurebesh-alphabet"
    body = requests.get(url)
    body_text = body.content
    #print(body)
    #print(body_text)

    clean = re.compile('<.*?>')

    alphabet_dict = dict()

    soup = BeautifulSoup(body_text, 'lxml')
    tbodys = soup.find_all("tbody")
    for tbody in tbodys:
        tds = tbody.find_all("td")
        #real_num = 0
        aurebesh_str = ""
        english_str = ""
        for num, td in enumerate(tds):
            if (num == 0) or (num % 3) == 0 :
                pass
            else:
                #real_num = real_num + 1
                clean_line = re.sub(clean, '', str(td))
                if len(clean_line) <= 2:
                    english_str = clean_line.lower()
                    #print(f"EN: {english_str}")
                    alphabet_dict[english_str] = aurebesh_str
                else:
                    aurebesh_str = clean_line.lower()
                    #print(f"AU: {aurebesh_str}")
    del alphabet_dict[""]
       
    return alphabet_dict     
            
def text_to_aurebesh(text: str, alphabet_dict: dict = download_aurebesh_alphabet):
    
    """ text to Leet function """
    
    text = text.lower()
    new_str_list = []
    fake_num = None
    
    for num, char in enumerate(text):
        if num != fake_num:
            try:
                #print("Im here!")
                #print(char, text[num + 1])
                if ((char == "c" and text[num + 1] == "h") \
                    or (char == "e" and text[num + 1] == "o") \
                    or (char == "k" and text[num + 1] == "h") \
                    or (char == "n" and text[num + 1] == "g") \
                    or (char == "o" and text[num + 1] == "o") \
                    or (char == "s" and text[num + 1] == "h") \
                    or (char == "t" and text[num + 1] == "h")):
                    new_char = alphabet_dict.get(char + text[num + 1], char + text[num + 1])    
                    fake_num = num + 1
                else: 
                    new_char = alphabet_dict.get(char, char)
            except:
                new_char = alphabet_dict.get(char, char)
            new_str_list.append(new_char + " ")
    new_str = "".join(new_str_list)[:-1]
    return new_str
            
if __name__ == "__main__":
    
    alphabet_dict = download_aurebesh_alphabet()
    #print(alphabet_dict)
    new_str = text_to_aurebesh("LEOT", alphabet_dict)
    print(new_str)