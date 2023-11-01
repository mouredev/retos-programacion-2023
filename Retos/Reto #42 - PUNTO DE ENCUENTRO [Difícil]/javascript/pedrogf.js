/*
 * Crea una función que calcule el punto de encuentro de dos objetos en movimiento
 * en dos dimensiones.
 * - Cada objeto está compuesto por una coordenada xy y una velocidad de desplazamiento
 *   (vector de desplazamiento) por unidad de tiempo (también en formato xy).
 * - La función recibirá las coordenadas de inicio de ambos objetos y sus velocidades.
 * - La función calculará y mostrará el punto en el que se encuentran y el tiempo que tardarn en lograrlo.
 * - La función debe tener en cuenta que los objetos pueden no llegar a encontrarse.   
 */

function objectMetting (obj1, obj2) {
    //Calcula la distancia entre los objetos en la posición inicial (previous) y en la t+1(actual).
    let previousDistance = Math.sqrt((obj2.x - obj1.x)**2 + (obj2.y - obj1.y)**2)
    let actualDistance = Math.sqrt(((obj2.x + obj2.vx) - (obj1.x + obj1.vx))**2 + (((obj2.y + obj2.vy) - (obj1.y + obj1.vy))**2))
    let t=1
    let newPositionObj1x, newPositionObj1y, newPositionObj2x, newPositionObj2y
    
    while (true) {
        t++
        // Calcula la posición de los objetos en función del tiempo.
        newPositionObj1x = obj1.x + obj1.vx * t
        newPositionObj1y = obj1.y + obj1.vy * t
        newPositionObj2x = obj2.x + obj2.vx * t
        newPositionObj2y = obj2.y + obj2.vy * t

        if(actualDistance >= previousDistance) { // Si la distancia entre los objetos aumenta o es igual nunca se encontrarán.
            return 'Los vectores nunca se encontraán' 
        } else if (newPositionObj1x === newPositionObj2x && newPositionObj1y === newPositionObj2y) { // avanzamos la posición multiplicando por el tiempo
            // Si la posición de ambos objetos es la misma, se han encontraron.
            return`Los vectores se han encontrado en la posición [${newPositionObj1x}, ${newPositionObj1y}] en un tiempo de ${t} unidades`
        }else{
            //recalculamos las nuevas posiciones de los objetos.
            previousDistance = actualDistance
            actualDistance = Math.sqrt((newPositionObj2x - newPositionObj1x)**2 + ((newPositionObj2y - newPositionObj1y)**2))
        }
    }
}

// Objetos que se encuentran.
let objeto1 = {
    x: 0,
    y: 0,
    vx: 1,
    vy: 1,
}
let objeto2 = {
    x: 5,
    y: 0,
    vx: 0,
    vy: 1,
}
console.log(objectMetting(objeto1, objeto2))

// Objetos con vectores paralelos que nunca se encuentran.
let objeto3 = {
    x: 2,
    y: 0,
    vx: 0,
    vy: 1,
}
let objeto4 = {
    x: 4,
    y: 0,
    vx: 0,
    vy: 1,
}
console.log(objectMetting(objeto3, objeto4))

// Objetos que se cruzan pero no en el mismo instante
let objeto5 = {
    x: 2,
    y: 2,
    vx: 1,
    vy: 1,
}
let objeto6 = {
    x: 4,
    y: 0,
    vx: 0,
    vy: 1,
}
console.log(objectMetting(objeto5, objeto6))

