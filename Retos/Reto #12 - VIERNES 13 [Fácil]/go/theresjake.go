package main
import (
	"fmt"
	"time"
)

var mes time.Month
var year int

func main() {
	fmt.Print("Ingresa el número del mes: ")
	fmt.Scan(&mes)

	for mes < 1 || mes > 12 {
		fmt.Print("El valor ingresado no es válido, inténtalo de nuevo: ")
		fmt.Scan(&mes)
	}

	fmt.Print("Ingresa el número del año: ")
	fmt.Scan(&year)
	
	fmt.Println(buscarViernes13(mes, year))
}

func buscarViernes13(mes time.Month, year int) bool {
	fecha := time.Date(year, mes, 13, 0, 0, 0, 0, time.UTC)
	return fecha.Weekday() == time.Friday
}

// Saludos Brais, soy relativamente nuevo en la comunidad, y
// este el primero de tus retos que realizo, un abrazo crack ☺