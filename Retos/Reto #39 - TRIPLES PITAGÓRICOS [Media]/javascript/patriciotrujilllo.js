/*
 * Crea una función que encuentre todos los triples pitagóricos
 * (ternas) menores o iguales a un número dado.
 * - Debes buscar información sobre qué es un triple pitagórico.
 * - La función únicamente recibe el número máximo que puede
 *   aparecer en el triple.
 * - Ejemplo: Los triples menores o iguales a 10 están
 *   formados por (3, 4, 5) y (6, 8, 10).
 */

//la base es (3,4,5) y para obtener los demas se multiplica por un entero para mantener
//la proporcion del triangulo

const tiplesPitagoricos = (numeroMax) =>{
    const a = 3
    const b = 4
    const c = 5

    if(numeroMax<c){
        console.log("No se pude crea ningun triple pitagorico")
    }

    const amountTiples = Math.floor(numeroMax/c)

    let allTiples = []

    for(let i=1; i<=amountTiples;i++){
        const aNew = a*i
        const bNew = b*i
        const cNew = c*i

        const tiple = [aNew,bNew,cNew]

        allTiples=[...allTiples,tiple]
    }
    return allTiples
}
console.log(tiplesPitagoricos(5)) //--> [ [ 3, 4, 5 ] ]
console.log(tiplesPitagoricos(10)) //--> [ [ 3, 4, 5 ], [ 6, 8, 10 ] ]
console.log(tiplesPitagoricos(13)) //--> [ [ 3, 4, 5 ], [ 6, 8, 10 ] ]
console.log(tiplesPitagoricos(15)) //--> [ [ 3, 4, 5 ], [ 6, 8, 10 ], [ 9, 12, 15 ] ]