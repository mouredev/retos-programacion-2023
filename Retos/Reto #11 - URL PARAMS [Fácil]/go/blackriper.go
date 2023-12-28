package main

import (
	"fmt"
	"strings"
)

// metodos de trabajo
type Params interface {
	ReadUrl()
	ExtractParams()
	PrintParams()
}

// implementar metodos
type UrlParams struct {
	Url    string
	Params []string
}

func (u *UrlParams) ReadUrl() {
	fmt.Println("Write a Url with params")
	fmt.Scanf("%v", &u.Url)
}

func (u *UrlParams) ExtractParams() {
	params := ShorhandUrl(u.Url)
	for _, val := range params {
		_, after, _ := strings.Cut(val, "=")
		u.Params = append(u.Params, after)

	}
}
func (u UrlParams) PrintParams() {
	fmt.Printf("the url %v contains next params %v", u.Url, u.Params)
}

// funcion para recortar url
func ShorhandUrl(url string) []string {
	_, after, _ := strings.Cut(url, "?")
	params := strings.Split(after, "&")
	return params
}

func main() {
	var url Params = &UrlParams{}
	url.ReadUrl()
	url.ExtractParams()
	url.PrintParams()
}
