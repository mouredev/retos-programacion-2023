import Foundation

extension String {
    var esHeterograma: Bool {
        for (key, value) in conteo() {
            if value > 1 {
                return false
            }
        }
        return true
    }
    
    var esIsograma: Bool {
        var total: Int = -1
        var conteo: [String: Int] = conteo()
        for (key, value) in conteo {
            if total < 0 {
                total = value
            } else {
                if value != total {
                    return false
                }
            }
        }
        return true
    }
    
    var esPangrama: Bool {
        let lower: String = self.lowercased()
        for char in Array("abcdefghijklmnopqrstuvwxyz") {
            if !lower.contains(where: { $0 == char }) {
                return false
            }
        }
        return true
    }
    
    private func conteo() -> [String: Int] {
        var dic: [String: Int] = [:]
        for char in Array(self) {
            let key: String = String(char)
            var value: Int = dic[key] ?? 0
            dic[key] = value + 1
        }
        
        return dic
    }
}

print("yuxtaponer".esHeterograma)
print("papa".esIsograma)
print("Benjamín pidió una bebida de kiwi y fresa. Noé, sin vergüenza, la más exquisita champaña del menú.".esPangrama)

