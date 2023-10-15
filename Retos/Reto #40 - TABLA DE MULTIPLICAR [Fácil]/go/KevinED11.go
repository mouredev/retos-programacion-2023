package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type MultiplicationTableWriterFunc func(number int)

func writeMultiplicationTable(number int) {
	for n := 1; n <= 10; n++ {
		fmt.Printf("%d x %d = %d\n", number, n, number*n)
	}
}
func convertUserInputToInt(input string) (int, error) {
	return strconv.Atoi(input)
}
func readUserInput() (int, error) {
	fmt.Println("Enter a number: ")

	reader := bufio.NewReader(os.Stdin)
	input, err := reader.ReadString('\n')

	if err != nil {
		return 0, err
	}

	input = strings.TrimSpace(input)

	return convertUserInputToInt(input)
}

func execute(writerFunc MultiplicationTableWriterFunc) {
	input, err := readUserInput()
	if err != nil {
		fmt.Println(err)
		return
	}

	writerFunc(input)
}

func main() {
	execute(writeMultiplicationTable)
}
