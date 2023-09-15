package main

import (
	"encoding/json"
	"fmt"
	"io"
	"log"
	"net/http"
)

// url api
const URL = "https://rickandmortyapi.com/api/character"

// metodos de trabajo
type API interface {
	ApiRequest()
	ApiRespose()
}

// convertir respuesta string a estructuras de go
type Characters struct {
	ID       int
	Name     string
	Status   string
	Species  string
	Type     string
	Gender   string
	Origin   map[string]string
	Location map[string]string
	Image    string
	Episode  []string
	Url      string
	Crated   string
}

type Response struct {
	Info    map[string]string
	Results []Characters
}

// implementar metodos de trabajo
type CallApi struct {
	Resp Response
}

// hacer llamada a api rick and morty https://rickandmortyapi.com/documentation
func (c *CallApi) ApiRequest() {
	res, err := http.Get(URL)
	if err != nil {
		log.Fatal(err)
	}
	body, err := io.ReadAll(res.Body)
	if err != nil {
		log.Fatal(err)
	}
	// decodificar json a estructuras de go
	json.Unmarshal([]byte(body), &c.Resp)
	defer res.Body.Close()

}

// imprimir resultados de la llamada ala  api
func (c CallApi) ApiRespose() {
	for _, character := range c.Resp.Results {
		fmt.Printf("id: %v Name: %v Status: %v Specie: %v \n", character.ID, character.Name, character.Status, character.Species)
	}

}

func main() {
	var api API = &CallApi{}
	api.ApiRequest()
	api.ApiRespose()
}
