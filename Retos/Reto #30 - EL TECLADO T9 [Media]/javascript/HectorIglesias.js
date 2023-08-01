/*
 * Los primeros dispositivos móviles tenían un teclado llamado T9
 * con el que se podía escribir texto utilizando únicamente su
 * teclado numérico (del 0 al 9).
 *
 * Crea una función que transforme las pulsaciones del T9 a su
 * representación con letras.
 * - Debes buscar cuál era su correspondencia original.
 * - Cada bloque de pulsaciones va separado por un guión.
 * - Si un bloque tiene más de un número, debe ser siempre el mismo.
 * - Ejemplo:
 *     Entrada: 6-666-88-777-33-3-33-888
 *     Salida: MOUREDEV
 * 
 * 2 --> A,B,C
 * 3 --> D,E,F
 * 4 --> G,H,I
 * 5 --> J,K,L
 * 6 --> M,N,O
 * 7 --> P,Q,R,S
 * 8 --> T,U,V
 * 9 --> W,X,Y,Z
 */

function teclado_t9(entrada){
    let salida= ""
    let aux= entrada.split("-")

    if(aux.length > 0){
        for(let i=0; i<aux.length;i++){
            if(aux[i][0]=="2"){
                salida= salida+filtro(aux[i], 2)
            }
            else if(aux[i][0]=="3"){
                salida= salida+filtro(aux[i], 3)
            }
            else if(aux[i][0]=="4"){
                salida= salida+filtro(aux[i], 4)
            }
            else if(aux[i][0]=="5"){
                salida= salida+filtro(aux[i], 5)
            }
            else if(aux[i][0]=="6"){
                salida= salida+filtro(aux[i], 6)
            }
            else if(aux[i][0]=="7"){
                salida= salida+filtro(aux[i], 7)
            }
            else if(aux[i][0]=="8"){
                salida= salida+filtro(aux[i], 8)
            }
            else if(aux[i][0]=="9"){
                salida= salida+filtro(aux[i], 9)
            }

        }
    }
    if(salida.length!=aux.length){
        salida= "La cadena introducida es erronea"
    }
    return salida
}

function filtro(cadena_filtro, numero){
    let tam_cadena= cadena_filtro.length
  
    if(tam_cadena==1){
        return asignar_numero(numero, tam_cadena)
    }
    else{
        if(comprobar_cadena(cadena_filtro)){
            if(tam_cadena==2){
                return asignar_numero(numero, tam_cadena)
            }
            else if(tam_cadena==3){
                return asignar_numero(numero, tam_cadena)
            }   
            else{
                return asignar_numero(numero, tam_cadena)
            }
        }
        else{
            salida= ""
            return salida
        }
    }
}

function comprobar_cadena(cadena){
    for(let i=0;i<cadena.length;i++){
        if(cadena[i]!=cadena[0]){
            return false
        }
    }

    return true
}

function asignar_numero(numero, repeticiones){
    switch(numero){
        case 2:
            if(repeticiones==1){return "A"}
            if(repeticiones==2){return "B"}
            if(repeticiones==3){return "C"}
            break
        case 3:
            if(repeticiones==1){return "D"}
            if(repeticiones==2){return "E"}
            if(repeticiones==3){return "F"}
            break
        case 4:
            if(repeticiones==1){return "G"}
            if(repeticiones==2){return "H"}
            if(repeticiones==3){return "I"}
            break
        case 5:
            if(repeticiones==1){return "J"}
            if(repeticiones==2){return "K"}
            if(repeticiones==3){return "L"}
            break
        case 6:
            if(repeticiones==1){return "M"}
            if(repeticiones==2){return "N"}
            if(repeticiones==3){return "O"}
            break
        case 7:
            if(repeticiones==1){return "P"}
            if(repeticiones==2){return "Q"}
            if(repeticiones==3){return "R"}
            if(repeticiones==4){return "S"}
            break
        case 8:
            if(repeticiones==1){return "T"}
            if(repeticiones==2){return "U"}
            if(repeticiones==3){return "V"}
            break
        case 9:
            if(repeticiones==1){return "W"}
            if(repeticiones==2){return "X"}
            if(repeticiones==3){return "Y"}
            if(repeticiones==3){return "Z"}
            break
    }
}

console.log(teclado_t9("6-666-88-777-33-3-33-888"))
console.log(teclado_t9("6-676-88-777-33-3-33-888"))