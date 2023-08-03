func drawStaircase(_ steps: Int) {
    if(steps == 0) {
        print("--")
    } else if(steps > 0) {
        var result = ""
        (0...steps).forEach { step in
            (0..<(steps - step)).forEach { _ in
                result += "  "
            }
            print("\(result)\((step == 0) ? "_" : "_|")")
            result = ""
        }
    } else {
        (steps...0).forEach { step in
            var result = (step == steps) ? "_" : " |_"
            ((steps - step)..<0).forEach { index in
                result = (index == -1 ? "" : "  ") + result
            }
            print(result)
            result = ""
        }
    }
}

drawStaircase(10)
drawStaircase(0)
drawStaircase(-10)
