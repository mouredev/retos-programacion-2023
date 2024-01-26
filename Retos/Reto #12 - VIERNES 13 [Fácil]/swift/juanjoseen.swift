import Foundation

extension Date {
    func dayNumber() -> Int? {
        return Calendar.current.dateComponents([.weekday], from: self).weekday
    }
}

func has_friday_13th(month: Int, year: Int) -> Bool {
    var dateComponents: DateComponents = DateComponents()
    dateComponents.year = year
    dateComponents.month = month
    dateComponents.day = 13
    
    if let date: Date = Calendar.current.date(from: dateComponents) {
        if let weekDay: Int = date.dayNumber() {
            // Friday is the 6th day in the week (starting in sunday)
            return weekDay == 6
        } else {
            print("Not a valid week day")
        }
    } else {
        print("Not a valid date")
    }
    return false
}

print(has_friday_13th(month: 1, year: 2023))
print(has_friday_13th(month: 10, year: 2023))
print(has_friday_13th(month: 1, year: 2024))

