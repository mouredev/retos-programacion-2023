package main

import (
	"fmt"
	"reflect"
	"strings"
)

func parseURL(url string) map[string]string {
	components := strings.Split(url, "?")

	if len(components) != 2 {
		return map[string]string{}
	}

	params := strings.Split(components[1], "&")

	var result = make(map[string]string)

	for _, param := range params {
		values := strings.Split(param, "=")

		if len(values) == 2 {
			result[values[0]] = values[1]
		}
	}

	return result
}

func main() {
	tests := []struct {
		input  string
		output map[string]string
	}{
		{"https://retosdeprogramacion.com?year=2023&challenge=0", map[string]string{"year": "2023", "challenge": "0"}},
		{"https://url.com?year=2023?challenge=0", map[string]string{}},
		{"https://url.com?year=2023&challenge=0", map[string]string{"year": "2023", "challenge": "0"}},
	}

	for i, test := range tests {
		result := parseURL(test.input)

		if reflect.DeepEqual(result, test.output) {
			fmt.Printf("Test %d passed\n", i+1)
			fmt.Println(result)
			fmt.Println(test.output)
		} else {
			fmt.Printf("Test %d failed\n", i+1)
			fmt.Println(result)
			fmt.Println(test.output)
		}

		fmt.Println("======")
	}
}
