package main

import (
	"fmt"
	"strings"
)

type Cipher interface {
	Encrypt(text string, shift int) string
	Decrypt(text string, shift int) string
}

type CaesarCipher struct{}

func NewCaesarCipher() *CaesarCipher {
	return &CaesarCipher{}
}

func (cc *CaesarCipher) Encrypt(text string, shift int) string {
	return caesar(text, shift)
}

func (cc *CaesarCipher) Decrypt(text string, shift int) string {
	return caesar(text, -shift)
}

func caesar(text string, shift int) string {
	var result strings.Builder
	for _, char := range text {
		if char >= 'a' && char <= 'z' {
			result.WriteRune('a' + (char-'a'+rune(shift)+26)%26)
		} else if char >= 'A' && char <= 'Z' {
			result.WriteRune('A' + (char-'A'+rune(shift)+26)%26)
		} else {
			result.WriteRune(char)
		}
	}
	return result.String()
}

func main() {
	cipher := NewCaesarCipher()

	originalText := "Hello, World!"
	shift := 3

	encryptedText := cipher.Encrypt(originalText, shift)
	fmt.Printf("Original: %s\nEncrypted: %s\n", originalText, encryptedText)

	decryptedText := cipher.Decrypt(encryptedText, shift)
	fmt.Printf("Encrypted: %s\nDecrypted: %s\n", encryptedText, decryptedText)
}
