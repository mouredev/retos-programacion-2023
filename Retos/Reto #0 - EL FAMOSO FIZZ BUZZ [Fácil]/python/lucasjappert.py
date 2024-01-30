def _execute_fizzbuzz():
    for i in range(1, 101):
        text = ""
        if i % 3 == 0: text += "fizz"
        if i % 5 == 0: text += "buzz"
        if text == "": text = i
        print(text)

_execute_fizzbuzz()