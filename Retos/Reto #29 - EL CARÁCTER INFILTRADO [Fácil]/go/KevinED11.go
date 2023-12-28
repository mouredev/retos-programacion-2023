package main

import (
	"fmt"
	"log"
)

func differenceBetweenStrings(s1, s2 string) []string {
	if len(s1) != len(s2) {
		log.Fatal("the strings must have the same length")
	}

	var diference []string
	for i := 0; i < len(s1); i++ {
		if s1[i] != s2[i] {
			diference = append(diference, string(s2[i]))
		}
	}

	return diference

}

func main() {
	fmt.Println(differenceBetweenStrings("abc", "abd"))

}
