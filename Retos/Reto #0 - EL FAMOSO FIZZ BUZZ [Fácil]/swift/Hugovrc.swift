
for numero in 1...100 {
    if numero % 3 == 0 && numero % 5 == 0 {
        print("fizzbuzz")
    }else if numero % 3 == 0 {
        print("fizz")
    }else if numero % 5 == 0 {
        print("buzz")
    }else {
        print(numero)
    }
    
}