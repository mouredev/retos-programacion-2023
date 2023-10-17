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

let pintarASCII (hab: TipoHabitacion) =
    match hab with
    | PUERTA -> "P"
    | VACIO -> " "
    | FANTASMA -> "F"
    | DULCE -> "D"
    | USUARIO -> "U"

let generarFantasma =
    let numCheck = Random().Next(0, 9)
    printfn "Fantasma: %A" numCheck
    numCheck = 5

let construirCasa =
    let casa = Array2D.zeroCreate 4 4
    let rnd = Random()
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
            printf "%A" (pintarASCII casa[col, fila].Tipo)
        printfn ""

let entrarHabitacion (casa: Habitacion[,]) (posicion: Coordenada) =
    let habitacion = casa.[posicion.Columna, posicion.Fila]
    match habitacion.Tipo with
    | PUERTA -> printfn "Entrando a la casa"
    | VACIO -> printfn "Habitacion vacia"
    | FANTASMA -> printfn "Fantasma"
    | DULCE -> printfn "Dulce"
    | USUARIO -> printfn "Usuario"

let rec leerDireccion() =
    printfn "Elige una direccion: norte, sur, este, oeste"
    let direccion = Console.ReadLine()
    match direccion with
    | "norte" -> { Fila = -1; Columna = 0 }
    | "sur" -> { Fila = 1; Columna = 0 }
    | "este" -> { Fila = 0; Columna = 1 }
    | "oeste" -> { Fila = 0; Columna = -1 }
    | _ -> leerDireccion()

let rec moverUsuario (casa: Habitacion[,]) (usuario: Coordenada) =
    let direccion = leerDireccion()
    let nuevoUsuario = { Posicion = { Fila = usuario.Fila + direccion.Fila; Columna = usuario.Columna + direccion.Columna }; Tipo = USUARIO }
    let nuevaCasa = Array2D.copy casa
    nuevaCasa[usuario.Columna, usuario.Fila] <- nuevoUsuario

let casa = construirCasa
mostrarCasa casa
