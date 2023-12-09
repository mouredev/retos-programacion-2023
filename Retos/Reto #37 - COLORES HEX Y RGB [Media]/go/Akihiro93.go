package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Print("")
	converter_rgb(8, 200, 33)
	// converter_hex("#8C821")
}

func converter_rgb(r, g, b int) {
	var result string = "#"

	for _, v := range([]int{r, g,b}) {
		var hex_v string = ""
		if v < 10 {
			hex_v = fmt.Sprintf("%x", v)
			hex_v = hex_v + "0"
		} else {	
			hex_v = fmt.Sprintf("%x", v)
			hex_v = strings.ToUpper(hex_v)
		}
		
		result = result + hex_v
	}
	fmt.Println(result)


}

//func converter_hex(hex string)  {}
