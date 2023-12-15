package main

import (
	"fmt"
	"os"
	"sort"
	"strings"
)

/* definir metodos de trabajo*/

// ruta donde se encuentra clonado tu repositorio de github
const SRC = "/home/blackriper/Documentos/Proyectos/retos-programacion-2023/Retos/"

type User struct {
	Name  string
	NumEx int
}

type Raking interface {
	CalculateData()
	ShowResults()
}

type ListRanking struct {
	Users []User
}

func (l *ListRanking) CalculateData() {
	num := make(chan int)
	directories := GetDirectories()
	users := GetUsers(directories)
	for _, user := range users {
		go FindUserInDirectories(directories, user, num)
		numEx := <-num
		finalUser := User{
			Name:  user,
			NumEx: numEx,
		}
		l.Users = append(l.Users, finalUser)
	}
	sort.Slice(l.Users, func(i, j int) bool { return l.Users[i].NumEx > l.Users[j].NumEx })
}
func (l ListRanking) ShowResults() {
	var numCorrections int
	fmt.Println(":::::Ranking Retos de programacion 2023:::::")
	for indx, user := range l.Users {
		place := PrizeIcon(indx + 1)
		fmt.Printf("%v %v -- %v\n", place, user.Name, user.NumEx)
		numCorrections += user.NumEx
	}
	fmt.Printf("\nTotal de participantes: %v \n", len(l.Users))
	fmt.Printf("Numero de correciones: %v \n", numCorrections)
}

/* Funciones auxiliares*/

// agregar iconos por decoracion
func PrizeIcon(indx int) (place string) {
	icons := map[int]string{
		1: "🥇",
		2: "🥈",
		3: "🥉",
	}
	if first, second := icons[indx]; second {
		place = fmt.Sprintf("%v.-%v ", indx, first)
	} else {
		place = fmt.Sprintf("%v.-", indx)
	}
	return place

}

// comprobar si el usuario ya esta en el array o no para evitar usuarios repetidos
func ExitsUser(users []string, user string) (exists bool) {
	for _, us := range users {
		if us == user {
			exists = true
		}
	}
	return exists
}

// obtiene los directorios de los diferentes retos disponibles en el  archivo
func GetDirectories() (directories []string) {
	files, err := os.ReadDir(SRC)
	if err != nil {
		panic(err)
	}
	for _, file := range files {
		if file.IsDir() == true {
			directories = append(directories, file.Name())
		}
	}
	return directories
}

// obtner primera lista de usuarios participantes
func GetUsers(directories []string) (users []string) {
	var i int
	for i < len(directories) {
		subfiles, _ := os.ReadDir(fmt.Sprintf("%v/%v", SRC, directories[i]))
		for _, subfile := range subfiles {
			solutions, _ := os.ReadDir(fmt.Sprintf("%v/%v/%v", SRC, directories[i], subfile.Name()))
			for _, sol := range solutions {
				user, _, _ := strings.Cut(sol.Name(), ".")
				if exists := ExitsUser(users, user); exists == false {
					users = append(users, user)
				}

			}
		}
		i++
	}
	return users
}

// contar cuantas veces se ha repetido un usuario en los directorios usando channel y gorutines
func FindUserInDirectories(directories []string, name string, num chan<- int) {
	var (
		i       int
		numPart int
	)
	for i < len(directories) {
		subfiles, _ := os.ReadDir(fmt.Sprintf("%v/%v", SRC, directories[i]))
		for _, subfile := range subfiles {
			solutions, _ := os.ReadDir(fmt.Sprintf("%v/%v/%v", SRC, directories[i], subfile.Name()))
			for _, sol := range solutions {
				user, _, _ := strings.Cut(sol.Name(), ".")
				if name == user {
					numPart++
				}
			}
		}
		i++
	}
	// enviar numero de veces que aparece el usuario al  canal num
	num <- numPart
}

func main() {
	var ranking Raking = &ListRanking{}
	ranking.CalculateData()
	ranking.ShowResults()
}
