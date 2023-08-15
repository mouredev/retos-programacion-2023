def excel_column(input: str):
    column = 0;
    
    if(input):
        input = input.upper()
        
        i = 0
        for letra in input:
            column += (ord(letra) - 64) * (26 ** (len(input)-1-i))
            i += 1
            
        print(input + " => " + str(column))
        
        
excel_column("A")
excel_column("Z")
excel_column("AA")
excel_column("CA")
excel_column("ZYX")
excel_column("AYK")
excel_column("")