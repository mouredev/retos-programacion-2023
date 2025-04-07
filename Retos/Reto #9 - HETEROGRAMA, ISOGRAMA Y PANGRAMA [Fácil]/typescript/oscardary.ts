/*
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.
 * 
 * heterograma: palabra o frase en la que ninguna letra se repite
 *      ejemplo > murciélago, ventilador, abcdef
 * isograma: palabra o frase en la que cada letra aparece el mismo número de veces
 *      ejemplo: murciélago (cada letra esta solo 1 vez), deeded (cada letra esta 3 veces), nana (cada letra esta 2 veces)
 * pangrama: frase que contiene todas las letras del alfabeto al menos una vez
 *      ejemplo: "Benjamín pidió una bebida de kiwi y fajú con exquisita salsa de ciruela."
 *          OJO no tiene g,h,ñ,v,z
 *      ejemplo: "The quick brown fox jumps over the lazy dog."
 * 
 * Al analizar frases, suele ignorarse: Espacios, Mayúsculas/minúsculas, Signos de puntuación
 */

function fnNormalizarTexto(texto: string){
    /**
     * normalize  = Separa letras y tildes
     * replace(1) = Elimina las marcas diacríticas
     * replace(2) = Elimina todo menos letras
     */
    //return texto.normalize("NFD").replace(/[\u0300-\u036f]/g, "").replace(/[^a-zA-ZñÑ]/g, "")
    return texto.normalize("NFD").replace(/[\u0300-\u036f]/g, "").toUpperCase().replace(/[^A-ZÑ]/g, "")
}

function fnEsHeterograma(texto: string){
    //let esHeterograma = true
    let arLetras = fnNormalizarTexto(texto).split("")
    //let letras = [...myText];    //reemplaza el <texto>.split("")
    let myMap: Map<string, number> = new Map()

    /*arLetras.forEach(letra => {
        let cantidad = myMap.get(letra) || 0
        myMap.set(letra, cantidad+1)
    })*/
    for (const letra of arLetras) {
        myMap.set(letra, (myMap.get(letra) || 0) + 1)
    }

    for (let [, valor] of myMap.entries() ) {
        if (valor > 1){
            //esHeterograma = false
            //break
            return false
        }
    }
    //return esHeterograma
    return true
}

function fnEsIsograma(texto: string){
    let arLetras = fnNormalizarTexto(texto)
    let myMap: Map<string, number> = new Map()

    for (let letra of arLetras ){
        myMap.set(letra, (myMap.get(letra) || 0) + 1)
    }

    /*let valorBase: number | null = null
    for (let [, valor] of myMap.entries() ) {
        //let valorNuevo = valor
        if (valorBase == undefined){
            valorBase = valor
        //} else if (valorBase !== valorNuevo){
        } else if (valorBase !== valor){
            return false
        }
    }
    return true*/
    const valores = [...myMap.values()] //devuelve un iterador con todos los valores del mapa.
    return valores.every(item => item === valores[0]) //verifica que todos los elementos del array cumplan una condición.
    
}

function fnEsPangrama(texto: string){
    let abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    /*let myMap: Map<string, number> = new Map()

    //Inicializar Mapa
    for (const letra of abc) {
        myMap.set(letra, 0) 
    }*/
   const myMap = new Map(abc.split("").map(letra => [letra, 0]))

    for (const letra of fnNormalizarTexto(texto)) {
        myMap.set(letra, (myMap.get(letra) || 0) + 1)
    }

    /*
    //Aquì mi versión
    for (const [letra, cantidad] of myMap) {
        if (cantidad>0) {
            myMap.delete(letra)
        }
    }
    
    if (myMap.size > 0){
        return false
    }
    return true
    */

    /*
    //Aquí una versión mas optima
    for (const cantidad of myMap.values()) {
        if (cantidad === 0){
            return false
        }
    }
    return true
    */

    //Aquí la versión final, más más más optimizada
        //devuelve un iterador con todos los valores del mapa.
        //verifica que todos los elementos del array cumplan una condición.
    //return [...myMap.values()].every(cant => cant > 0)
    return ![...myMap.values()].some(cant => cant === 0)
}


let myText9_1: string = "murciélago" //"Hola Mundo, hólá múndó"
console.log("\nEl texto >>" + myText9_1 + "<< es Heterograma?")
console.log("Heterograma: "+fnEsHeterograma(myText9_1))

let myText9_2: string = "Nana" //"Hola Mundo, hólá múndó"
console.log("\nEl texto >>" + myText9_2 + "<< es Isograma?")
console.log("Isograma: "+fnEsIsograma(myText9_2))

let myText9_3: string = "The quick brown fox jumps over the lazy dog." //"paranguaricutirimicuarodol"
console.log("\nEl texto >>" + myText9_3 + "<< es Pantograma?")
console.log("Pantograma: "+fnEsPangrama(myText9_3))
console.log("\n")
