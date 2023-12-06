import Foundation

import Foundation

var seed = Int(Date().timeIntervalSince1970)

func randomNumber(a: Int, m: Int) -> Int {
    var q = a / m
    var r = a % m

    seed = a * (seed % q) - r * (seed / q)

    if seed < 0 {
        seed += m
    }

    return abs(seed)
}

var a = Int(Date().timeIntervalSince1970)

var m = 12345


for i in 1...10 {
    print("Numero \(i): \(randomNumber(a: a, m: m) % 100)\n")
    Thread.sleep(forTimeInterval: 3)
}