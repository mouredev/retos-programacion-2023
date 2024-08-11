package main

import (
	"fmt"
	"strings"
)

type URLParameterExtractor interface {
	Extract(url string) ([]string, error)
}

type SimpleURLParameterExtractor struct{}

func NewSimpleURLParameterExtractor() *SimpleURLParameterExtractor {
	return &SimpleURLParameterExtractor{}
}

func (e *SimpleURLParameterExtractor) Extract(url string) ([]string, error) {
	if !strings.Contains(url, "?") {
		return nil, fmt.Errorf("no parameters found in URL")
	}

	parts := strings.Split(url, "?")
	if len(parts) < 2 {
		return nil, fmt.Errorf("invalid URL format")
	}

	paramsPart := parts[1]
	params := strings.Split(paramsPart, "&")
	values := []string{}

	for _, param := range params {
		pair := strings.Split(param, "=")
		if len(pair) == 2 {
			values = append(values, pair[1])
		} else {
			return nil, fmt.Errorf("invalid parameter format")
		}
	}

	return values, nil
}

func main() {
	url := "https://retosdeprogramacion.com?year=2023&challenge=0"
	extractor := NewSimpleURLParameterExtractor()

	values, err := extractor.Extract(url)
	if err != nil {
		fmt.Println("Error:", err)
		return
	}

	fmt.Println("Extracted values:", values)
}
