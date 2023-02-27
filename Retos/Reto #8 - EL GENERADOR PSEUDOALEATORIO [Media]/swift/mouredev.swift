import Foundation

func random() -> Int {
    return Calendar.current.component(.nanosecond, from: Date()) % 101
}

(0...100).forEach { _ in
    print(random())
}