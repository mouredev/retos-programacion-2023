open System

type Coordenada = {
    Fila: int
    Columna: int
}

type TipoHabitacion = PUERTA | VACIO | FANTASMA | DULCE | USUARIO

type Habitacion = {
    Posicion: Coordenada
    Tipo: TipoHabitacion
}

Console.OutputEncoding <- System.Text.Encoding.UTF8

let pintarASCII (hab: TipoHabitacion) =
    let characterWidth = 2 // Adjust the width as needed

    match hab with
    | PUERTA -> sprintf "%-*s" characterWidth "🚪"
    | VACIO -> sprintf "%-*s" characterWidth "▒▒"
    | FANTASMA -> sprintf "%-*s" characterWidth "👻"
    | DULCE -> sprintf "%-*s" characterWidth "🍬"
    | USUARIO -> sprintf "%-*s" characterWidth "😀"

let generarFantasma =
    let numCheck = Random().Next(0, 9)
    printfn "Fantasma: %A" numCheck
    numCheck = 5

let construirCasa =
    let casa = Array2D.zeroCreate 4 4
    for col in 0 .. 3 do
        for fila in 0 .. 3 do
            casa[col, fila] <- { Posicion = { Fila = fila; Columna = col }; Tipo = VACIO }
    let puerta = { Posicion = { Fila = 0; Columna = 0 }; Tipo = PUERTA }
    casa[0, 0] <- puerta
    let dulce = { Posicion = { Fila = 3; Columna = 2 }; Tipo = DULCE }
    casa[3, 2] <- dulce
    casa

let mostrarCasa (casa: Habitacion[,]) = 
    for col in 0 .. 3 do
        for fila in 0 .. 3 do
            printf "%s" (pintarASCII casa[col, fila].Tipo)
        printfn ""

let entrarHabitacion (casa: Habitacion[,]) (posicion: Coordenada) =
    let hayFantasma = generarFantasma
    if hayFantasma then
        casa[posicion.Columna, posicion.Fila] <- { Posicion = posicion; Tipo = FANTASMA }
    else
        printfn "No hay fantasma"
    let habitacion: Habitacion = casa.[posicion.Columna, posicion.Fila]
    let hasTerminado =
        match habitacion.Tipo with
        | PUERTA ->             
            printfn "Has salido de la casa"
            false
        | VACIO -> 
            printfn "No hay nada en esta habitacion. Responde la pregunta para continuar"
            casa[posicion.Columna, posicion.Fila] <- { Posicion = posicion; Tipo = USUARIO }
            false
        | FANTASMA -> 
            printfn "Has encontrado un fantasma"
            false
        | DULCE -> 
            printfn "Has encontrado un dulce"
            true
        | USUARIO -> 
            printfn "Ya estas en esta habitacion"
            false
    hasTerminado

let rec leerDireccion(usuario: Coordenada) =
    printfn "Elige una direccion: norte, sur, este, oeste"
    let direccion = Console.ReadLine()
    let coordinate =
        match direccion with
        | "norte" -> { Fila = 0; Columna = -1 }
        | "sur" -> { Fila = 0; Columna = 1 }
        | "este" -> { Fila = 1; Columna =0 }
        | "oeste" -> { Fila = -1; Columna = 0 }
        | _ -> leerDireccion(usuario)
    let nuevaPosicion = { Fila = usuario.Fila + coordinate.Fila; Columna = usuario.Columna + coordinate.Columna }
    if nuevaPosicion.Fila < 0 || nuevaPosicion.Fila > 3 || nuevaPosicion.Columna < 0 || nuevaPosicion.Columna > 3 then
        printfn "No puedes salir de la casa"
        leerDireccion(usuario)
    else
        coordinate


let rec moverUsuario (casaMemo: Habitacion[,]) (casa: Habitacion[,]) (usuario: Coordenada) =
    let direccion = leerDireccion(usuario)   
    let nuevoUsuario = { Posicion = { Fila = usuario.Fila + direccion.Fila; Columna = usuario.Columna + direccion.Columna }; Tipo = USUARIO }
    let memoEstado: Habitacion = casaMemo.[usuario.Columna, usuario.Fila]
    let fin = entrarHabitacion casa nuevoUsuario.Posicion
    casa[usuario.Columna, usuario.Fila] <- memoEstado
    if not fin then
        mostrarCasa casa
        moverUsuario casaMemo casa nuevoUsuario.Posicion
    else
        printfn "Has terminado el juego"

let casa = construirCasa
let casaMemo = Array2D.copy casa
mostrarCasa casa
moverUsuario casaMemo casa { Fila = 0; Columna = 0 }