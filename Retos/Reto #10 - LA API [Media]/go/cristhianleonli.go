package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
)

type ChuckNorrisJoke struct {
	Id    string `json:"id"`
	Value string `json:"value"`
	Icon  string `json:"icon_url"`
}

func Request(url string, object interface{}) error {
	response, err := http.Get(url)
  
	if err != nil {
		log.Fatal(err)
	}

	defer response.Body.Close()

	return json.NewDecoder(response.Body).Decode(object)
}

func main() {
	joke := &ChuckNorrisJoke{}
	if err := Request("https://api.chucknorris.io/jokes/random", &joke); err != nil {
		log.Fatal(err)
	}

	fmt.Println(joke.Value)
}
