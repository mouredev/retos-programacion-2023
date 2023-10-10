package main

import (
	"testing"
)

/* codigo de testing obtenido del ejercicio 12 de carxofeta gracias por tu contribucion
go tiene su propia libreria para testing  solo si quieres mas funciones puedes usar alguna libreria
go permite evaluar varios casos de uso en forma de array o como el lo llama table driven testing por lo tanto cada caso de uso es como un testing individual
si vas a probar este testing el nombre del archivo tiene que tener al final _test.go para poder ejecutar el comando go test*/

// 1.-testing function friday13
type fridayTest struct {
	month, year int
	expected    bool
}

// definir casos de uso el ultimo caso comentado nos daria un eror
var caseUses = []fridayTest{
	{5, 2023, false},
	{1, 2023, true},
	//{1, 2023, false}
}

// funcion para testing de friday13 funcion
func TestFriday13(t *testing.T) {
	for _, test := range caseUses {
		if output := friday13(test.month, test.year); output != test.expected {
			t.Errorf("Output %v not equal expected %v \n", output, test.expected)
		}
	}
}

// 2.-testing funcion Parse data funcion agegada para poder hacer testing
type parseTest struct {
	month, year   string
	expected_one  int
	expected_two  error
	expected_tree int
	expected_four error
}

var inputs = []parseTest{
	{"1", "2023", 1, nil, 2023, nil},
	{"2", "2022", 2, nil, 2022, nil},
	//{"aw", "2023", 3, nil, 2023, nil},
}

func TestParseData(t *testing.T) {
	for _, input := range inputs {
		out1, out2, out3, out4 := parseData(input.month, input.year)
		if out1 != input.expected_one || out2 != input.expected_two || out3 != input.expected_tree || out4 != input.expected_four {
			t.Errorf("Ouputs %v, %v ,%v ,%v not equals %v ,%v ,%v ,%v", out1, out2, out3, out4, input.expected_one, input.expected_two, input.expected_tree, input.expected_four)
		}
	}
}
