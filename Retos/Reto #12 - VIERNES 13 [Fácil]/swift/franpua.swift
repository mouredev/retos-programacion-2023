import Foundation
/*
 Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
 - La función recibirá el mes y el año y retornará verdadero o falso.
 */

func isFriday13(year: Int, month: Int) -> Bool{
    
    let calendar = Calendar.current
    let componets = DateComponents(year: year ,month: month, day: 13)
    let date = calendar.date(from: componets)
    
    if calendar.component(.weekday, from: date!) == 6 {
        return true
    } else {
        return false
    }
}
print(isFriday13(year: 2023, month: 1))
print(isFriday13(year: 2023, month: 3))