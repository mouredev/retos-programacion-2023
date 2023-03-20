package main

import (
	"fmt"
	"strings"
)

func FindParameters(url string) interface{} {
	params := make([]string, 0)

	urlDividida := strings.Split(url, "?")

	if len(urlDividida) > 1 {
		listaParams := strings.Split(urlDividida[1], "&")

		for _, param := range listaParams {
			clearParam := strings.Split(param, "=")
			if len(clearParam) > 1 && clearParam[1] != "" {
				params = append(params, clearParam[1])
			} else {
				return "La cadena no tiene parametros validos"
			}
		}

		return params
	} else {
		return "La cadena no tiene parametros"
	}
}

func main() {
	fmt.Println(FindParameters("https://retosdeprogramacion.com?year=2023&challenge=0"))
	fmt.Println(FindParameters("https://retosdeprogramacion.com"))
	fmt.Println(FindParameters("https://retosdeprogramacion.com?"))
	fmt.Println(FindParameters("https://retosdeprogramacion.com?year=2023"))
	fmt.Println(FindParameters("https://retosdeprogramacion.com?year=2023&"))
	fmt.Println(FindParameters("https://retosdeprogramacion.com?year=&"))
	fmt.Println(FindParameters("https://retosdeprogramacion.com?year=2023&challenge=0&languaje=python"))
}
