package main

import (
	"fmt"
	"strings"
)

type T9Translator interface {
	Translate(input string) string
}

type BasicT9Translator struct {
	t9Map map[string]string
}

func NewBasicT9Translator() *BasicT9Translator {
	return &BasicT9Translator{
		t9Map: map[string]string{
			"2": "A", "22": "B", "222": "C",
			"3": "D", "33": "E", "333": "F",
			"4": "G", "44": "H", "444": "I",
			"5": "J", "55": "K", "555": "L",
			"6": "M", "66": "N", "666": "O",
			"7": "P", "77": "Q", "777": "R", "7777": "S",
			"8": "T", "88": "U", "888": "V",
			"9": "W", "99": "X", "999": "Y", "9999": "Z",
		},
	}
}

func (t *BasicT9Translator) Translate(input string) string {
	blocks := strings.Split(input, "-")
	var result strings.Builder
	for _, block := range blocks {
		if char, exists := t.t9Map[block]; exists {
			result.WriteString(char)
		} else {
			result.WriteString("?")
		}
	}
	return result.String()
}

type Validator interface {
	Validate(input string) error
}

type BasicValidator struct{}

func (v *BasicValidator) Validate(input string) error {
	blocks := strings.Split(input, "-")
	for _, block := range blocks {
		if len(block) == 0 {
			return fmt.Errorf("empty block found")
		}
		char := block[0]
		for i := 1; i < len(block); i++ {
			if block[i] != char {
				return fmt.Errorf("block '%s' contains different numbers", block)
			}
		}
	}
	return nil
}

type T9Service struct {
	translator T9Translator
	validator  Validator
}

func NewT9Service(translator T9Translator, validator Validator) *T9Service {
	return &T9Service{translator: translator, validator: validator}
}

func (s *T9Service) Process(input string) (string, error) {
	if err := s.validator.Validate(input); err != nil {
		return "", err
	}
	return s.translator.Translate(input), nil
}

func main() {
	translator := NewBasicT9Translator()
	validator := &BasicValidator{}
	service := NewT9Service(translator, validator)

	input := "6-666-88-777-33-3-33-888"
	output, err := service.Process(input)
	if err != nil {
		fmt.Println("err:", err)
		return
	}
	fmt.Println("output:", output)

	anotherInput := "77-9-444-55"
	anotherOutput, err := service.Process(anotherInput)
	if err != nil {
		fmt.Println("err:", err)
		return
	}
	fmt.Println("another output:", anotherOutput)
}
