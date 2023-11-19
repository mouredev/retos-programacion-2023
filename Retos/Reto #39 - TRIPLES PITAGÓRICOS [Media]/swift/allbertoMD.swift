import Foundation

func findPythagoreanTriplesUpTo(number max: Int) {
    for a in 1...max {
        
        for b in a...max {
            
            for c in b...max  {
                if a * a + b * b == c * c {
                    print("(\(a), \(b), \(c)) is a Pythaforean Triple")
                }
            }
        }
    }
}


print("Introduce a max possitive number")
if let input = readLine(), let argument = Int(input) {
    findPythagoreanTriplesUpTo(number: argument)
} else {
    print("number most be Int")
}

