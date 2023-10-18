
import Foundation

func countdown(from: UInt32, withIntervals intervals: UInt32) {
    
    for number in (0...from).reversed() {
        print(number)
        if number == 0 {
            break
        }
        sleep(intervals)
    }
    print("El programa terminó")
}

countdown(from: 3, withIntervals: 4)


