// Crea un programa que sea capaz de solicitarte un número y se
// encargue de imprimir su tabla de multiplicar entre el 1 y el 10.
// - Debe visualizarse qué operación se realiza y su resultado.
//    Ej: 1 x 1 = 1
//        1 x 2 = 2
//        1 x 3 = 3
//        ... 

// Solución
let rec ReadNumber() =
    printf "Introduce un número: "
    let userInput = System.Console.ReadLine()
    match System.Int32.TryParse(userInput) with
    | (true, value) -> value
    | _ -> ReadNumber()

let printTable(number: int) =
    [1..10] |> List.iter(fun v -> printfn "%d x %d = %d" number v (number * v))

let number = ReadNumber()
printTable(number)