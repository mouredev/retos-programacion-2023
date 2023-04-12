import Foundation

func hasFriday13(_ year: Int, _ month: Int) -> Bool {
    let a = (14 - month) / 12
    let y = year - a
    let m = month + 12 * a - 2
    let d = (13 + y + y/4 - y/100 + y/400 + (31 * m) / 12) % 7
    return d == 5
}

print(hasFriday13(2022, 1))
print(hasFriday13(2000, 10))
print(hasFriday13(2022, 5))
print(hasFriday13(2023, 10))
print(hasFriday13(2024, 9))
print(hasFriday13(2024, 12))
