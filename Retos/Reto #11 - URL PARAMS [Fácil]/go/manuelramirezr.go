package main

import (
	"regexp"
	"strings"
)

type URL string

var validation bool

// URLRegex here
var URLRegex = `^https?:\/\/(www\.)?[\w-]+\.[\w-]+(\.[\w-]+)?\/?(\?[\w-]+=[\w-]+(&[\w-]+=[\w-]+)*)?$`
var parameters = `[\w-]+=[\w-]+(&[\w-]+=[\w-]+)*`
var re = regexp.MustCompile(URLRegex)
var rePar = regexp.MustCompile(parameters)

// Validate URL
func validateURL(url string) bool {
	return re.MatchString(url)
}

// Get Values from URL Parameters
func getValues(url string) []string {
	s := rePar.FindAllString(url, -1)
	values := []string{}
	parameter := strings.Split(strings.Join(s, ","), "&")
	if len(parameter) > 1 {
		for _, v := range parameter {
			values = append(values, strings.Split(v, "=")[1])
		}
		return values
	} else {
		return []string{"No parameters"}
	}

}

func main() {
	URL := "https://retosdeprogramacion.com/?id=1&name=Manuel"
	validation = validateURL(URL)
	if validation {
		values := getValues(URL)
		println(strings.Join(values, ","))
	} else {
		println("URL is not valid")
	}

}
