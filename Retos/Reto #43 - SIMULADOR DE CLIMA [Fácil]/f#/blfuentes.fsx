open System

type ClimaData = {
    Temperature: int
    Rain: float
}

let getRain (currentRain: float) (temperature: int) =
    let rainPerc = 
        match temperature with
        | t when t < 5 -> currentRain * 0.8
        | t when t > 25 -> currentRain * 1.2
        | _ -> currentRain
    match rainPerc with
    | r when r < 0.0 -> 0.0
    | r when r > 100.0 -> 100.0
    | _ -> rainPerc

let rec getClimaData (remainingDays: int) (currentDay: ClimaData) (climaCollection: ClimaData list) =
    if remainingDays = 0 then
        climaCollection
    else
        // temperatura final base de este día
        let endDayTemperature = 
            if (Random().Next(1, 10) = 5) then
                let tmpTemperature = 
                    if (Random().Next(1, 10) > 5) then
                        currentDay.Temperature + 2
                    else
                        currentDay.Temperature - 2
                tmpTemperature                
            else
                currentDay.Temperature

        // calcular la prob de lluvia del día siguiente con la temperatura del día actual
        let nextDayRain = getRain currentDay.Rain endDayTemperature               

        // clima del día actual para añadir a la lista
        let clima = { Temperature = (if currentDay.Rain = 100.0 then (endDayTemperature - 1) else endDayTemperature); Rain = currentDay.Rain }

        // clima de previsión del día siguiente
        let nextClima = { Temperature = clima.Temperature; Rain = nextDayRain }

        getClimaData (remainingDays - 1) nextClima (climaCollection @ [clima])

let initialDay:ClimaData = { Temperature = 22; Rain = 70.0 }
let climas = getClimaData 365 initialDay []

let daysofRain = climas |> List.filter(fun c -> c.Rain = 100.0) |> List.length
let maxTemperature = climas |> List.maxBy(fun c -> c.Temperature) |> fun c -> c.Temperature
let minTemperature = climas |> List.minBy(fun c -> c.Temperature) |> fun c -> c.Temperature