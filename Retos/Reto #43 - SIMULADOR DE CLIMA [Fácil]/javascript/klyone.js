
function simulateWeather(initialTemperature, rainLikehood, days) {
    result = {}
    simulation = []
    simulation.push({temperature: initialTemperature,
                     rain: rainLikehood, rained: (rainLikehood == 100) ? true : false})

    let temperature = initialTemperature
    let rain = rainLikehood

    for (i = 0 ; i < days ; i++) {
        let d = passNextDay({temperature: temperature, rain: rain})
        simulation.push(d)
        temperature = d.temperature
        rain = d.rain
    }

    result.simulation = simulation

    let maxTemp = result.simulation[0].temperature
    let minTemp = result.simulation[0].temperature
    let rainedDays = 0

    result.simulation.forEach((d) => {
        if (d.temperature > maxTemp)
            maxTemp = d.temperature
        if (d.temperature < minTemp)
            minTemp = d.temperature
        if (d.rained)
            rainedDays++
    })

    result.metrics = {maxTemperature: maxTemp, minTemperature: minTemp, rainedDays: rainedDays}

    return result
}

function passNextDay({temperature, rain})
{
    let newTemperature = temperature
    let newRain = rain
    let rained = false
    const getRandom = () => Math.floor(Math.random() * 101)

    if (rain == 100) {
        newTemperature -= 1
        newRain = 0
        rained = true
    }
    else {
        let tempIncrease = getRandom() < 10
        if (tempIncrease) {
            newTemperature += 2
        }
        else {
            let tempDecrease = getRandom() < 10
            if (tempDecrease) {
                newTemperature -= 2
            }
        }
    }

    if (temperature > 25) {
        newRain += 20
        if (newRain > 100)
            newRain = 100
    } else {
        if (temperature < 5) {
            newRain -= 20;
            if (newRain < 0)
                newRain = 0
        }
    }

    return {temperature: newTemperature, rain: newRain, rained: rained}
}

console.log(simulateWeather(15, 10, 7))
console.log(simulateWeather(25, 30, 10))
console.log(simulateWeather(5, 25, 3))
console.log(simulateWeather(30, 50, 9))
