package main

import (
	"fmt"
	"strconv"
	"strings"
)

// definir metodos de trabajo
type Coverter interface {
	CoverterHexOrRGB(tyconv string)
}

var HEXTABLE map[int]string = map[int]string{10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}

/* implementar metodos de trabajo*/
type Value struct {
	Hex string
	Rgb []int
}

func (v Value) CoverterHexOrRGB(tycov string) {
	switch tycov {
	case "HEX":
		hex := RgbToHex(v.Rgb)
		fmt.Printf("RGB to HEX r: %v , g: %v , b: %v -> %v\n", v.Rgb[0], v.Rgb[1], v.Rgb[2], hex)
	case "RGB":
		rgb := HexToRbg(v.Hex)
		fmt.Printf("HEX to RGB hex: %v -> (r: %v ,g: %v , b: %v)\n", v.Hex, rgb[0], rgb[1], rgb[2])
	}

}

/* metodos auxiliares*/

// convertir rgb a hex
func RgbToHex(rgb []int) string {
	var hex string = "#"
	for _, val := range rgb {
		h := val % 16
		if h >= 10 {
			hex += HEXTABLE[h] + HEXTABLE[h]
		} else {
			hex += strconv.Itoa(h)
			hex += strconv.Itoa(h)
		}
	}
	return hex
}

// convertir rgb a hex
func HexToRbg(hex string) []int {
	var rgb []int

	for ind, val := range strings.ToUpper(hex) {
		if string(val) != "#" && ind < 6 {
			v := GetValues(string(val))
			result := v * 16
			v1 := GetValues(strings.ToUpper(string(hex[ind+1])))
			c := result + v1
			if ind == 1 || ind == 3 || ind == 5 {
				rgb = append(rgb, c)
			}
		}
	}
	return rgb
}

func GetValues(val string) int {
	var result int
	for key, value := range HEXTABLE {
		if value == val {
			result = key
		}
	}

	if result == 0 {
		v, _ := strconv.Atoi(val)
		result = v
	}
	return result
}

func main() {
	hex := "#FF00FF"
	rgb := []int{255, 0, 255}
	var conv Coverter = &Value{Hex: hex, Rgb: rgb}
	conv.CoverterHexOrRGB("HEX")
	conv.CoverterHexOrRGB("RGB")
}
