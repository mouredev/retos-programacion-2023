package main

import (
	"fmt"
	"log"
	"strconv"
	"strings"
)

func RGBToHex(r, g, b int) string {
	return fmt.Sprintf("#%02X%02X%02X", r, g, b)
}

func HexToRGB(hex string) (int, int, int, error) {
	if strings.HasPrefix(hex, "#") {
		hex = hex[1:]
	}

	if len(hex) != 6 {
		return 0, 0, 0, fmt.Errorf("invalid hex color format")
	}

	r, err := strconv.ParseInt(hex[0:2], 16, 32)
	if err != nil {
		return 0, 0, 0, err
	}

	g, err := strconv.ParseInt(hex[2:4], 16, 32)
	if err != nil {
		return 0, 0, 0, err
	}

	b, err := strconv.ParseInt(hex[4:6], 16, 32)
	if err != nil {
		return 0, 0, 0, err
	}

	return int(r), int(g), int(b), nil
}

func main() {
	r, g, b := 0, 0, 0
	hex := RGBToHex(r, g, b)
	fmt.Printf("RGB(%d, %d, %d) -> HEX: %s\n", r, g, b, hex)

	hex = "#000000"
	r, g, b, err := HexToRGB(hex)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Printf("HEX: %s -> RGB(%d, %d, %d)\n", hex, r, g, b)
}
