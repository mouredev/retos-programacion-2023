package main

import (
	"fmt"
	"strings"
)

type TriforceDrawer interface {
	DrawTriforce(rows int) string
}

type Triforce struct{}

func NewTriforce() *Triforce {
	return &Triforce{}
}

func (t *Triforce) DrawTriforce(rows int) string {
	var builder strings.Builder

	for row := 0; row < rows*2; row++ {
		if row < rows {
			startSpace := strings.Repeat(" ", ((2*rows)-1)-row)
			printRow := strings.Repeat("*", (2*(row+1))-1)
			builder.WriteString(fmt.Sprintf("%s%s\n", startSpace, printRow))
		} else {
			currentRow := row - rows
			startSpace := strings.Repeat(" ", (rows-currentRow)-1)
			middleSpace := strings.Repeat(" ", (2*(rows-currentRow))-1)
			printRow := strings.Repeat("*", (2*(currentRow+1))-1)
			builder.WriteString(fmt.Sprintf("%s%s%s%s\n", startSpace, printRow, middleSpace, printRow))
		}
	}

	return builder.String()
}

func main() {
	triforce := NewTriforce()

	fmt.Println(triforce.DrawTriforce(1))
	fmt.Println(triforce.DrawTriforce(2))
	fmt.Println(triforce.DrawTriforce(3))
}
