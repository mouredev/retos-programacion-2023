package main

import (
	"fmt"
	"math"
)

type Vector struct {
	X, Y float64
}

type Object struct {
	Position Vector
	Velocity Vector
}

func calculateIntersection(obj1, obj2 Object) (Vector, float64, bool) {
	dx := obj2.Position.X - obj1.Position.X
	dy := obj2.Position.Y - obj1.Position.Y
	dvx := obj2.Velocity.X - obj1.Velocity.X
	dvy := obj2.Velocity.Y - obj1.Velocity.Y

	if dvx == 0 && dvy == 0 {
		if dx == 0 && dy == 0 {
			return obj1.Position, 0, true
		} else {
			return Vector{}, 0, false
		}
	}

	var tx, ty float64
	var txValid, tyValid bool

	if dvx != 0 {
		tx = dx / dvx
		txValid = true
	}
	if dvy != 0 {
		ty = dy / dvy
		tyValid = true
	}

	if txValid && tyValid && math.Abs(tx-ty) > 1e-9 {
		return Vector{}, 0, false
	}

	t := 0.0
	if txValid {
		t = tx
	} else if tyValid {
		t = ty
	}

	if t < 0 {
		return Vector{}, 0, false
	}

	intersection := Vector{
		X: obj1.Position.X + obj1.Velocity.X*t,
		Y: obj1.Position.Y + obj1.Velocity.Y*t,
	}

	return intersection, t, true
}

func main() {
	obj1 := Object{
		Position: Vector{X: 0, Y: 0},
		Velocity: Vector{X: 1, Y: 1},
	}
	obj2 := Object{
		Position: Vector{X: 10, Y: 10},
		Velocity: Vector{X: -1, Y: -1},
	}

	intersection, time, found := calculateIntersection(obj1, obj2)
	if found {
		fmt.Printf("objects will be found at (%.2f, %.2f) after %.2f time units.\n", intersection.X, intersection.Y, time)
	} else {
		fmt.Println("the objects will not collide.")
	}

	obj3 := Object{
		Position: Vector{X: 10, Y: 10},
		Velocity: Vector{X: 1, Y: 1},
	}
	obj4 := Object{
		Position: Vector{X: 20, Y: 20},
		Velocity: Vector{X: 5, Y: 5},
	}
	intersection, time, found = calculateIntersection(obj3, obj4)
	if found {
		fmt.Printf("objects will be found at (%.2f, %.2f) after %.2f time units.\n", intersection.X, intersection.Y, time)
	} else {
		fmt.Println("the objects will not collide.")
	}
}
