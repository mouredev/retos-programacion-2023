import UIKit

class RandomGenerator {
    private let primes: [Int] = [2, 3, 5, 7, 11, 13, 17, 19, 23, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167]
    private var index: Int = 0
    
    private init() {}
    
    static let shared: RandomGenerator = RandomGenerator()
    
    func random() -> Int  {
        let time: Int = Int(Date().timeIntervalSince1970 * 1000)
        let part1: Int = Int(time / getPrime())
        let part2: Int = Int(part1 * getPrime())
        return part2 % 101
    }
    
    private func getPrime() -> Int {
        let prime: Int = primes[index]
        index = (index + 1) % primes.count
        return prime
    }
    
}

let rg: RandomGenerator = RandomGenerator.shared
print(rg.random())
