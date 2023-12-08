package main

import (
	"fmt"
	"regexp"
)

func main() {
	str1 := "https://retosdeprogramacion.com?year=2023&challenge=0"
	str2 := "http://www.baidu.com?name=abcd&age=456"
	str3 := "http://www.baidu.com?name=abcde&age=456&sex=%20M%20"
	str4 := "http://www.baidu.com"

	fmt.Printf("%q\n", GetParams(str1))
	fmt.Printf("%q\n", GetParams(str2))
	fmt.Printf("%q\n", GetParams(str3))
	fmt.Printf("%q\n", GetParams(str4))
}

func GetParams(str string) []string {
	re := regexp.MustCompile(`=([^&]+)`)
	match := re.FindAllStringSubmatch(str, -1)
	var params []string
	for _, v := range match {
		params = append(params, v[1])
	}
	return params
}
