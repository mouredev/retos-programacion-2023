/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */


function generar_contrasena(longitud, incluir_mayusculas, incluir_numeros, incluir_simbolos){
    if(longitud<8 || longitud >16)
        return "Error: La longitud de la contraseña debe estar entre 8 y 16."

    contraseñas = ""
    temp = 0
    for (let i = 0; i < longitud; i++) {
        temp = numeroAleatorio(temp)

        if(incluir_mayusculas.toUpperCase() ==="SI" && temp === 1)
            contraseñas +=  caracterAleatorioEntreNumeros(65, 90)    
        else if(incluir_numeros.toUpperCase() ==="SI" && temp === 2)
            contraseñas +=  caracterAleatorioEntreNumeros(48, 57)
        else if(incluir_simbolos.toUpperCase() ==="SI" && temp === 3)  
            contraseñas +=  caracterAleatorioEntreNumeros(33, 47) 
        else
            contraseñas +=  caracterAleatorioEntreNumeros(97, 122)
    }
    return contraseñas
}

function numeroAleatorio(temp){
    aleatorio = Math.floor(Math.random() * 4) + 1;
    if(temp === aleatorio)
        return numeroAleatorio(aleatorio)
    else
        return aleatorio
}
    
function caracterAleatorioEntreNumeros(num1, num2) {
    // Obtener el rango y generar un índice aleatorio
    const rango = Math.abs(num2 - num1) + 1;
    const indiceAleatorio = Math.floor(Math.random() * rango);
    // Obtener el carácter correspondiente al índice aleatorio
    const caracterAleatorio = String.fromCharCode(Math.min(num1, num2) + indiceAleatorio);
  
    // Devolver el carácter aleatorio
    return caracterAleatorio;
  }


console.log(generar_contrasena(8,"si","si","si"))
console.log(generar_contrasena(9,"no","si","si"))
console.log(generar_contrasena(10,"si","no","si"))
console.log(generar_contrasena(11,"si","si","no"))
console.log(generar_contrasena(12,"no","no","no"))
console.log(generar_contrasena(13,"no","si","si"))
console.log(generar_contrasena(200,"no","si","si"))
//console.log(caracterAleatorioEntreNumeros(122, 122))
//const numeroAleatorio = Math.floor(Math.random() * 5) + 1;

//console.log(numeroAleatorio);