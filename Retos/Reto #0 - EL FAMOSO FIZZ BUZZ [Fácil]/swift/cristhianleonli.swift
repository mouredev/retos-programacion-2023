import Foundation

func main() {
    for i in 1...100 {
        switch (i % 3 == 0, i % 5 == 0) {
        case (true, false):
            print("fizz")
        case (false, true):
            print("buzz")
        case (true, true):
            print("fizzbuzz")
        case (false, false):
            print("\(i)")
        }
    }
}

main()