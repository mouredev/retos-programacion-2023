package main

import (
	"errors"
	"fmt"
	_ "fmt"
	"strings"
)

type IAlphabet interface {
	Get() string
}

type IChiper interface {
	Encrypt() (string, error)
}

type IConversor interface {
	GetMapConversion() *map[string]string
}

type IDecrypter interface {
	Decrypt() (string, error)
}

type EnglishAlphabet struct {
}

func (a *EnglishAlphabet) Get() string {
	return "abcdefghijklmnopqrstuvwxyz"
}

type CaesarCipherConversor struct {
	IAlphabet
	Shift int
}

func (c *CaesarCipherConversor) GetMapConversion() *map[string]string {
	conversor := make(map[string]string)
	alphabet := c.IAlphabet.Get()

	for i, letter := range alphabet {
		cesarPosition := (i + c.Shift) % len(alphabet)
		cesarLetter := string(alphabet[cesarPosition])
		conversor[string(letter)] = cesarLetter
	}

	return &conversor

}

type CaesarCipher struct {
	text string
	IConversor
}

func (c *CaesarCipher) Encrypt() (string, error) {
	var cesarText string
	conversor := *c.IConversor.GetMapConversion()

	text := strings.ToLower(c.text)

	for _, letter := range text {
		let, exists := conversor[string(letter)]
		if !exists {
			return "", errors.New("Invalid letter")
		}

		cesarText += let
	}

	return cesarText, nil

}

type CaesarCipherDecrypter struct {
	text string
	IConversor
}

func (c *CaesarCipherDecrypter) Decrypt() (string, error) {
	text := strings.ToLower(c.text)
	originalMap := *c.IConversor.GetMapConversion()
	newMap := make(map[string]string)
	var decryptedText string

	for k, v := range originalMap {
		newMap[v] = k
	}

	for _, letter := range text {
		let, exist := newMap[string(letter)]
		if !exist {
			return "", errors.New("Invalid letter")
		}

		decryptedText += let
	}

	return decryptedText, nil

}

type Main struct {
	IChiper
	IDecrypter
}

func (m *Main) Encrypt() string {
	result, err := m.IChiper.Encrypt()
	if err != nil {
		fmt.Println(err)
	}
	return result
}

func (m *Main) Decrypt() string {
	result, err := m.IDecrypter.Decrypt()
	if err != nil {
		fmt.Println(err)
	}
	return result
}

func main() {
	alphabet := EnglishAlphabet{}
	cipherConversor := CaesarCipherConversor{IAlphabet: &alphabet, Shift: 3}

	cipher := CaesarCipher{text: "Hello", IConversor: &cipherConversor}
	decrypter := CaesarCipherDecrypter{text: "khoor", IConversor: &cipherConversor}

	program := Main{IChiper: &cipher, IDecrypter: &decrypter}
	encryptedText := program.Encrypt()
	decryptedText := program.Decrypt()

	fmt.Println(encryptedText, decryptedText)

}
