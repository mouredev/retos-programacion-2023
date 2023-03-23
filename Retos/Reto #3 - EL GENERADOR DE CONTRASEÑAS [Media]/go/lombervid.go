package main

import (
	"fmt"
	"math/rand"
	"strings"
	"time"
)

const defaultLength int = 12
const pattern string = "abcdefghijklmnopqrstuvwxyz"
const numbers string = "0123456789"
const symbols string = "!@#$%^&*()-_=+[]{};:?"

type PasswordGenerator struct {
	length     int
	hasUpper   bool
	hasNumbers bool
	hasSymbols bool
}

func (pg *PasswordGenerator) getPattern() string {
	patternStr := pattern

	if pg.hasUpper {
		patternStr += strings.ToUpper(pattern)
	}

	if pg.hasNumbers {
		patternStr += numbers
	}

	if pg.hasSymbols {
		patternStr += symbols
	}

	return patternStr
}

func (pg *PasswordGenerator) reset() {
	pg.length = defaultLength
	pg.hasUpper = false
	pg.hasNumbers = false
	pg.hasSymbols = false
}

func (pg *PasswordGenerator) WithLength(length int) *PasswordGenerator {
	if length < 8 {
		pg.length = 8
	} else if length > 16 {
		pg.length = 16
	} else {
		pg.length = length
	}

	return pg
}

func (pg *PasswordGenerator) WithUpper() *PasswordGenerator {
	pg.hasUpper = true

	return pg
}

func (pg *PasswordGenerator) WithNumbers() *PasswordGenerator {
	pg.hasNumbers = true

	return pg
}

func (pg *PasswordGenerator) WithSymbols() *PasswordGenerator {
	pg.hasSymbols = true

	return pg
}

func (pg *PasswordGenerator) Generate() string {
	defer pg.reset()

	pattern := []rune(pg.getPattern())
	src := rand.NewSource(int64(time.Now().UnixNano()))
	random := rand.New(src)

	random.Shuffle(len(pattern), func(i, j int) {
		pattern[i], pattern[j] = pattern[j], pattern[i]
	})

	return string(pattern[:pg.length])
}

func NewPasswordGenerator() *PasswordGenerator {
	return new(PasswordGenerator).WithLength(defaultLength)
}

func main() {
	generator := NewPasswordGenerator()

	fmt.Println(generator.Generate())
	fmt.Println(generator.WithLength(16).Generate())
	fmt.Println(generator.WithNumbers().WithSymbols().Generate())
	fmt.Println(generator.Generate())
	fmt.Println(generator.WithLength(100).WithNumbers().Generate())
	fmt.Println(generator.WithLength(5).WithSymbols().Generate())
	fmt.Println(generator.WithLength(16).WithUpper().WithNumbers().WithSymbols().Generate())
}
