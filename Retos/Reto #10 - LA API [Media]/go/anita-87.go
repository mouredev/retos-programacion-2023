package main

import (
	"io"
	"log"
	"net/http"
)

func main() {
	c := http.Client{}

	resp, err := c.Get("https://uselessfacts.jsph.pl/api/v2/facts/random")
	if err != nil {
		log.Fatalf("Error: %v", err)
	}
	defer resp.Body.Close()

	data, err := io.ReadAll(resp.Body)
	if err != nil {
		log.Fatalf("Error: %v", err)
	}

	log.Printf("Response: %v", string(data))
}
