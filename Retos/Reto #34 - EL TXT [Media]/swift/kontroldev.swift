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

import Foundation

func getInput() -> String {
    let keyboard = FileHandle.standardInput
    let inputData = keyboard.availableData
    return String(data: inputData, encoding: .utf8)?.trimmingCharacters(in: .newlines) ?? ""
}

func main() {
    let fileURL = URL(fileURLWithPath: "text.txt")

    var fileContent = ""
    do {
        fileContent = try String(contentsOf: fileURL)
    } catch {
        print("El archivo no existe. Se creará uno nuevo.")
    }

    var choice: Int = 0
    print("Elige una opción:")
    print("1. Continuar escribiendo")
    print("2. Borrar contenido y empezar de nuevo")

    if let input = Int(getInput()) {
        choice = input
    } else {
        print("Opción inválida.")
        return
    }

    if choice == 2 {
        do {
            try "".write(to: fileURL, atomically: false, encoding: .utf8)
        } catch {
            print("No se pudo borrar el contenido del archivo.")
            return
        }
    } else if choice == 1 {
        print("Contenido actual del archivo:\n\(fileContent)")
    } else {
        print("Opción inválida.")
        return
    }

    print("Introduce texto. Presiona Enter para guardar una nueva línea. Ctrl+D para finalizar:")
    while let input = readLine() {
        do {
            try input.appendLineToURL(fileURL: fileURL)
            print("Texto guardado en el archivo.")
        } catch {
            print("No se pudo guardar el texto en el archivo.")
            return
        }
    }
}

extension String {
    func appendLineToURL(fileURL: URL) throws {
        try (self + "\n").write(to: fileURL, atomically: true, encoding: .utf8)
    }
}

main()

