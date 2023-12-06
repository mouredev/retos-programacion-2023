
def analyze(n):
    if i%5 == 0 and i%3==0:
        print("\nfizzbuzz")
    elif i%5 == 0:
        print("\nbuzz")
    elif i%3==0:
        print("\nfizz")
    else:
        print("\n", i)
    

for i in range(1, 101):
    analyze(i)

