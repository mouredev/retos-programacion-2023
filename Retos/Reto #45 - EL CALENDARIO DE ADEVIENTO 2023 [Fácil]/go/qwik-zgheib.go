package main

import (
	"bufio"
	"fmt"
	"math/rand"
	"os"
	"strings"
)

func main() {
	rand.Int()
	participants := make(map[string]bool)
	scanner := bufio.NewScanner(os.Stdin)

	for {
		fmt.Println("\n--- options ---")
		fmt.Println("1. add participant")
		fmt.Println("2. list participants")
		fmt.Println("3. remove participant")
		fmt.Println("4. raffle winner")
		fmt.Println("5. exit")

		fmt.Print("choose an option: ")
		scanner.Scan()
		option := strings.TrimSpace(scanner.Text())

		switch option {
		case "1":
			fmt.Print("insert participant name: ")
			scanner.Scan()
			name := strings.TrimSpace(scanner.Text())
			if _, exists := participants[name]; exists {
				fmt.Println("already exists.")
			} else {
				participants[name] = true
				fmt.Println("successfully added.")
			}
		case "2":
			if len(participants) == 0 {
				fmt.Println("not participants.")
			} else {
				fmt.Println("participants:")
				for name := range participants {
					fmt.Println("-", name)
				}
			}
		case "3":
			fmt.Println("insert participant name to remove: ")
			scanner.Scan()
			name := strings.TrimSpace(scanner.Text())
			if _, exists := participants[name]; exists {
				delete(participants, name)
				fmt.Println("successfully removed.")
			} else {
				fmt.Println("participant not found.")
			}
		case "4":
			if len(participants) == 0 {
				fmt.Println("not enough participants.")
			} else {
				participantList := make([]string, 0, len(participants))
				for name := range participants {
					participantList = append(participantList, name)
				}
				winner := participantList[rand.Intn(len(participantList))]
				fmt.Printf("winner: %s\n", winner)
				delete(participants, winner)
			}
		case "5":
			fmt.Println("exiting...")
			return
		default:
			fmt.Println("invalid option. insert a valid option.")
		}
	}
}
