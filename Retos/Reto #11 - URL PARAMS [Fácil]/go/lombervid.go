package main

import (
	"fmt"
	"reflect"
	"strings"
)

type URL string

func (u URL) GetQueryParams() map[string]string {
	params := make(map[string]string)

	urlInfo := strings.Split(strings.TrimSpace(string(u)), "?")

	if len(urlInfo) < 2 {
		return params
	}

	if urlInfo[1] == "" {
		return params
	}

	for _, param := range strings.Split(urlInfo[1], "&") {
		pairs := strings.Split(param, "=")

		if len(pairs) < 2 {
			params[pairs[0]] = "true"
		} else {
			params[pairs[0]] = pairs[1]
		}
	}

	return params
}

func main() {
	tests := []struct {
		url  URL
		want map[string]string
	}{
		{
			"https://retosdeprogramacion.com?year=2023&challenge=0",
			map[string]string{"year": "2023", "challenge": "0"},
		},
		{
			"http://google.com/?something=",
			map[string]string{"something": ""},
		},
		{
			"http://google.com/?something",
			map[string]string{"something": "true"},
		},
		{
			"http://google.com/?",
			map[string]string{},
		},
	}

	for i, tt := range tests {
		got := tt.url.GetQueryParams()

		if !reflect.DeepEqual(got, tt.want) {
			fmt.Printf("Failed test %d: got %v, want %v", i, got, tt.want)
		}
	}
}
