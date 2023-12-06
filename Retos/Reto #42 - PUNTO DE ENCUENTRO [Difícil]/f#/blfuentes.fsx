// /*
//  * Crea una función que calcule el punto de encuentro de dos objetos en movimiento
//  * en dos dimensiones.
//  * - Cada objeto está compuesto por una coordenada xy y una velocidad de desplazamiento
//  *   (vector de desplazamiento) por unidad de tiempo (también en formato xy).
//  * - La función recibirá las coordenadas de inicio de ambos objetos y sus velocidades.
//  * - La función calculará y mostrará el punto en el que se encuentran y el tiempo que tardarn en lograrlo.
//  * - La función debe tener en cuenta que los objetos pueden no llegar a encontrarse.   
//  */

type Position = {
    X: int
    Y: int
}
type Element = {
    Position: Position
    Speed: Position
}

let getDistance (posA: Position) (posB: Position) =
    sqrt((pown((float)(posA.X - posB.X)) 2) + (pown((float)(posA.Y - posB.Y)) 2))

let rec getCollision (posA: Element) (posB: Element) (steps: int)=    
    let initialDistance = getDistance posA.Position posB.Position
    
    if initialDistance = 0 then
        (steps, posA.Position)
    else
        let newPosA = { X = posA.Position.X + posA.Speed.X; Y = posA.Position.Y + posA.Speed.Y }
        let newPosB = { X = posB.Position.X + posB.Speed.X; Y = posB.Position.Y + posB.Speed.Y }
        let newDistance = getDistance newPosA newPosB
        if initialDistance <= newDistance then
            raise (System.Exception("No hay colisión!"))
        else
            getCollision { Position = newPosA; Speed = posA.Speed } { Position = newPosB; Speed = posB.Speed } (steps + 1)
    

// Sample usage
let pointA = { Position = { X = 0; Y = 0 }; Speed = { X = 2; Y = 1} }
let pointB = { Position = {X = 0; Y = 6 }; Speed = { X = 2; Y = -2} }

let (steps, collision) = getCollision pointA pointB 0