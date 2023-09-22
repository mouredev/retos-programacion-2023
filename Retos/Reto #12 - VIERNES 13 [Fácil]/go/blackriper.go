package main

import (
	"fmt"
	"time"
)

// metodos de trabajo
type Friday13 interface {
	ReadDate()
	FindFriday13()
}

// implementar metodos de  trabajo
type Friday struct {
	Year  int
	Month int
}

// leer info del año y el mes
func (f *Friday) ReadDate() {
	fmt.Println("Introduce a  year")
	fmt.Scanf("%d", &f.Year)
	fmt.Println("Introduce a month")
	fmt.Scanf("%d", &f.Month)
}

// comprobar viernes 13
func (f *Friday) FindFriday13() {
	date := time.Date(f.Year, time.Month(f.Month), 13, 0, 0, 0, 0, time.UTC)
	if date.Weekday() == time.Friday {
		fmt.Printf("the year %v  in the month %v has a friday 13", f.Year, f.Month)
	} else {
		fmt.Printf("the year %v in the month %v has not friday 13", f.Year, f.Month)
	}
}

func main() {
	var friday13 Friday13 = &Friday{}
	friday13.ReadDate()
	friday13.FindFriday13()
}
