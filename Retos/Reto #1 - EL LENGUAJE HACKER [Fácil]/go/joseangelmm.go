package main

import (
	"bufio"
	"fmt"
	"os"
	"sync"
)

var alphabet = map[string]string{
	"a": "4",
	"b": "I3",
	"c": "[",
	"d": ")",
	"e": "3",
	"f": "|=",
	"g": "&",
	"h": "#",
	"i": "1",
	"j": ",_|",
	"k": ">|",
	"l": "1",
	"m": "/\\/\\",
	"n": "^/",
	"o": "0",
	"p": "|*",
	"q": "(_,)",
	"r": "I2",
	"s": "5",
	"t": "7",
	"u": "(_)",
	"v": "\\/",
	"w": "\\/\\/",
	"x": "><",
	"y": "j",
	"z": "2",
	" ": " ",
}

func main() {

	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {

		var wg sync.WaitGroup
		var leetWord string

		userText := scanner.Text()

		for i := range userText {
			wg.Add(1)

			go func() {
				defer wg.Done()
				val, ok := alphabet[string(userText[i])]
				if ok {
					leetWord += val
				} else {
					leetWord += " "
				}

			}()

			wg.Wait()
		}
		fmt.Println(leetWord)
	}
}
