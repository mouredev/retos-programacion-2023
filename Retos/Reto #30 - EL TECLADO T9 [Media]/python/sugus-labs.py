from bs4 import BeautifulSoup
import requests
import re
import string

def download_t9_alphabet():
    url = "https://es.wikipedia.org/wiki/Texto_predictivo"
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
                try:
                    clean_line = re.sub(clean, '', str(li))
                    number_char = str(clean_line[0])
                    corr_chars = clean_line.split("(")[1].split(")")[0]
                    corr_char_list = list(corr_chars)
                    alphabet_dict[number_char] = corr_char_list
                    #print(clean_line, number_char, corr_chars) 
                except:
                    break     
            if number_char == "9":
                break    
        if number_char == "9":
            break   

    return alphabet_dict     
            
def t9_to_text(text: str, alphabet_dict: dict = download_t9_alphabet):
    
    """ text with numbers to words function """
    
    new_str_list = []
    text_list = text.split("-")
    
    for t in text_list:
        pos = len(t) - 1
        new_char = alphabet_dict.get(t[0])[pos]
        new_str_list.append(new_char)
    new_str = "".join(new_str_list)
    
    return new_str

if __name__ == "__main__":
    alphabet_dict = download_t9_alphabet()
    new_str = t9_to_text("6-666-88-777-33-3-33-888", alphabet_dict)
    print(new_str)