package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

// First solution
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

// Second solution
type IReader interface {
	Read()
}

type IWriter interface {
	Write()
}

type ITableWriter interface {
	IReader
	IWriter
}

type MathOperationFunc func(n1, n2 int) int

var (
	divideFunc = func(n1, n2 int) int {
		return n1 / n2
	}

	addFunc = func(n1, n2 int) int {
		return n1 + n2
	}

	subtractFunc = func(n1, n2 int) int {
		return n1 - n2
	}

	multiplyFunc = func(n1, n2 int) int {
		return n1 * n2
	}
)

type PrintTableConfig struct {
	Number, RangeEnd int
	OperationFunc    MathOperationFunc
}

func printTableToConsole(config PrintTableConfig) {
	number := config.Number
	for n := 1; n <= config.RangeEnd; n++ {
		fmt.Printf("%d x %d = %d\n", number, n, config.OperationFunc(number, n))
	}
}

func readUserInput() (int, error) {
	var numberToUse int
	fmt.Println("Enter a number: ")

	_, err := fmt.Scanf("%d", &numberToUse)
	if err != nil {
		return 0, err
	}

	return numberToUse, nil

}

type MultiplicationTableConsoleWriter struct {
	Number int
}

func (m *MultiplicationTableConsoleWriter) Read() {
	fmt.Println("What multiplication table do you want to view?")

	result, err := readUserInput()
	if err != nil {
		fmt.Println(err)
		return
	}
	m.Number = result
}

func (m *MultiplicationTableConsoleWriter) Write() {
	fmt.Printf("Multiplication table  %v \n", m.Number)
	printTableToConsole(PrintTableConfig{
		Number:        m.Number,
		RangeEnd:      10,
		OperationFunc: multiplyFunc,
	})
}

type DivisionTableConsoleWriter struct {
	Number int
}

func (d *DivisionTableConsoleWriter) Read() {
	fmt.Println("What division table do you want to view?")

	result, err := readUserInput()
	if err != nil {
		fmt.Println(err)
		return
	}

	if result == 0 {
		fmt.Println("Cannot divide by zero")
		return
	}
	d.Number = result
}

func (d *DivisionTableConsoleWriter) Write() {
	fmt.Printf("Division table  %v \n", d.Number)
	printTableToConsole(PrintTableConfig{
		Number:        d.Number,
		RangeEnd:      10,
		OperationFunc: divideFunc,
	})
}

type AdditionTableConsoleWriter struct {
	Number int
}

func (a *AdditionTableConsoleWriter) Read() {
	fmt.Println("What addition table do you want to view?")

	result, err := readUserInput()
	if err != nil {
		fmt.Println(err)
		return
	}
	a.Number = result
}

func (a *AdditionTableConsoleWriter) Write() {
	fmt.Printf("Addition table  %v \n", a.Number)
	printTableToConsole(PrintTableConfig{
		Number:        a.Number,
		RangeEnd:      10,
		OperationFunc: addFunc,
	})
}

type SubtractionTableConsoleWriter struct {
	Number int
}

func (s *SubtractionTableConsoleWriter) Read() {
	fmt.Println("What substraction table do you want to view?")

	if result, err := readUserInput(); err != nil {
		fmt.Println(err)
		return
	} else {
		s.Number = result
	}
}

func (s *SubtractionTableConsoleWriter) Write() {
	fmt.Printf("Substraction table  %v \n", s.Number)
	printTableToConsole(PrintTableConfig{
		Number:        s.Number,
		RangeEnd:      10,
		OperationFunc: subtractFunc,
	})

}

func execute(tableWriter ITableWriter) {
	tableWriter.Read()
	tableWriter.Write()
}

func main() {
	execute(writeMultiplicationTable)
	execute(&MultiplicationTableConsoleWriter{})
	execute(&DivisionTableConsoleWriter{})
	execute(&AdditionTableConsoleWriter{})
	execute(&SubtractionTableConsoleWriter{})
}
