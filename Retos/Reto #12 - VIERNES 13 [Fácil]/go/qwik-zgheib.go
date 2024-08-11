package main

import (
	"fmt"
	"time"
)

type Friday13thDetector interface {
	HasFriday13th(month, year int) (bool, error)
}

type SimpleFriday13thDetector struct{}

func NewSimpleFriday13thDetector() *SimpleFriday13thDetector {
	return &SimpleFriday13thDetector{}
}

func (d *SimpleFriday13thDetector) HasFriday13th(month, year int) (bool, error) {
	if month < 1 || month > 12 {
		return false, fmt.Errorf("invalid month: %d", month)
	}
	if year < 1 {
		return false, fmt.Errorf("invalid year: %d", year)
	}

	date := time.Date(year, time.Month(month), 13, 0, 0, 0, 0, time.UTC)

	return date.Weekday() == time.Friday, nil
}

func main() {
	month := 10
	year := 2023

	detector := NewSimpleFriday13thDetector()

	hasFriday13th, err := detector.HasFriday13th(month, year)
	if err != nil {
		fmt.Println("Error:", err)
		return
	}

	if hasFriday13th {
		fmt.Printf("There is a Friday 13th in %d/%d\n", month, year)
	} else {
		fmt.Printf("There is no Friday 13th in %d/%d\n", month, year)
	}
}
