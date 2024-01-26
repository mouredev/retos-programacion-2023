package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func main() {
	fmt.Print("Enter a decimal number: ")
	reader := bufio.NewReader(os.Stdin)
	str, err := reader.ReadString('\n')
	if err != nil {
		log.Fatal(err)
	}
	str = strings.Trim(str, "\n")

	num, err := strconv.ParseInt(str, 10, 64)
	if err != nil {
		log.Fatal(err)
	}

	fmt.Printf("%d number converted to octal is: %s\n", num, changeBase(num, 8))
	fmt.Printf("%d number converted to hexadecimal is: %s\n", num, changeBase(num, 16))
}

func changeBase(num, base int64) string {
	result := []string{}

	if num < base {
		return strconv.FormatInt(num, 10)
	}

	for num/base > base {
		result = append(result, strconv.FormatInt(num%base, 10))
		num = num / base

	}
	result = append(result, strconv.FormatInt(num%base, 10))
	result = append(result, strconv.FormatInt(num/base, 10))

	s := ""
	for i := len(result) - 1; i >= 0; i-- {
		s = s + result[i]
	}

	return s
}
