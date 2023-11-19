package main

import "math/rand"

type Password struct {
	Length     int
	HasUpper   bool
	HasNumbers bool
	HasSymbols bool
}

func main() {
	passwordType := Password{
		Length:     14,
		HasUpper:   true,
		HasNumbers: true,
		HasSymbols: false,
	}

	println(passwordType.Generate())
}

func (p *Password) Generate() string {
	baseUpperRune := 'A'
	baseLowerRune := 'a'
	baseNumberRune := '0'
	ss := []string{"!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+"}
	rand.Shuffle(len(ss), func(i, j int) { ss[i], ss[j] = ss[j], ss[i] })

	var password string

	for len(password) < p.Length {
		password += string(baseLowerRune + rune(rand.Intn(26)))
		if p.HasUpper {
			password += string(baseUpperRune + rune(rand.Intn(26)))
		}
		if p.HasNumbers {
			password += string(baseNumberRune + rune(rand.Intn(10)))
		}
		if p.HasSymbols {
			password += ss[rand.Intn(len(ss))]
		}
	}

	return password[:p.Length]
}
