(1...100).forEach { num in
    if(num % 5 == 0) {
        print("\(num % 3 == 0 ? "fizz" : "")buzz")
    } else if(num % 3 == 0) {
        print("fizz")
    } else {
        print(num)
    }
}