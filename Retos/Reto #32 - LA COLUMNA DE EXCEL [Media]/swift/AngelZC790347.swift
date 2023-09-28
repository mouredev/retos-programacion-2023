import Foundation
func getNumberColumn(pattern:String)->Int{
	guard let _ = pattern.range(of: "[A-Z]", options: .regularExpression) else {
		return 0
	}

	if pattern.count < 2{		
		return Int(UnicodeScalar(pattern)!.value) - 64
	}
	return (Int(UnicodeScalar(String(pattern.first!))!.value) - 64) * 26 + getNumberColumn(pattern: String(pattern.dropFirst()))
}

print(getNumberColumn(pattern: "A"))
print(getNumberColumn(pattern: "Z"))
print(getNumberColumn(pattern: "AA"))
print(getNumberColumn(pattern: "CA"))
print(getNumberColumn(pattern: " "))	

