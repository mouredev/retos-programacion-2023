package main

import (
	"encoding/json"
	"fmt"
	"net/http"
	"time"
)

var client *http.Client

type animeRamdom struct {
	Anime     string `json:"anime"`
	Character string `json:"character"`
	Quote     string `json:"quote"`
}

func GetJSON(url string, target interface{}) error {
	resp, err := client.Get(url)
	if err != nil {
		panic(err)
	}

	defer resp.Body.Close()

	return json.NewDecoder(resp.Body).Decode(target)
}

func main() {
	client = &http.Client{Timeout: 10 * time.Second}

	animeRecomendado := &animeRamdom{}

	if err := GetJSON("https://animechan.vercel.app/api/random", animeRecomendado); err != nil {
		panic(err)
	}

	fmt.Println("Anime:", animeRecomendado.Anime)
	fmt.Println("Personaje:", animeRecomendado.Character)
	fmt.Println("Cita del Personaje:", animeRecomendado.Quote)

}
