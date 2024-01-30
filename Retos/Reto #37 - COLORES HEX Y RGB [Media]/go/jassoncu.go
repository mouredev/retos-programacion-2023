package main

import (
	"fmt"
	"image/color"
	"regexp"
	"strconv"
)

func hexToRGB(hex string) (int, int, int, error) {
	// Verificar el formato del color HEX
	hexPattern := regexp.MustCompile(`^#?([0-9a-fA-F]{3}|[0-9a-fA-F]{6})$`)
	if !hexPattern.MatchString(hex) {
		return 0, 0, 0, fmt.Errorf("Formato de color HEX no válido")
	}

	// Quitar el carácter '#' si está presente
	if hex[0] == '#' {
		hex = hex[1:]
	}

	// Convertir a valores RGB
	var r, g, b int
	var err error
	if len(hex) == 3 {
		// Manejar formato corto de 3 caracteres
		r, err = strconv.Atoi(hex[0:1] + hex[0:1])
		if err != nil {
			return 0, 0, 0, err
		}
		g, err = strconv.Atoi(hex[1:2] + hex[1:2])
		if err != nil {
			return 0, 0, 0, err
		}
		b, err = strconv.Atoi(hex[2:3] + hex[2:3])
		if err != nil {
			return 0, 0, 0, err
		}
	} else {
		// Manejar formato largo de 6 caracteres
		r, err = strconv.Atoi(hex[0:2])
		if err != nil {
			return 0, 0, 0, err
		}
		g, err = strconv.Atoi(hex[2:4])
		if err != nil {
			return 0, 0, 0, err
		}
		b, err = strconv.Atoi(hex[4:6])
		if err != nil {
			return 0, 0, 0, err
		}
	}

	return r, g, b, nil
}

func rgbToHex(r, g, b int) string {
	// Convertir valores RGB a formato HEX
	return fmt.Sprintf("#%02X%02X%02X", r, g, b)
}

func main() {
	// Ejemplos de uso
	rgbExample := color.RGBA{0, 0, 0, 255}
	hexExample := "#000000"

	// Convertir RGB a HEX
	hexResult := rgbToHex(int(rgbExample.R), int(rgbExample.G), int(rgbExample.B))
	fmt.Printf("RGB a HEX: r: %d, g: %d, b: %d -> %s\n", rgbExample.R, rgbExample.G, rgbExample.B, hexResult)

	// Convertir HEX a RGB
	r, g, b, err := hexToRGB(hexExample)
	if err != nil {
		fmt.Println(err)
	} else {
		fmt.Printf("HEX a RGB: hex: %s -> (r: %d, g: %d, b: %d)\n", hexExample, r, g, b)
	}
}
