package main

import (
	"fmt"
	"time"
)

func main() {
	years := []string{"2019", "2020", "2021", "2022", "2023"}
	months := []string{"01", "02", "03", "04", "10"}
	for i := 0; i < len(years); i++ {
		fmt.Println(IsFryday(years[i], months[i]), years[i], months[i])
	}
}

func IsFryday(year, month string) bool {
	layout := "2006-01-02"
	dateToParse := fmt.Sprintf("%s-%s-13", year, month)
	date, err := time.Parse(layout, dateToParse)
	if err != nil {
		return false
	}
	return date.Weekday() == time.Friday
}
