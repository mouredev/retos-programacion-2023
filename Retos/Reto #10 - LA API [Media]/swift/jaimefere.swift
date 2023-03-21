import Foundation
import _Concurrency
import PlaygroundSupport

struct Driver: Decodable {
    let permanentNumber: String
    let code: String
    let givenName: String
    let familyName: String
    let dateOfBirth: String
    let nationality: String
    
    func getAge() -> Int {
        let dateFormatter = DateFormatter()
        dateFormatter.dateFormat = "yyyy-MM-dd"
        let currentYear = Calendar.current.dateComponents([.year], from: .now).year!
        let dateOfBirth = dateFormatter.date(from: dateOfBirth)!
        return currentYear - Calendar.current.dateComponents([.year], from: dateOfBirth).year!
    }
}

struct DriverTable: Decodable {
    let Drivers: Array<Driver>
}

struct MRData: Decodable {
    let DriverTable: DriverTable
}

struct F1APIResponse: Decodable {
    let MRData: MRData
}

func printF1DriversTable(season: Int) {
    let f1DriversAPIUrl = URL(string: "http://ergast.com/api/f1/\(season)/drivers.json")
    let session = URLSession.shared
    let task = session.dataTask(with: f1DriversAPIUrl!) { data, response, error in
        guard let data = data else { return }
        let f1APIResponse: F1APIResponse = try! JSONDecoder().decode(F1APIResponse.self, from: data)
        f1APIResponse.MRData.DriverTable.Drivers.sorted{ Int($0.permanentNumber)! < Int($1.permanentNumber)! }.forEach{ driver in
            print("\(driver.permanentNumber). \(driver.code): \(driver.givenName) \(driver.familyName), \(driver.getAge()) años (\(driver.nationality))")
        }
    }
    task.resume()
}

printF1DriversTable(season: 2023)
