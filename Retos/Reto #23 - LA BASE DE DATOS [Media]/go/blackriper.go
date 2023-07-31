package main

import (
	"database/sql"
	"fmt"
	_ "github.com/go-sql-driver/mysql"
	"time"
)

/*
 1.-Creamos modulo de go con go mod init nombre_del_modulo
 2.-Instalamos driver go de mysql go get -u github.com/go-sql-driver/mysql
 3.-No o olviden agregar la linea  _ "github.com/go-sql-driver/mysql en el import de lo contrario no recnocera el driver mysql"
 4.-Happy coding
*/

// creamos una interface para los diferentes metodos de interaccion con la base de datos
type Database interface {
	ConnectDatabase()
	GetChallengs() []Challenge
}

// creamos tipos de datos para la informacion que proviene de la base de datos
type Challenge struct {
	ID         int
	Name       string
	Difficulty string
	Date       time.Time
}

// implementando interface
type Sql struct {
	DB *sql.DB
}

func (sq *Sql) ConnectDatabase() {
	db, err := sql.Open("mysql", "mouredev_read:mouredev_pass@tcp(mysql-5707.dinaserver.com:3306)/moure_test?parseTime=true")

	if err != nil {
		panic(err.Error())
	}
	sq.DB = db
}

func (sq *Sql) GetChallengs() []Challenge {
	var challenges []Challenge

	res, err := sq.DB.Query("SELECT * FROM challenges")
	defer res.Close()

	if err != nil {
		panic(err.Error())
	}

	for res.Next() {
		var ch Challenge
		err := res.Scan(&ch.ID, &ch.Name, &ch.Difficulty, &ch.Date)
		if err != nil {
			panic(err.Error())
		}
		challenges = append(challenges, ch)
	}
	defer sq.DB.Close()
	return challenges
}

// funcion para imprimir datos
func PrintChallenges() {
	var db Database = &Sql{}
	db.ConnectDatabase()
	for _, ch := range db.GetChallengs() {
		fmt.Printf("%v | %v | %v | %v \n", ch.ID, ch.Name, ch.Difficulty, ch.Date)
	}
}

func main() {
	PrintChallenges()
}
