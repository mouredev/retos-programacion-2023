package main

import "fmt"

/* definir metodos de trabajo*/
type Permutation interface {
	ReadWord() string
	Perm(f func([]rune))
}

/*implementar metodos de trabajo*/
type Entry struct {
	A []rune
}

// leer entrada del usuario
func (e *Entry) ReadWord() string {
	var word string
	fmt.Println("Enter a word")
	fmt.Scanf("%s", &word)
	e.A = []rune(word)
	return word
}

// llamar la primera vez para evitar errores en la recursividad
func (e *Entry) Perm(f func([]rune)) {
	perm(e.A, f, 0)
}

/*Funciones auxiliares*/

// Hacer permutaciones desde i hasta len(a)-1
func perm(a []rune, f func([]rune), i int) {
	if i > len(a) {
		f(a)
		return
	}
	perm(a, f, i+1)
	for j := i + 1; j < len(a); j++ {
		a[i], a[j] = a[j], a[i]
		perm(a, f, i+1)
		a[i], a[j] = a[j], a[i]
	}
}

func main() {
	var per Permutation = &Entry{}
	word := per.ReadWord()
	fmt.Printf("Permutacions the word %v \n", word)
	per.Perm(func(r []rune) {
		fmt.Println(string(r))
	})
}
