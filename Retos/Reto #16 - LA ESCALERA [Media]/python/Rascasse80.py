def escalera(num):
    if num < 0:
        #esc = "|_"
        for i in range(abs(num)+1):
            esc = (" "*2*i) + "|_"
            print(esc)
    elif num > 0:
        for i in range(num, -1, -1):
            esc = (" " *i*2) + "_|"
            print(esc)
    else:
        print("__")

escalera(-7)