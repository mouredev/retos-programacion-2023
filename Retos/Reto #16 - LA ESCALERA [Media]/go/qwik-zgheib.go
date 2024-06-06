package main

import (
	"fmt"
	"strings"
)

type StairDrawer interface {
	DrawStairs(steps int) string
}

type Stairs struct{}

func NewStairs() *Stairs {
	return &Stairs{}
}

func (s *Stairs) DrawStairs(steps int) string {
	if steps == 0 {
		return "__"
	}

	var builder strings.Builder
	if steps > 0 {
		for i := steps; i > 0; i-- {
			if i == steps {
				builder.WriteString(strings.Repeat("  ", i))
				builder.WriteString("_\n")
			}
			builder.WriteString(strings.Repeat("  ", i-1))
			builder.WriteString("_|\n")

		}
	} else {
		builder.WriteString("_\n")
		for i := 0; i < -steps; i++ {
			if i == 0 {
				builder.WriteString(" ")
			} else {
				builder.WriteString(strings.Repeat("  ", i+1))
			}
			builder.WriteString("|_\n")
		}
	}
	return builder.String()
}

func main() {
	stairs := NewStairs()

	testCases := []int{4, -4, 0}
	for _, steps := range testCases {
		fmt.Printf("Steps: %d\n", steps)
		fmt.Println(stairs.DrawStairs(steps))
	}
}
