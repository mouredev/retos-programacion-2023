import Foundation

func fizzBuzz(num: Int = 100) {
    for n in 0...num {
        if n % 3 == 0 && n % 5 == 0 {
            print("fizzbuzz")
            continue
        }
        
        if n % 3 == 0 {
            print("fizz")
            continue
        }
        
        if n % 5 == 0 {
            print("buzz")
            continue
        }
        
        print(n)
    }
}

fizzBuzz()




