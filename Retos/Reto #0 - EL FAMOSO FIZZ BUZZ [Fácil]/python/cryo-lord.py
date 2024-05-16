texto = ""
print("@-------------------@")
for i in range(1,101):
    if i%3 == 0:
        texto += "fizz"
    if i%5 == 0:
        texto += "buzz"
    if texto != "":
        print(f"     {i}: " + texto + "\n@-------------------@")
        texto = ""
    else:
        print(f"         {i}" + "\n@-------------------@")