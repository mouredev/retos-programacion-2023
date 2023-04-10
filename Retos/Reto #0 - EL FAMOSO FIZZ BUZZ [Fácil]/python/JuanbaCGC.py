def multiplo_de (num, mult):
    return num % mult

for i in range(1, 101):
    if multiplo_de(i,3) == 0 and multiplo_de(i,5) == 0:
        print("fizzbuzz \n")
    elif multiplo_de(i,3) == 0:
        print("fizz \n")
    elif multiplo_de(i,5) == 0:
        print("buzz \n")
    else:
        print(i,"\n")