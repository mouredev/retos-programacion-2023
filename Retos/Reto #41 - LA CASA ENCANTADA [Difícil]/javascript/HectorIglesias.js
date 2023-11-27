/*
 * Este es un reto especial por Halloween.
 * Te encuentras explorando una mansión abandonada llena de habitaciones.
 * En cada habitación tendrás que resolver un acertijo para poder avanzar a la siguiente.
 * Tu misión es encontrar la habitación de los dulces.
 *
 * Se trata de implementar un juego interactivo de preguntas y respuestas por terminal.
 * (Tienes total libertad para ser creativo con los textos)
 *
 * - 🏰 Casa: La mansión se corresponde con una estructura cuadrada 4 x 4
 *   que deberás modelar. Las habitaciones de puerta y dulces no tienen enigma.
 *   (16 habitaciones, siendo una de entrada y otra donde están los dulces)
 *   Esta podría ser una representación:
 *   🚪⬜️⬜️⬜️
 *   ⬜️👻⬜️⬜️
 *   ⬜️⬜️⬜️👻
 *   ⬜️⬜️🍭⬜️
 * - ❓ Enigmas: Cada habitación propone un enigma aleatorio que deberás responder con texto.
 *   Si no lo aciertas no podrás desplazarte.
 * - 🧭 Movimiento: Si resuelves el enigma se te preguntará a donde quieres desplazarte.
 *   (Ejemplo: norte/sur/este/oeste. Sólo deben proporcionarse las opciones posibles)
 * - 🍭 Salida: Sales de la casa si encuentras la habitación de los dulces.
 * - 👻 (Bonus) Fantasmas: Existe un 10% de que en una habitación aparezca un fantasma y
 *   tengas que responder dos preguntas para salir de ella.
 */
function casa_encantada(){
    let fila = ""
    
    let casa = []
    casa[0] = Math.floor(Math.random() * 4)
    
    if(casa[0] == 1 || casa[0] == 2){
        casa[1] = 1
        while (casa[1] == 1 || casa[1] ==2){
            casa[1] = Math.floor(Math.random() * 4)
        }
    }
    else{
        casa[1] = Math.floor(Math.random() * 4)
    }

    let dulces = [Math.floor(Math.random() * 4), Math.floor(Math.random() * 4)]
    while (dulces[0] == casa[0] && dulces[1] == casa[1]){
        dulces = [Math.floor(Math.random() * 4), Math.floor(Math.random() * 4)]
      
    }
   
    for(let i=0; i<4; i++){
        for(let j=0; j<4; j++){
            if(casa[0] == i && casa[1] == j){
                fila += "🚪"
            }
            else if(dulces[0] == i && dulces[1] == j){
                fila += "🍭"
            }
            else{
                fila += "⬜️"
            }
        }
        console.log(fila)
        fila= ""  
    }   

    let dulces_conseguidos = false
    while (dulces_conseguidos == false){
        dulces_conseguidos = juego(casa, dulces)
    }

    console.log("Disfruta de los dulces")
}

function juego(casa, dulces){
    console.log("Estas en la posicion "+casa[0]+"-"+casa[1])
    let respuesta_valida = false
    let respuesta = ""
    let posicion = casa

    while(posicion != dulces){
        let direcciones_posibles = calcular_dir_posibles(posicion)
        console.log("Puedes moverte en las siguientes direcciones: "+direcciones_posibles)

        while(respuesta_valida == false){
            respuesta = prompt("¿Hacia donde quieres moverte? ")
            respuesta_valida = validar_respuesta(respuesta, direcciones_posibles)
        }
        respuesta_valida = false
    
        posicion= calcular_nueva_posicion(respuesta, posicion)
        if(posicion[0] == dulces[0] && posicion[1] == dulces[1]){
            return true
        }
        else{
            let respuesta_acertijo = ""
            let respuesta_valida_acertijo = false
            while(respuesta_valida_acertijo == false){
                respuesta_acertijo = prompt("¿Te está gustando el juego? S/N ")
                respuesta_valida_acertijo = validar_respuesta_acertijo(respuesta_acertijo)
            }  
            respuesta_valida_acertijo = false
        }
    }

    return true
}

function calcular_dir_posibles(array){
    let direcciones_posibles = ""

    if(array[0] != 0){
        direcciones_posibles += "Norte-"
    }

    if(array[1] != 0){
       direcciones_posibles += "Oeste-"
    }

    if(array[1] != 3){
       direcciones_posibles += "Este-"
    }

    if(array[0] != 3){
        direcciones_posibles += "Sur"
    }

    if(direcciones_posibles[direcciones_posibles.length-1] == "-"){
        direcciones_posibles = direcciones_posibles.slice(0, direcciones_posibles.length-1)
    }

    return direcciones_posibles
}

function validar_respuesta(respuesta, direcciones_posibles){
    let array_dir_posibles = direcciones_posibles.split("-")
    for(let i=0; i<array_dir_posibles.length; i++){
        array_dir_posibles[i] = array_dir_posibles[i].toLowerCase()
    }
    respuesta = respuesta.toLowerCase()

    if(respuesta == "norte" || respuesta == "sur" || respuesta == "oeste" || respuesta == "este"){
        if(array_dir_posibles.includes(respuesta)){
            return true
        }
        else{
            console.log("No puedes ir en esa dirección")
            return false
        }
    }
    else{
        console.log("Introduzca un valor válido")
        return false
    }

    
}

function calcular_nueva_posicion(respuesta, posicion){
    respuesta = respuesta.toLowerCase()
    if (respuesta == "norte"){
        posicion = [posicion[0]-1, posicion[1]]
        
    }
    else if (respuesta == "oeste"){
        posicion = [posicion[0], posicion[1]-1]
    }
    else if (respuesta == "este"){
        posicion = [posicion[0], posicion[1]+1]
    }
    else if (respuesta == "sur"){
        posicion = [posicion[0]+1, posicion[1]]
    }
    return posicion
}

function validar_respuesta_acertijo(respuesta){
    respuesta = respuesta.toLowerCase()

    if(respuesta == "s" || respuesta == "n"){
        if(respuesta == "s"){
            return true
        }
        else{
            console.log("Respuesta incorrecta")
            return false
        }
    }
    else{
        console.log("Introduzca un valor válido")
        return false
    }

    
}

casa_encantada()
