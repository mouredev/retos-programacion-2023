from bs4 import BeautifulSoup
import requests
import re
import string

def download_leet_alphabet():
    url = "https://simple.wikipedia.org/wiki/Leet"
    body = requests.get(url)
    body_text = body.content

    clean = re.compile('<.*?>')

    alphabet_dict = dict()

    soup = BeautifulSoup(body_text, 'lxml')
    divs = soup.find_all("div", class_="mw-parser-output")
    for div in divs:
        uls = div.find_all("ul")
        for ul in uls:
            lis = ul.find_all("li")
            for li in lis:
                clean_line = re.sub(clean, '', str(li))
                source_char = clean_line[0]
                if source_char in string.ascii_letters:
                    dest_char = (clean_line[1:].replace(":", "").strip()).split(",")[0]
                elif source_char in string.digits:
                    dest_char = clean_line[4]
                alphabet_dict[source_char] = dest_char
                if source_char == "9":
                    break
            else:
                continue
            break
        else:
            continue
        break      
    
    return alphabet_dict     
            
def text_to_leet(text: str, alphabet_dict: dict = download_leet_alphabet):
    
    """ text to Leet function """
    
    new_str_list = []
    
    for char in text.upper():
        new_char = alphabet_dict.get(char, char)
        new_str_list.append(new_char)
    new_str = "".join(new_str_list)
    return new_str
            
if __name__ == "__main__":
    alphabet_dict = download_leet_alphabet()
    new_str = text_to_leet("LEET", alphabet_dict)
    print(new_str)