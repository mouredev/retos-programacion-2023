package main

import (
	"database/sql"

	_ "github.com/go-sql-driver/mysql"
)

func main() {
	db, err := sql.Open("mysql", "mouredev_read:mouredev_pass@tcp(mysql-5707.dinaserver.com:3306)/moure_test")
	if err != nil {
		panic(err.Error())
	}
	defer db.Close()

	rows, err := db.Query("SELECT * FROM challenges")
	if err != nil {
		panic(err.Error())
	}
	defer rows.Close()

	for rows.Next() {
		var id int
		var name, difficulty, date string

		err = rows.Scan(&id, &name, &difficulty, &date)
		if err != nil {
			panic(err.Error())
		}
		println(id, name, difficulty, date)
	}
}
