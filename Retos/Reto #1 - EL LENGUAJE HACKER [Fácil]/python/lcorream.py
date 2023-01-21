import random 

def traductor():
    
    list_dictionary = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    list_A = ["/\\", '@', '/-\\', '^', 'aye', '(L', 'Д']
    list_B= ["I3", "8", "13", "|3", "ß", "!3","(3", "/3", ")3", "|-]", "j3", "6"]
    list_C = ['¢', '{', '<', '(', '©']
    list_D = [')', '|)', '(|','[)', 'I>', '|>', '?', 'T)', 'I7', 'cl', '|}', '>', '|]']
    list_E = ['3', '&', '£', '€', 'ë', '[-', '|=-']
    list_F = ['|=', 'ƒ', '|#', 'ph', '/=', 'v']
    list_G = ["&", "6", "(_+", "9", "C-", "gee", "(?", "[,", "{,", "<-", "(."]
    list_H = ['#', '/-/', '[-]', ']-[', ')-(', '(-)', ':-:', '|~|', '|-|', ']~[', '}{', '!-!', '1-1', '\-/', 'I+I']
    list_I = ["1", "[]", "|", "!", "eye", "3y3", "]["]
    list_J = [",_|", "_|", "._|", "._]", "_]", ",_]", "]", ";", "1"]
    list_K = [" >|", "|<", "/<", "1<", "|c", "|(", "|{"]
    list_L = ['£', '7', '|_', '|']
    list_M = ['JVI', '[V]', '[]V[]', '|\/|', '^ ^', '<\/>','(v)', '(V)', '| V |', 'nn', 'IVI',']\[/','1^1','ITI','JTI']
    list_N = ['^/', '|\|', '/\/', '[\]', '<\>','{\}', '|V', '/V', 'И', '^', 'ท']
    list_0 = ["0", "Q", "()", "oh", "[]", "p", "<>", "Ø"]
    list_P = ['|*', '|o', '|º', '?', '|^', '|>', '|"', '9', '[]D', '|°', '|7']
    list_Q = ["(_,)", "9", "()", "2", "0_", "<|", "&"]
    list_R = ["I2", "|`", "|~", "|?", "/2", "|^", "lz", "|9","2", "12", "®", "[z", "Я", ".-", "|2", "|-"]
    list_S = ["5", '$', 'z', '§', 'ehs', 'es', '2']
    list_T = ["7", '+', '-|-', "']['", '†', '"|"', '~|~']
    list_U = ["(_)", '|_|', 'v', 'L|', 'µ', 'บ']
    list_V = ["\/", '|/', '\|']
    list_W = ["\/\/", 'VV', '\^/', '\V/', '\X/', '\_|_/']
    list_X = ["><", 'Ж', '}{', ')(', '][']
    list_Y = ["Ч", '\|/', '¥', '\//']
    list_Z = ["7_", '~/_', '-\_', '-|_']
             
    
    while True:

        dictionary_hack = dict(zip(list_dictionary, [random.choice(list_A), random.choice(list_B), random.choice(list_C), random.choice(list_D), random.choice(list_E), random.choice(list_F), random.choice(list_G), random.choice(list_H), random.choice(list_I), random.choice(list_J), random.choice(list_K), random.choice(list_L), random.choice(list_M), random.choice(list_N), random.choice(list_0), random.choice(list_P), random.choice(list_Q), random.choice(list_R), random.choice(list_S), random.choice(list_T), random.choice(list_U), random.choice(list_V), random.choice(list_W), random.choice(list_X), random.choice(list_Y), random.choice(list_Z)]))
        
        text_init = input("Ingrese la frase que desee traducir")
        for input_txt in text_init:
            if input_txt in list_dictionary:
                print(dictionary_hack[input_txt], end=" ")
                

if __name__ == "__main__":
    traductor()
