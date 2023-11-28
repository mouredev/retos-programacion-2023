package main

import (
	"fmt"
	"math/rand"
)

/*interfaces de trabajo*/
type Adev interface {
	ShowMenuOptions()
}

type ParticipanCrud interface {
	AddParticipan(name string)
	ShowParticipans()
	DeleteParticipan(name string)
	HoldaDraw()
}

/*Implementar interface para acciones de los participantes*/

type Hold struct {
	Participans []string
}

func (h *Hold) AddParticipan(name string) {
	if exists := ExistParticipan(h.Participans, name); exists == false {
		h.Participans = append(h.Participans, name)
		fmt.Printf("participant %v successfully added\n", name)
	} else {
		fmt.Printf("participan %v already exists\n", name)
	}
}

func (h *Hold) ShowParticipans() {
	fmt.Println("+++Register participans aDEViento+++")
	for _, participan := range h.Participans {
		fmt.Println(participan)
	}
}
func (h *Hold) DeleteParticipan(name string) {
	if exists := ExistParticipan(h.Participans, name); exists == true {
		indx := GetIndex(h.Participans, name)
		h.Participans = append(h.Participans[:indx], h.Participans[indx+1:]...)
		fmt.Printf("participan %v delete successfully\n", name)
	} else {
		fmt.Printf("participan %v not exists \n", name)
	}
}

func (h *Hold) HoldaDraw() {
	random := rand.Intn(len(h.Participans))
	winner := h.Participans[random]
	h.Participans = append(h.Participans[:random], h.Participans[random+1:]...)
	fmt.Printf("Congratulations %v you winner a prieze\n", winner)
}

/*funciones auxilares*/
func GetIndex(participans []string, name string) int {
	indx := 0
	for ind, parparticipan := range participans {
		if parparticipan == name {
			indx = ind
		}
	}
	return indx
}

func ExistParticipan(participans []string, name string) bool {
	for _, part := range participans {
		if name == part {
			return true
		}
	}
	return false
}

/* implementar metodos para mostrar menu de opciones*/
type ADEViento struct {
	Adev ParticipanCrud
}

func (ad *ADEViento) ShowMenuOptions() {
	var (
		option int
		name   string
	)
adviento:
	for {
		fmt.Println("************************")
		fmt.Println("Welcome hold ADEViento")
		fmt.Println("**************************")
		fmt.Println("1.-Add participan")
		fmt.Println("2.-Show participans")
		fmt.Println("3.-Delete participan")
		fmt.Println("4.-Hold a Draw")
		fmt.Println("5.-Exit to program")

		fmt.Println("Enter a number to perform an action: ")
		fmt.Scanf("%d", &option)

		switch option {

		case 1:
			fmt.Println("What is name for a new participian?")
			fmt.Scanf("%s", &name)
			ad.Adev.AddParticipan(name)
		case 2:
			ad.Adev.ShowParticipans()
		case 3:
			fmt.Println("What is name for delete participan?")
			fmt.Scanf("%s", &name)
			ad.Adev.DeleteParticipan(name)
		case 4:
			ad.Adev.HoldaDraw()
		case 5:
			break adviento
		}

	}

}

func main() {
	var crudpart ParticipanCrud = &Hold{}
	var adev Adev = &ADEViento{Adev: crudpart}
	adev.ShowMenuOptions()

}
