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
	// Read the number from console
	fmt.Println("Enter the number of steps")
	reader := bufio.NewReader(os.Stdin)
	str, err := reader.ReadString('\n')
	checkError(err)
	str = strings.Trim(str, "\n")

	// Convert to number
	steps, err := strconv.Atoi(str)
	checkError(err)

	// Print steps
	printSteps(steps)
}

func printSteps(steps int) {
	result := ""
	if steps == 0 {
		result = "__"
	}
	if steps > 0 {
		for i := steps - 1; i >= 0; i-- {
			spaces := strings.Repeat(" ", i*2)
			result += fmt.Sprintf("%s_|\n", spaces)
		}
	}
	if steps < 0 {
		steps = steps * -1
		for i := 0; i <= steps-1; i++ {
			spaces := strings.Repeat(" ", i*2)
			result += fmt.Sprintf("%s|_\n", spaces)
		}
	}
	fmt.Println(result)
}

func checkError(err error) {
	if err != nil {
		log.Fatal(err)
	}
}
