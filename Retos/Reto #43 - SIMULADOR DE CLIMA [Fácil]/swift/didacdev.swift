import Foundation

func weatherForecast(temperature: Double, rainProb: Double, days: Int) {

    var temperatures: [Double] = [temperature]
    var rainProbs: [Double] = [rainProb]

    for _ in 1...days {

        var newTemperature: Double = 0.0
        var newRainProb: Double = 0.0

        if rainProbs.last! == 1.0 {
            newTemperature = temperatures.last! - 1.0
        } else {
            newTemperature = temperatureChange(temperature: temperatures.last!)
        }
        
        if newTemperature > 20 {
            if rainProbs.last! <= 0.8 {
                newRainProb = rainProbs.last! + 0.2
            } else {
                newRainProb = rainProbs.last!
            }
        } else if newTemperature < 5 {
            if rainProbs.last! >= 0.2 {
                newRainProb = rainProbs.last! - 0.2
            } else {
                newRainProb = rainProbs.last!
            }
        } else {
            newRainProb = rainProbs.last!
        }

        temperatures.append(newTemperature)
        rainProbs.append(newRainProb)
    }
    
    for day in 0..<days {
        print("> Day \(day + 1): la temperatura es de \(temperatures[day])º y la probabilidad de lluvia del \(round(rainProbs[day]*100))%")
    }

    if let temperature = temperatures.max() {
        print("La temperatura máxima es de \(temperature)º")
    }

    if let temperature = temperatures.min() {
        print("La temperatura mínima es de \(temperature)º")
    }

    var rainingDays = 0
    rainProbs.forEach { (rainProb) in
        if rainProb == 1.0 {
            rainingDays += 1
        }
    }

    print("Lloverá \(rainingDays) días")

}

func temperatureChange(temperature: Double) -> Double {

    let randomNumber = Double.random(in: 0..<1)

    if randomNumber <= 0.1 {

        return temperature + 2

    } else if randomNumber <= 0.2 {

        return temperature - 2

    } else {

        return temperature

    }
}

weatherForecast(temperature: 20, rainProb: 0.8, days: 20)
