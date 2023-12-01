const DAYS_AMOUNT = 7
const INITIAL_CONDITIONS = {
    temperature: 30,
    rainProbability: 100
}

const forecastWeather = (daysAmount, initialConditions) => {

    const forecast = [initialConditions]

    for (i = 0; i < daysAmount; i++) {
        const lastDaysForecast = forecast[forecast.length - 1]
        let temperature = lastDaysForecast.temperature
        let rainProbability = lastDaysForecast.rainProbability

        // 10% de posibilidades de que la temperatura aumente o disminuya 2 grados.
        const randomNumber = Math.floor(Math.random() * 20)
        if (randomNumber === 0) temperature = temperature - 2
        if (randomNumber === 1) temperature = temperature + 2

        // Si la temperatura supera los 25 grados, la probabilidad de lluvia al día siguiente aumenta en un 20%.
        if (lastDaysForecast.temperature > 25) rainProbability = rainProbability + 20
        // Si la temperatura baja de 5 grados, la probabilidad de lluvia al día siguiente disminuya en un 20%.
        else if (lastDaysForecast.temperature < 5) rainProbability = rainProbability - 20
        if (rainProbability > 100) rainProbability = 100
        if (rainProbability < 0) rainProbability = 0

        // Si llueve (100%), la temperatura del día siguiente disminuye en 1 grado.
        if (lastDaysForecast.rainProbability === 100) temperature = temperature - 1

        forecast.push({ temperature: temperature, rainProbability: rainProbability })
    }

    const minTemperature = forecast.reduce((accumulator, current) => accumulator < current.temperature ? accumulator : current.temperature, forecast[0].temperature)
    const maxTemperature = forecast.reduce((accumulator, current) => accumulator > current.temperature ? accumulator : current.temperature, forecast[0].temperature)
    const rainDaysAmount = forecast.reduce((accumulator, current) => accumulator + (current.rainProbability === 100 ? 1 : 0), 0)

    return {
        minTemperature: minTemperature,
        maxTemperature: maxTemperature,
        rainDaysAmount: rainDaysAmount,
        forecast: forecast
    }
}

console.log(forecastWeather(DAYS_AMOUNT, INITIAL_CONDITIONS))