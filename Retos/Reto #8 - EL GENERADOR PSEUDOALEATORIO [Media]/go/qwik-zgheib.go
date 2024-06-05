package main

import (
	"fmt"
	"time"
)

type RandomNumberGenerator interface {
	Next() int
}

type LinearCongruentialGenerator struct {
	seed, a, c, m uint64
}

func NewLinearCongruentialGenerator(seed int64) *LinearCongruentialGenerator {
	return &LinearCongruentialGenerator{
		seed: uint64(seed),
		a:    1664525,
		c:    1013904223,
		m:    4294967296,
	}
}

func (lcg *LinearCongruentialGenerator) Next() int {
	lcg.seed = (lcg.a*lcg.seed + lcg.c) % lcg.m
	return int(lcg.seed % 101)
}

func main() {
	seed := time.Now().UnixNano()
	lcg := NewLinearCongruentialGenerator(seed)

	num := lcg.Next()
	fmt.Println("Number generated:", num)
}
