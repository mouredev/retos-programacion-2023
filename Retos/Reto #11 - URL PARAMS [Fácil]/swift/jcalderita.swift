import Foundation

let url: String = "https://retosdeprogramacion.com?year=2023&challenge=0"

let urlParts = url.components(separatedBy: "=").dropFirst()

if !urlParts.isEmpty {
    print(urlParts.compactMap { $0.components(separatedBy: "&").first })
}