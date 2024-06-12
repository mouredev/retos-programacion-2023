package main

import (
	"fmt"
	"math/rand"
)

type Weather struct {
	Temperature       int
	ProbabilityOfRain float64
}

func fnMin(a, b float64) float64 {
	if a < b {
		return a
	}
	return b
}

func fnMax(a, b float64) float64 {
	if a > b {
		return a
	}
	return b
}

func simulateWeather(days int, initialTemp int, initialRainProb float64) {
	rand.Int()
	weather := Weather{
		Temperature:       initialTemp,
		ProbabilityOfRain: initialRainProb,
	}

	maxTemp := initialTemp
	minTemp := initialTemp
	rainDays := 0

	for i := 1; i <= days; i++ {
		if rand.Float64() < 0.10 {
			if rand.Intn(2) == 0 {
				weather.Temperature += 2
			} else {
				weather.Temperature -= 2
			}
		}

		if weather.Temperature > 25 {
			weather.ProbabilityOfRain = fnMin(weather.ProbabilityOfRain+20, 100)
		} else if weather.Temperature < 5 {
			weather.ProbabilityOfRain = fnMax(weather.ProbabilityOfRain-20, 0)
		}

		rains := rand.Float64() < (weather.ProbabilityOfRain / 100)
		if rains {
			weather.Temperature -= 1
			rainDays++
		}

		if weather.Temperature > maxTemp {
			maxTemp = weather.Temperature
		}
		if weather.Temperature < minTemp {
			minTemp = weather.Temperature
		}

		fmt.Printf("Day %d: Temperature = %d°C, Rain = %v\n", i, weather.Temperature, rains)
	}

	fmt.Printf("\nMaximum Temperature: %d°C\n", maxTemp)
	fmt.Printf("Minimum Temperature: %d°C\n", minTemp)
	fmt.Printf("Days with Rain: %d\n", rainDays)
}

func main() {
	simulateWeather(10, 20, 30)
}
