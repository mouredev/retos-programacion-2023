/* Función marcador hasta caso de empate */
function match(sequence) {
    const points = ['Love', 15, 30, 40]
    let ballsP1 = 0
    let ballsP2 = 0
    for (let i = 0; i < 6; i++) {
         if (sequence[i] === 'P1') {
             ballsP1++
             if (ballsP1 === 4) {
                 console.log('Ha ganado el P1') 
                 break
             }
         } else {
             ballsP2++
             if (ballsP2 === 4) {
                 console.log('Ha ganado el P2') 
                 break
             }
         }
         if ((points[ballsP1] === 40) && (points[ballsP2] === 40)) {
             console.log('Deuce')
         } else {
             console.log(`${points[ballsP1]} - ${points[ballsP2]}`)
         } 
     }
 }
 
 
 //Función del marcador una vez hay empate
 function desempate(sequence) {
     let ventajaP1 = 0
     let ventajaP2 = 0
     for (let i = 0; i < sequence.length; i++) {
         if (sequence[i] === 'P1') {
             ventajaP1++
         } else {
             ventajaP2++
         }
         if ((ventajaP1 - ventajaP2 === 1) || (ventajaP2 - ventajaP1 === 1)) {
             console.log(`Ventaja ${sequence[i]}`)
         } else if ((ventajaP1 - ventajaP2 === 0) || (ventajaP2 - ventajaP1 === 0)) {
             console.log('Deuce')
         } else {
             console.log(`Ha ganado el ${sequence[i]}`)
             break
         }
     }
 }
 
 // Función marcador total de partido
 function tennisMatch(sequence) {
     match(sequence)
     const desempateSequence = sequence.slice(6, sequence.length)
     desempate(desempateSequence)
 }
 
 const puntosPartido = ['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P2', 'P2', 'P2']
 
 tennisMatch(puntosPartido)