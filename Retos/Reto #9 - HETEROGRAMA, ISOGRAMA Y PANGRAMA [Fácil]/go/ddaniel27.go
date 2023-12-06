package main

func main() {
	println(isPangram("the quick brown fox jumps over the lazy dog"))
	println(isIsogram("uncopyrightable"))
	println(isHeterogram("jumping"))
}

func isHeterogram(word string) bool {
	letters := make(map[rune]bool)
	for _, letter := range word {
		if letter == ' ' || letter == '-' {
			continue
		}
		if letters[letter] {
			return false
		}
		letters[letter] = true
	}
	return true
}

func isIsogram(word string) bool {
	letters := make(map[rune]int)
	for _, letter := range word {
		if letter == ' ' || letter == '-' {
			continue
		}
		letters[letter] += 1
	}
	var aux int
	for _, count := range letters {
		if aux == 0 {
			aux = count
			continue
		}
		if aux != count {
			return false
		}
	}
	return true
}

func isPangram(word string) bool {
	dict := map[rune]bool{
		'a': false,
		'b': false,
		'c': false,
		'd': false,
		'e': false,
		'f': false,
		'g': false,
		'h': false,
		'i': false,
		'j': false,
		'k': false,
		'l': false,
		'm': false,
		'n': false,
		'o': false,
		'p': false,
		'q': false,
		'r': false,
		's': false,
		't': false,
		'u': false,
		'v': false,
		'w': false,
		'x': false,
		'y': false,
		'z': false,
	}

	for _, letter := range word {
		if letter == ' ' || letter == '-' {
			continue
		}
		dict[letter] = true
	}

	for _, value := range dict {
		if !value {
			return false
		}
	}
	return true
}
