def same_text(text1: str, text2: str):
    if len(text1) != len(text2):
        return "Tiene que tener la misma longitud"
    else:
        diff_characters= []
        for i in range(0, len(text1)):
            if text1[i] != text2[i]:
                diff_characters.append(text2[i])
        return text1 + " / " + text2 + " -> " + str(diff_characters)
    
print(same_text("Hola.me llamo Lucas", "Hola me llamo Lucas"))