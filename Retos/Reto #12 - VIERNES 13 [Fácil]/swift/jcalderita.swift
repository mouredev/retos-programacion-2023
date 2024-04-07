import Foundation

func hasFriday13(month: Int, year: Int) -> Bool {
    let calendar = Calendar(identifier: .gregorian)
    var components = DateComponents()
    components.year = year
    components.month = month
    components.day = 13
    
    guard let date = calendar.date(from: components) else {
        return false
    }
    
    return calendar.component(.weekday, from: date) == 6
}

print(hasFriday13(month: 9, year: 2024))