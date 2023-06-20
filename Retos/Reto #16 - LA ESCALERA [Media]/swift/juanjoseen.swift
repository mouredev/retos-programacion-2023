//
//  juanjoseen.swift
//  
//
//  Created by Juan Jose Elias Navarro on 18/04/23.
//

import Foundation

func stairs(_ steps: Int) {
    if steps == 0 {
        print("__")
    } else if steps < 0 {
        for step in 0...abs(steps) * 2 {
            draw(step)
        }
    } else {
        for step in (0...abs(steps) * 2).reversed() {
            draw(step)
        }
    }
}

func draw(_ step: Int) {
    var spaces: String = String(repeating: " ", count: step)
    spaces.append(step % 2 == 0 ? "_" : "|")
    print(spaces)
}

print("Stairs (0)")
stairs(0)
print("\n\nStairs (-3)")
stairs(-3)
print("\n\nStairs (4)")
stairs(4)
