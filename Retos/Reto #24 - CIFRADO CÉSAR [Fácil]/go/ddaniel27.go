package main

func main() {
	str := "Hello, World!"
	shift := 3
	encrypted := encrypt(str, shift)
	decripted := decrypt(encrypted, shift)
	println(encrypted)
	println(decripted)
}

func encrypt(str string, shift int) string {
	var encrypted string
	for _, c := range str {
		if (c < 'a' || c > 'z') && (c < 'A' || c > 'Z') {
			encrypted += string(c)
			continue
		}
		aux := c + rune(shift)
		if (aux > 'Z' && aux < 'a') || aux > 'z' {
			aux -= 26
		}
		encrypted += string(aux)
	}
	return encrypted
}

func decrypt(str string, shift int) string {
	var decrypted string
	for _, c := range str {
		if (c < 'a' || c > 'z') && (c < 'A' || c > 'Z') {
			decrypted += string(c)
			continue
		}
		aux := c - rune(shift)
		if (aux < 'a' && aux > 'Z') || aux < 'A' {
			aux += 26
		}
		decrypted += string(aux)
	}
	return decrypted
}
