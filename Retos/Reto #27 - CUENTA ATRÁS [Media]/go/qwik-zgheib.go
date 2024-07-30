package main

import (
	"fmt"
	"time"
)

type Printer interface {
	Print(count int)
}

type ConsolePrinter struct{}

func (cp *ConsolePrinter) Print(count int) {
	fmt.Println(count)
}

type Countdown struct {
	start    int
	interval int
	printer  Printer
}

func NewCountdown(start, interval int, printer Printer) (*Countdown, error) {
	if start <= 0 || interval <= 0 {
		return nil, fmt.Errorf("invalid start or interval")
	}

	return &Countdown{
		start:    start,
		interval: interval,
		printer:  printer,
	}, nil
}

func (cd *Countdown) Start() {
	for i := cd.start; i >= 0; i-- {
		cd.printer.Print(i)
		time.Sleep(time.Duration(cd.interval) * time.Second)
	}
}

func main() {
	printer := &ConsolePrinter{}
	countdown, err := NewCountdown(10, 1, printer)
	if err != nil {
		fmt.Println("Err:", err)
		return
	}

	countdown.Start()
}
