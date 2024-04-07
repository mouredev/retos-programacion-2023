import Foundation

(1 ... 10).forEach { _ in
    print(Calendar.current.component(.nanosecond, from: Date()) % 101)
}