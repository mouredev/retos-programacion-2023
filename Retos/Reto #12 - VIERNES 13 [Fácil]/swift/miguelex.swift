import Foundation

func isFridayThe13th (month: Int, year: Int) -> Bool {
    
    let calendar = Calendar.current
    let dateToCheck = DateComponents(year: year ,month: month, day: 13)
    let date = calendar.date(from: dateToCheck)
    let result : Bool
    
    result = calendar.component(.weekday, from: date!) == 6 ? true : false
    
    return result
}

print("¿Hay viernes 13 en marzo de 2023? \(isFridayThe13th(month: 3, year: 2023))")
print("¿Hay viernes 13 en enero de 2023? \(isFridayThe13th(month: 1, year: 2023))")
