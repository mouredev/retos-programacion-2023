package main

import (
	"encoding/json"
	"fmt"
	"io"
	"net/http"
)

type Response struct {
	Content []Content `json:"content"`
}

type Content struct {
	ID     string `json:"id"`
	Name   string `json:"name"`
	Symbol string `json:"symbol"`
	Slug   string `json:"slugName"`
	Status string `json:"status"`
	Type   string `json:"type"`
	URL    string `json:"url"`
}

func main() {
	resp, err := http.Get("https://api.bravenewcoin.com/v3/asset?symbol=LTC")
	if err != nil {
		fmt.Println("Error: ", err)
	}

	data, err := io.ReadAll(resp.Body)
	if err != nil {
		fmt.Println("Error: ", err)
	}

	var response Response
	if err := json.Unmarshal(data, &response); err != nil {
		fmt.Println("Error: ", err)
	}

	fmt.Printf("ID: %s\nName: %s\nSymbol: %s\nSlug: %s\nStatus: %s\nType: %s\nURL: %s\n",
		response.Content[0].ID,
		response.Content[0].Name,
		response.Content[0].Symbol,
		response.Content[0].Slug,
		response.Content[0].Status,
		response.Content[0].Type,
		response.Content[0].URL,
	)
}
