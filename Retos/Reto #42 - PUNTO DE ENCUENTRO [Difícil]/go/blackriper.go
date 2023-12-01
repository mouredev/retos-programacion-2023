package main

import (
	"fmt"
)

// definir metodos de trabajo
type MettingPoint interface {
	PointMetting(o1, o2 *Object)
	PrintResults()
}

// definir estructuras de trabajo
type Object struct {
	x, y   float64
	vx, vy float64
}

type ColisionPoint struct {
	X     float64
	Y     float64
	T     float64
	Found bool
}

func (c *ColisionPoint) PointMetting(o1, o2 *Object) {
	// Calculamos la velocidad relativa entre los dos objetos para mas info https://es.wikipedia.org/wiki/Velocidad_relativa.
	v12x := o1.vx - o2.vx
	v12y := o1.vy - o2.vy

	// Si la velocidad relativa es cero, los objetos no se moverán y, por lo tanto, no se encontrarán.
	if v12x == 0 && v12y == 0 {
		c.Found = false
		return
	}

	// Calculamos la ecuación de la recta que representa el movimiento de los dos objetos.
	// La ecuación es de la forma y = mx + b, donde m es la pendiente y b es el intercepto con el eje y.
	// mas info https://www.profesorenlinea.cl/geometria/Recta_Ecuacion_de.html
	m := v12y / v12x
	b := o1.y - m*o1.x

	// Resolvemos la ecuación para encontrar el punto de encuentro.
	c.X = (o2.y - b) / m
	c.Y = m*c.X + b

	// Calculamos el tiempo que tardarán los objetos en llegar al punto de encuentro.
	c.T = (c.X - o1.x) / o1.vx
	c.Found = true
	return
}

func (c ColisionPoint) PrintResults() {
	if c.Found {
		fmt.Println("the metting point is (", c.X, ", ", c.Y, ").")
		fmt.Println("the time it will take to find each other", c.T)
	} else {
		fmt.Println("Los objetos no se encontrarán.")
	}

}

func main() {
	// Definimos los objetos.
	o1 := Object{x: 1, y: 2, vx: 3, vy: 4}
	o2 := Object{x: 5, y: 6, vx: 7, vy: 8}

	var point MettingPoint = &ColisionPoint{}
	point.PointMetting(&o1, &o2)
	point.PrintResults()
}
