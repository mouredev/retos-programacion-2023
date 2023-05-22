def fizzbuzz():
    for i in range(1,101):
        pr=''
        if i%3==0: pr+='fizz'
        if i%5==0: pr+='buzz'
        if pr=='': pr=str(i)
        print(pr)

fizzbuzz()