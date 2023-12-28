package main

import (
	"fmt"
	"os"
	"os/exec"
	"time"
)

const (
	Filas     = 10
	Columnas  = 10
	PiezaTetris = `
     *  
   ***
	`
)

var pantalla [Filas][Columnas]bool

type Pieza struct {
	x, y int
	forma string
}

func nuevaPieza() Pieza {
	return Pieza{
		x:     0,
		y:     Columnas/2 - 2,
		forma: PiezaTetris,
	}
}

func (p *Pieza) mostrar() {
	for i := 0; i < len(p.forma); i++ {
		for j := 0; j < len(p.forma); j++ {
			if p.forma[i] == '*' {
				pantalla[p.x+i][p.y+j] = true
			}
		}
	}
}

func (p *Pieza) borrar() {
	for i := 0; i < len(p.forma); i++ {
		for j := 0; j < len(p.forma); j++ {
			if p.forma[i] == '*' {
				pantalla[p.x+i][p.y+j] = false
			}
		}
	}
}

func (p *Pieza) moverAbajo() bool {
	p.borrar()
	p.x++
	if p.colision() {
		p.x--
		p.mostrar()
		return true
	}
	p.mostrar()
	return false
}

func (p *Pieza) moverIzquierda() {
	p.borrar()
	p.y--
	if p.colision() {
		p.y++
	}
	p.mostrar()
}

func (p *Pieza) moverDerecha() {
	p.borrar()
	p.y++
	if p.colision() {
		p.y--
	}
	p.mostrar()
}

func (p *Pieza) rotar() {
	p.borrar()
	var nuevaForma string
	for i := 0; i < len(p.forma); i++ {
		for j := len(p.forma) - 1; j >= 0; j-- {
			nuevaForma += string(p.forma[j*len(p.forma)+i])
		}
	}
	p.forma = nuevaForma
	if p.colision() {
		for i := 0; i < 3; i++ {
			p.rotar()
		}
	}
	p.mostrar()
}

func (p *Pieza) colision() bool {
	for i := 0; i < len(p.forma); i++ {
		for j := 0; j < len(p.forma); j++ {
			if p.forma[i] == '*' {
				if p.x+i >= Filas || p.y+j < 0 || p.y+j >= Columnas || pantalla[p.x+i][p.y+j] {
					return true
				}
			}
		}
	}
	return false
}

func limpiarPantalla() {
	cmd := exec.Command("clear") // Linux/Unix
	cmd.Stdout = os.Stdout
	cmd.Run()
}

func imprimirPantalla() {
	limpiarPantalla()
	for i := 0; i < Filas; i++ {
		for j := 0; j < Columnas; j++ {
			if pantalla[i][j] {
				fmt.Print("▣ ")
			} else {
				fmt.Print("□ ")
			}
		}
		fmt.Println()
	}
}

func main() {
	piezaActual := nuevaPieza()
	ticker := time.NewTicker(time.Millisecond * 500) // Velocidad de caída de la pieza
	gameOver := false

	for !gameOver {
		imprimirPantalla()
		select {
		case <-ticker.C:
			if !piezaActual.moverAbajo() {
				piezaActual = nuevaPieza()
				if piezaActual.colision() {
					gameOver = true
				}
			}
		default:
			var accion string
			fmt.Print("Acción (a: izquierda, d: derecha, s: abajo, r: rotar): ")
			fmt.Scanln(&accion)
			switch accion {
			case "a":
				piezaActual.moverIzquierda()
			case "d":
				piezaActual.moverDerecha()
			case "s":
				if !piezaActual.moverAbajo() {
					piezaActual = nuevaPieza()
					if piezaActual.colision() {
						gameOver = true
					}
				}
			case "r":
				piezaActual.rotar()
			}
		}
	}

	fmt.Println("¡Game Over!")
}
