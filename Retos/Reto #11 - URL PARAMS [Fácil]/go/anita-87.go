package main

import (
	"fmt"
	"strings"
)

func main() {
	url := "https://retosdeprogramacion.com?year=2023&challenge=0"

	params := strings.Split(url, "?")[1]

	var paramValues []string
	for _, param := range strings.Split(params, "&") {
		paramValues = append(paramValues, strings.Split(param, "=")[1])
	}

	fmt.Println(paramValues)
}
