package main

func main() {
	println(DecToOctal(15), DecToHex(15))
}

func DecToOctal(dec int) string {
	oct := ""
	for dec > 0 {
		oct = string(dec%8+48) + oct
		dec /= 8
	}
	return oct
}

func DecToHex(dec int) string {
	hex := ""
	for dec > 0 {
		if dec%16 > 9 {
			hex = string(dec%16+55) + hex
		} else {
			hex = string(dec%16+48) + hex
		}
		dec /= 16
	}
	return hex
}
