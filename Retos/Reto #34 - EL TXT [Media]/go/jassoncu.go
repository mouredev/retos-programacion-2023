/*
 * Crea un programa capaz de interactuar con un fichero TXT.
 * IMPORTANTE: El fichero TXT NO debe subirse como parte de la corrección.
 * Únicamente el código.
 *
 * - Si no existe, debe crear un fichero llamado "text.txt".
 * - Desde el programa debes ser capaz de introducir texto por consola y guardarlo
 *   en una nueva línea cada vez que se pulse el botón "Enter".
 * - Si el fichero existe, el programa tiene que dar la opción de seguir escribiendo
 *   a continuación o borrar su contenido y comenzar desde el principio.
 * - Si se selecciona continuar escribiendo, se tiene que mostrar por consola
 *   el texto que ya posee el fichero.
 */

package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	// Nombre del archivo TXT
	fileName := "text.txt"

	// Verificamos si el archivo existe
	_, err := os.Stat(fileName)

	// Abrimos el archivo en modo de escritura, creándolo si no existe
	file, err := os.OpenFile(fileName, os.O_WRONLY|os.O_APPEND|os.O_CREATE, 0644)
	if err != nil {
		fmt.Println("Error al abrir el archivo:", err)
		return
	}
	defer file.Close()

	// Si el archivo no existe, mostramos un mensaje inicial
	if os.IsNotExist(err) {
		fmt.Println("El archivo no existe. Se ha creado uno nuevo.")
	} else {
		fmt.Println("El archivo ya existe. ¿Desea borrar su contenido y comenzar desde el principio? (S/N)")
		var respuesta string
		fmt.Scanln(&respuesta)
		respuesta = strings.TrimSpace(strings.ToUpper(respuesta))
		if respuesta == "S" {
			// Borramos el contenido del archivo
			err := os.Truncate(fileName, 0)
			if err != nil {
				fmt.Println("Error al borrar el contenido del archivo:", err)
				return
			}
			fmt.Println("El contenido del archivo ha sido borrado.")
		}
	}

	scanner := bufio.NewScanner(os.Stdin)
	for {
		fmt.Print("Escribe una línea de texto (o presiona Enter para salir): ")
		scanner.Scan()
		text := scanner.Text()
		if text == "" {
			break
		}

		_, err := fmt.Fprintln(file, text)
		if err != nil {
			fmt.Println("Error al escribir en el archivo:", err)
			return
		}
	}
	fmt.Println("Adiós. Se ha guardado el texto en el archivo.")
}
