def infiltrated_characters(input1: str, input2:str):
    infiltrated_characters_list = []
    
    if len(input1) == len(input2):
        for index in range(0, len(input2)):
            if input1[index] != input2[index]:
                infiltrated_characters_list.append(input2[index])
                
        print(infiltrated_characters_list)
        
        
infiltrated_characters("Me llamo mouredev", "Me llemo mouredov")
infiltrated_characters("Me llamo.Brais Moure", "Me llamo brais moure")
infiltrated_characters("Me llamo.Brais Moure", "Me llamo brais moure ")