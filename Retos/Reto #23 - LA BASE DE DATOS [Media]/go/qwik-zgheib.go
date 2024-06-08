package main

import (
	"database/sql"
	"fmt"
	"log"

	_ "github.com/go-sql-driver/mysql"
)

type DBConnector interface {
	Connect() (*sql.DB, error)
	Query(db *sql.DB, query string) (*sql.Rows, error)
}

type Printer interface {
	Print(rows *sql.Rows) error
}

type MySQLConnector struct {
	DSN string
}

func NewMySQLConnector(dsn string) *MySQLConnector {
	return &MySQLConnector{DSN: dsn}
}

func (mc *MySQLConnector) Connect() (*sql.DB, error) {
	db, err := sql.Open("mysql", mc.DSN)
	if err != nil {
		return nil, err
	}
	return db, nil
}

func (mc *MySQLConnector) Query(db *sql.DB, query string) (*sql.Rows, error) {
	rows, err := db.Query(query)
	if err != nil {
		return nil, err
	}
	return rows, nil
}

type SimplePrinter struct{}

func NewSimplePrinter() *SimplePrinter {
	return &SimplePrinter{}
}

func (sp *SimplePrinter) Print(rows *sql.Rows) error {
	columns, err := rows.Columns()
	if err != nil {
		return err
	}

	values := make([]sql.RawBytes, len(columns))
	scanArgs := make([]interface{}, len(values))
	for i := range values {
		scanArgs[i] = &values[i]
	}

	for rows.Next() {
		err = rows.Scan(scanArgs...)
		if err != nil {
			return err
		}

		var value string
		for i, col := range values {
			if col == nil {
				value = "NULL"
			} else {
				value = string(col)
			}
			fmt.Printf("%s: %s\n", columns[i], value)
		}
		fmt.Println()
	}
	return nil
}

func main() {
	dsn := "mouredev_read:mouredev_pass@tcp(mysql-5707.dinaserver.com:3306)/moure_test"
	connector := NewMySQLConnector(dsn)
	printer := NewSimplePrinter()

	db, err := connector.Connect()
	if err != nil {
		log.Fatalf("Error connecting to the database: %v", err)
	}
	defer db.Close()

	query := "SELECT * FROM `challenges`"
	rows, err := connector.Query(db, query)
	if err != nil {
		log.Fatalf("Error executing query: %v", err)
	}
	defer rows.Close()

	err = printer.Print(rows)
	if err != nil {
		log.Fatalf("Error printing query results: %v", err)
	}
}
