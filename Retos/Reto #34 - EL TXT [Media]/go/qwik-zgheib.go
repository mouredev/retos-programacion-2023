package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	fileName := "text.txt"

	if _, err := os.Stat(fileName); os.IsNotExist(err) {
		file, err := os.Create(fileName)
		if err != nil {
			fmt.Println("Error creating file:", err)
			return
		}
		defer func(file *os.File) {
			err := file.Close()
			if err != nil {
				return
			}
		}(file)
		fmt.Println("File created:", fileName)
	} else {
		fmt.Println("File already exists. Do you want to (c)ontinue writing or (o)verwrite it?")
		var response string
		_, err := fmt.Scanln(&response)
		if err != nil {
			return
		}
		if strings.ToLower(response) == "o" {
			err := os.Truncate(fileName, 0)
			if err != nil {
				fmt.Println("Error truncating file:", err)
				return
			}
			fmt.Println("File content cleared.")
		} else if strings.ToLower(response) == "c" {
			content, err := os.ReadFile(fileName)
			if err != nil {
				fmt.Println("Error reading file:", err)
				return
			}
			fmt.Println("Current file content:")
			fmt.Println(string(content))
		} else {
			fmt.Println("Invalid option. Exiting.")
			return
		}
	}

	file, err := os.OpenFile(fileName, os.O_APPEND|os.O_WRONLY, 0644)
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer func(file *os.File) {
		err := file.Close()
		if err != nil {
			return
		}
	}(file)

	scanner := bufio.NewScanner(os.Stdin)
	fmt.Println("Enter text (press Enter to save, type 'exit' to quit):")

	for scanner.Scan() {
		text := scanner.Text()
		if strings.ToLower(text) == "exit" {
			break
		}
		_, err := file.WriteString(text + "\n")
		if err != nil {
			fmt.Println("Error writing to file:", err)
			return
		}
	}

	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading input:", err)
	}
}
