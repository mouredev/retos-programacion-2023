import Foundation


for n in 1...100{
    var multiplo3: Bool = n % 3 == 0
    var multiplo5: Bool = n % 5 == 0
    
    if multiplo3 && multiplo5 {
        print("fizzbuzz")
    }else if multiplo3{
        print("fizz")
    }else if multiplo5 {
        print("buzz")
    }else{
        print(n)
    }
    
}

