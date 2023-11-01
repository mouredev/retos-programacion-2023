package main

import (
	"fmt"
	"math/rand"
)

// definir metodos de trabajo
type WeatherSimulator interface {
	ReadParameters()
	SimulateWeather()
	ShowResultSimulate()
}

// implementar metodos
type Weather struct {
	Temp        int
	PosRain     int
	NumDays     int
	NumRainDays int
	MaxTemp     int
	MinTemp     int
}

func (w *Weather) ReadParameters() {
	fmt.Println("Enter initial temperature")
	fmt.Scanf("%d", &w.Temp)

	fmt.Println("Enter porcent posibility of rain ")
	fmt.Scanf("%d", &w.PosRain)

	fmt.Println("Enter number of days to simulate")
	fmt.Scanf("%d", &w.NumDays)

}

func (w *Weather) SimulateWeather() {

	temp := w.Temp
	posRain := w.PosRain
	raining := false

	w.MaxTemp = temp
	w.MinTemp = temp

	for d := 0; d < w.NumDays; d++ {

		if GradeIncrease() {
			temp += 2
		} else {
			temp -= 2
		}

		if temp > 25 {
			posRain += 20
		} else if temp < 5 {
			posRain -= 20
		}

		if posRain >= 100 {
			temp -= 1
			w.NumRainDays++
		}

		if temp > w.MaxTemp {
			w.MaxTemp = temp
		}

		if temp < w.MinTemp {
			w.MinTemp = temp
		}

		if posRain >= 100 {
			raining = true
		}

		fmt.Printf("Day %d: Temperature: %d, rain: %s\n", d+1, temp, IsRain(raining))
	}
}

func (w Weather) ShowResultSimulate() {
	fmt.Printf("Max Temperature: %v \n", w.MaxTemp)
	fmt.Printf("Min Temperature: %v \n", w.MinTemp)
	fmt.Printf("Total days of rain: %v \n", w.NumRainDays)
}

// funciones auxiliares
func GradeIncrease() bool {
	num := rand.Intn(2)
	if num == 0 {
		return true
	}
	return false
}

func IsRain(rain bool) string {
	if rain {
		return "rain"
	} else {
		return "no rain"
	}
}

func main() {
	var simulate WeatherSimulator = &Weather{}
	simulate.ReadParameters()
	simulate.SimulateWeather()
	simulate.ShowResultSimulate()
}
