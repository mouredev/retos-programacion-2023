package main

import (
	"fmt"
)

/*
type StringComparator interface {
	Compare(str1, str2 string) ([]string, error)
}
*/

type SimpleStringComparator struct{}

func NewSimpleStringComparator() *SimpleStringComparator {
	return &SimpleStringComparator{}
}

func (c *SimpleStringComparator) Compare(str1, str2 string) ([]string, error) {
	if len(str1) != len(str2) {
		return nil, fmt.Errorf("strings must be of equal length")
	}

	var differences []string
	for i := 0; i < len(str1); i++ {
		if str1[i] != str2[i] {
			differences = append(differences, string(str1[i]))
		}
	}

	return differences, nil
}

func FindDifferences(str1, str2 string) ([]string, error) {
	comparator := NewSimpleStringComparator()
	return comparator.Compare(str1, str2)
}

func main() {
	str1 := "I'm maher majar"
	str2 := "I'm mahar majer"

	differences, err := FindDifferences(str1, str2)
	if err != nil {
		fmt.Println("Error:", err)
		return
	}

	fmt.Printf("Differences between \"%s\" and \"%s\": %v\n", str1, str2, differences)

	str3 := "I'm.Maher Majar"
	str4 := "I'm maher majar"

	differences, err = FindDifferences(str3, str4)
	if err != nil {
		fmt.Println("Error:", err)
		return
	}

	fmt.Printf("Differences between \"%s\" and \"%s\": %v\n", str3, str4, differences)
}

/**
	* if use to test: create file <name>_test.go, with this content and execute with go test -v
	* otherwise install package testify with: go get github.com/stretchr/testify/assert

package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestFindDifferences(t *testing.T) {
	tests := []struct {
		str1       string
		str2       string
		expected   []string
		shouldFail bool
	}{
		{"I'm maher majar", "I'm mahar majer", []string{"e", "a"}, false},
		{"I'm.Maher Majar", "I'm maher majar", []string{".", "M", "M"}, false},
		{"abc", "abcd", nil, true},
	}

	for _, test := range tests {
		result, err := FindDifferences(test.str1, test.str2)
		if test.shouldFail {
			assert.Error(t, err)
		} else {
			assert.NoError(t, err)
			assert.Equal(t, test.expected, result)
		}
	}
}
*/