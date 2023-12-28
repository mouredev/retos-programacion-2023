const crearEscalera = (escalones: number) => {
    let piso = '__'

    if (escalones > 0) {
        let escaleras = new Array(escalones).fill('_|');
        escaleras.push(piso)
        escaleras = escaleras.map((elemento, indice) => " ".repeat(indice * 2) + elemento)
        return escaleras.reverse().join('\n')
    }
    escalones = Math.abs(escalones)
    let escaleras = new Array(escalones).fill('|_');
    escaleras.push(piso)
    escaleras = escaleras.reverse().map((elemento, indice) => " ".repeat(indice * 2) + elemento)
    return escaleras.join('\n')
}

const reto = (escalones: number) => {
    console.log(crearEscalera(escalones));
}

reto(-4)
reto(0)
reto(4)