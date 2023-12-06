import Foundation
func read_abacus(_ abacus:[String])throws -> Int{
	enum ArgumentError:Error{
		case invalidFormat		
	}
	if !abacus.allSatisfy({$0.allSatisfy({$0 == "-"||$0 == "O"}) && $0.count == 12 }) { throw ArgumentError.invalidFormat }
	return Int((abacus.map({
		Double($0.first != "-" ? $0.split(separator: "-")[0].count : 0)*(pow(Double(10), Double(abacus.count - 1 - abacus.firstIndex(of: $0)!)))
	}).reduce(0, +)))
}
let abacus =	["O---OOOOOOOO",
				"OOO---OOOOOO",
				"---OOOOOOOOO",
				"OO---OOOOOOO",
				"OOOOOOO---OO",
				"OOOOOOOOO---",
				"---OOOOOOOOO"]
do{
	print(try read_abacus(abacus))	
}catch let e {
	print(e)
	exit(1)
}
