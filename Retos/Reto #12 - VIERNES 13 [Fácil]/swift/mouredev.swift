import Foundation

func friday13(year: Int, month: Int) -> Bool {
 
    let calendar = Calendar(identifier: .gregorian)
    var components = DateComponents()
    components.year = year
    components.month = month
    components.day = 13
    
    if let date = calendar.date(from: components) {
        return calendar.component(.weekday, from: date) == 6
    }
    
    return false
}

print(friday13(year: 2023, month: 3))
print(friday13(year: 2023, month: 1))
print(friday13(year: 2023, month: 13))
print(friday13(year: -2023, month: 1))
print(friday13(year: 2023, month: 0))
