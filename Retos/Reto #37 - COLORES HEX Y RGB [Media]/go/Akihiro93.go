package main

import (
	"fmt"
	"log"
	"strconv"
	"strings"
)

func main() {
	fmt.Print("")
	converter_rgb(8, 200, 33)
	converter_hex("#08C821")
}

func converter_rgb(r, g, b int) {
	
	var result string = "#"
	for _, v := range([]int{r, g,b}) {
		var hex_v string = ""
			hex_v = fmt.Sprintf("%02X", v)
			hex_v = strings.ToUpper(hex_v)
		result = result + hex_v
	}
	fmt.Println(result)
}

func converter_hex(hex string) {
	var list_values []int64
	for _, v := range([]string{hex[1:3], hex[3:5], hex[5:7]}) {
		i, err := strconv.ParseInt(v, 16, 64)
		if err != nil {
			log.Fatalln(err)
		}
		list_values = append(list_values, i)
	}
	fmt.Printf("(r: %d, g: %d, b: %d )",list_values[0], list_values[1], list_values[2])
}
