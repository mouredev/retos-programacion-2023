package main

import (
	"fmt"
	"io"
	"log"
	"net/http"
)

func Request(url string) []byte {
	response, err := http.Get(url)
	if err != nil {
		log.Fatal(err)
	}
	defer response.Body.Close()

	body, err := io.ReadAll(response.Body)
	if err != nil {
		log.Fatal(err)
	}

	return body
}

func main() {
	url := "https://animechan.vercel.app/api/random"
	response := Request(url)

	fmt.Println(string(response))
}
