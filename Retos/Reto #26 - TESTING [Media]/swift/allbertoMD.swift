import Foundation
import XCTest

// Se aconseja usar el script en Playground para poder usar XCTest

func isFriday13th(month: Int, year: Int) -> Bool {
    
    let calendar = Calendar.current
    var components = DateComponents()
    
    components.year = year
    components.month = month
    components.day = 13
    
    if let date = calendar.date(from: components) {
        let weekday = calendar.component(.weekday, from: date)
        return weekday == 6
    }
    
    return false
}

class IsFriday13thTests: XCTestCase {
    
    func testIsFriday13th() {
        
        XCTAssertTrue(isFriday13th(month: 8, year: 2021))
        XCTAssertTrue(isFriday13th(month: 1, year: 2023))

        
        XCTAssertFalse(isFriday13th(month: 5, year: 2023))
        XCTAssertFalse(isFriday13th(month: 7, year: 2025))
    }
}

IsFriday13thTests.defaultTestSuite.run()




