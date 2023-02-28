package main

import (
	"fmt"
	"regexp"
	"sort"
	"strings"
)

func rangeStr(start rune, end rune) string {
	var str string

	for i := start; i <= end; i++ {
		str += string(i)
	}

	return str
}

func mapValues[K comparable, V any](M map[K]V) []V {
	values := make([]V, 0, len(M))

	for _, value := range M {
		values = append(values, value)
	}

	return values
}

func mapKeys[K comparable, V any](M map[K]V) []K {
	keys := make([]K, 0, len(M))

	for key := range M {
		keys = append(keys, key)
	}

	return keys
}

func stringChars(str string) string {
	keys := mapKeys(countChars(str))

	strKeys := strings.Split(string(keys), "")
	sort.Strings(strKeys)

	return strings.Join(strKeys, "")
}

func countChars(str string) map[rune]int {
	counts := make(map[rune]int)

	for _, v := range str {
		counts[v]++
	}

	return counts
}

func clearString(str string) string {
	reg := regexp.MustCompile("[^a-z]+")

	return reg.ReplaceAllString(strings.ToLower(str), "")
}

func isIsogram(phrase string) bool {
	str := clearString(phrase)

	if str == "" {
		return false
	}

	counts := mapValues(countChars(str))
	sort.Ints(counts)

	return counts[0] == counts[len(counts)-1]
}

func isHeterogram(phrase string) bool {
	str := clearString(phrase)

	if str == "" {
		return false
	}

	counts := mapValues(countChars(str))
	sort.Ints(counts)

	return counts[len(counts)-1] == 1
}

func isPangram(phrase string) bool {
	str := clearString(phrase)

	if str == "" {
		return false
	}

	chars := stringChars(str)

	return chars == rangeStr('a', 'z')
}

func main() {
	tests := []struct {
		phrase       string
		isIsogram    bool
		isHeterogram bool
		isPangram    bool
	}{
		{"Some text her~!!!!!!!!", false, false, false},
		{"UNCOPYRIGHTABLE", true, true, false},
		{"deed", true, false, false},
		{"Vivienne", true, false, false},
		{"lycanthropies", true, true, false},
		{"Jackdaws love my big sphinx of quartz.", false, false, true},
		{"Waltz, bad nymph, for quick jigs vex.", false, false, true},
	}

	for i, test := range tests {
		fmt.Printf("Text %d %q", i, test.phrase)

		got := isIsogram(test.phrase)
		if got != test.isIsogram {
			fmt.Printf("\n\t- failed `isIsogram`: got %t, want %t\n", got, test.isIsogram)
			continue
		}

		got = isHeterogram(test.phrase)
		if got != test.isHeterogram {
			fmt.Printf("\n\t- failed `isHeterogram`: got %t, want %t\n", got, test.isHeterogram)
			continue
		}

		got = isPangram(test.phrase)
		if got != test.isPangram {
			fmt.Printf("\n\t- failed `isPangram`: got %t, want %t\n", got, test.isPangram)
			continue
		}

		fmt.Printf(" pass\n")
	}
}
