import Foundation


var x = 1
let a = 8
let c = 4
let m = 101

var seconds = 0.0

print("Cuantos números aleatorios quieres imprimir:")
guard let randomCount = readLine(), let randomCountInt = Int(randomCount) else {
    fatalError()
}
print("\nNúmeros aleatorios:")


let timerSeconds = Timer(timeInterval: 1.0, repeats: true) { _ in
    seconds += 0.1
}

let timerX = Timer(timeInterval: seconds, repeats: true) { _ in
    x += 1
}

for _ in 0..<randomCountInt {
    timerSeconds.fire()
    timerX.fire()
    sleep(1)
    x = (a * x + c) % m
    print(x)
}

