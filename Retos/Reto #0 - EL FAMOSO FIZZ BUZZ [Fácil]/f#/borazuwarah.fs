(*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 *)

for i in 1 .. 100 do
    match i with
    | i when i % 3 = 0 && i % 5 = 0 -> printfn "FizzBuzz"
    | i when i % 3 = 0 -> printfn "Fizz"
    | i when i % 5 = 0 -> printfn "Buzz"
    | _ -> printfn "%d" i