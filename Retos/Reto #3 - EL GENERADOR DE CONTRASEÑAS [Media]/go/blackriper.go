package main

import (
	"fmt"
	"log"
	"math/rand"
	"strconv"
	"strings"
)

// metodos de trabajo

type FactoryPass interface {
	ReadConfig()
	GeneratePassword()
	ShowNewPassword()
}

// implementar metodos
type Factory struct {
	Long     int
	Capital  bool
	Number   bool
	Symb     bool
	Password string
}

func (f *Factory) ReadConfig() {
	var option string

	fmt.Println("How long do you want the password? It can only be 8 to 16 characters.")
	fmt.Scanf("%s", &option)
	if option == "8" || option == "16" {
		lon, err := strconv.Atoi(option)
		if err != nil {
			log.Fatal(err)
		}
		f.Long = lon
	} else {
		fmt.Println("long not valid")
	}
	f.Capital = ConfirmQuestion("Do you want to use capital letters? y/n")
	f.Number = ConfirmQuestion("Do you want to use numbers? y/n")
	f.Symb = ConfirmQuestion("Do you want to use symbols? y/n")
}

func (f *Factory) GeneratePassword() {
	caracters := "abcdefghijklmnopqrstuvwxyz"

	if f.Capital == true {
		caracters += strings.ToUpper(caracters)
	}
	if f.Number == true {
		caracters += "1234567890"
	}
	if f.Symb == true {
		caracters += "~!@#$%^&*()_+`-=[]{}|;':,./<>?"
	}

	var pass string
	for i := 0; i < f.Long; i++ {
		pass = pass + string(caracters[rand.Intn(len(caracters))])
	}
	f.Password = pass
}

func (f Factory) ShowNewPassword() {
	fmt.Printf("Password generate : %v", f.Password)
}

// funcion auxilar para optiones
func ConfirmQuestion(message string) bool {
	var (
		answer string
		result bool
	)
	fmt.Println(message)
	fmt.Scanf("%s", &answer)
	if strings.ToLower(answer) == "y" {
		result = true
	} else if strings.ToLower(answer) == "n" {
		result = false
	}
	return result
}

func main() {
	var passFactory FactoryPass = &Factory{}
	passFactory.ReadConfig()
	passFactory.GeneratePassword()
	passFactory.ShowNewPassword()
}
