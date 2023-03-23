
let generarClave = (tamano = 8, mayusculas = false, numeros = false , especiales = false) => { 

    if (tamano < 8 || tamano > 16)
        return "El tamaño de la clave no es correcto"
    let clave = "";
    let caracteres = "abcdefghijklmnopqrstuvwxyz";
    if (mayusculas) {
        caracteres += "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    }
    if (numeros) {
        caracteres += "0123456789";
    }
    if (especiales) {
        caracteres += "¡!#$%&/()=?¿*+[]{}-_.:,;@";
    }
    for (let i = 0; i < tamano; i++) {
        clave += caracteres.charAt(Math.floor(Math.random() * caracteres.length));
    }
    return clave;
}

console.log(generarClave(10, true, true, true));
console.log(generarClave());
console.log(generarClave(15, true, true, false));
console.log(generarClave(3, true, true, false));
console.log(generarClave(20, true, true, false));