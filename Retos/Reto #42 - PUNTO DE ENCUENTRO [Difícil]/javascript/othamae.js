/*
 * Crea una función que calcule el punto de encuentro de dos objetos en movimiento
 * en dos dimensiones.
 * - Cada objeto está compuesto por una coordenada xy y una velocidad de desplazamiento
 *   (vector de desplazamiento) por unidad de tiempo (también en formato xy).
 * - La función recibirá las coordenadas de inicio de ambos objetos y sus velocidades.
 * - La función calculará y mostrará el punto en el que se encuentran y el tiempo que tardarn en lograrlo.
 * - La función debe tener en cuenta que los objetos pueden no llegar a encontrarse.   
 */


function meetingPoint(object1, object2){
    const dx = object2.x - object1.x
    const vx = object1.vx - object2.vx
    const dy = object2.y - object1.y
    const vy = object1.vy - object2.vy

    const t = (dx * vx + dy * vy) / (vx * vx + vy * vy)

    if (t > 0){
        const x = object1.x + object1.vx * t
        const y = object1.y + object1.vy * t
        const relativeX = object2.x + object2.vx * t
        const relativeY = object2.y + object2.vy * t

        const distance = Math.sqrt((x - relativeX) ** 2 + (y - relativeY) ** 2)

        if (distance < 0.00001) {
            return `Time to meet: ${t}, Coordinates: (${x}, ${y})`
        }      
    }
    return ("They will never meet")
}


// Test:

const object1={
    x:0,
    y:0,
    vx:1,
    vy:1
}

const object2={
    x: 4,
    y:0,
    vx:0,
    vy:1
}

const object3={
    x:0,
    y:0,
    vx:1,
    vy:1
}

const object4={
    x: 2,
    y:0,
    vx:1,
    vy:2
}

const object5={
    x:6,
    y:6,
    vx:-1,
    vy:-1
}

const object6={
    x: 2,
    y:0,
    vx:1,
    vy:2
}

const object7={
    x:6,
    y:6,
    vx:-1,
    vy:-1
}

const object8={
    x: 2,
    y:0,
    vx:2,
    vy:1
}


console.log(meetingPoint(object1, object2)) // Time to meet: 4, Coordinates: (4, 4)
console.log(meetingPoint(object3, object4)) // They will never meet
console.log(meetingPoint(object5, object6)) // Time to meet: 2, Coordinates: (4, 4)
console.log(meetingPoint(object7, object8)) // They will never meet
