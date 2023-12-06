package main

import (
	"database/sql"
	"fmt"
	_ "github.com/go-sql-driver/mysql"
)

type Challenge struct {
	Id         int
	Name       string
	Difficulty string
	Date       string
}

func printTableData() {
	fmt.Println("connecting with MySql database")
	source := "mouredev_read:mouredev_pass@(mysql-5707.dinaserver.com)/moure_test"

	db, err := sql.Open("mysql", source)
	if err != nil {
		panic(err.Error())
	}
	defer db.Close()

	results, err := db.Query("SELECT * FROM challenges")
	if err != nil {
		panic(err.Error())
	}

	defer results.Close()

	columns, err := results.Columns()
	if err != nil {
		panic(err.Error())
	}
	fmt.Println(columns)

	listRows := []Challenge{}
	for results.Next() {
		var challenge Challenge
		err := results.Scan(&challenge.Id, &challenge.Name,
			&challenge.Difficulty, &challenge.Date)
		if err != nil {
			panic(err.Error())
		}
		listRows = append(listRows, challenge)

		fmt.Printf("%+v\n", challenge)
	}

	fmt.Println(listRows)

}

func main() {
	go printTableData()
	var name string
	fmt.Scan(&name)
}
