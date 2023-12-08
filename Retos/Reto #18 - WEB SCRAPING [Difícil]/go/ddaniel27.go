// A quien lea esto
// No es la mejor solucion a decir verdad
// Pero es lo mas practico que se me ocurrio
// No se si es la mejor forma de hacerlo
// Pero funciona y tampoco quiero
// Pasar mucho tiempo en esto
// Ademas en la web no hay mucho que identifique
// A los articulos de la pagina
// Esta hecho con notion
package main

import (
	"fmt"

	"github.com/PuerkitoBio/goquery"
	"github.com/gocolly/colly"
)

func main() {
	c := colly.NewCollector()

	count := 0

	c.OnHTML("article[class]", func(e *colly.HTMLElement) {
		count++
		if count == 8 {
			children := e.DOM.Children()
			children.Slice(13, 28).Each(func(_ int, s *goquery.Selection) {
				fmt.Println(s.Text())
			})
		}
	})

	c.Visit("https://holamundo.day")
}
