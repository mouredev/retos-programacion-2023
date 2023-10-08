let marcadorJugadorOne = 0;
let marcadorJugadorTwo = 0;
let resultados =["love", "15", "30", "40", "Deuce", "Ventaja"]
let aumetarJuadorOne=0;
let aumetarJuadorTwo=0;
let resuldatoOne;
let resuldatoTwo;
function juegoDeTenis(jugador){
    jugador =jugador.toLowerCase();
    

    if(jugador === 'p1'){
        ++aumetarJuadorOne;
        marcadorJugadorOne = resultados[aumetarJuadorOne];
        marcadorJugadorTwo = resultados[aumetarJuadorTwo];
        resuldatoOne = marcadorJugadorOne + " - "+marcadorJugadorTwo;
        
    }else if(jugador === 'p2'){
        ++aumetarJuadorTwo;
        marcadorJugadorTwo = resultados[aumetarJuadorTwo];
        marcadorJugadorOne = resultados[aumetarJuadorOne];
        resuldatoTwo = marcadorJugadorOne + " - "+marcadorJugadorTwo;
    }
    if(resuldatoOne === resuldatoTwo){
        console.log("Deuce");
    }
    console.log(marcadorJugadorOne + " - "+marcadorJugadorTwo);
}

juegoDeTenis("p1")
juegoDeTenis("p1")
juegoDeTenis("p2")
juegoDeTenis("p2")
juegoDeTenis("p1")
juegoDeTenis("p2")
juegoDeTenis("p1")
juegoDeTenis("p1")


// function jugarTenis(secuencia) {
//     let puntuacion = {
//       P1: 0,
//       P2: 0
//     };
  
//     const puntuaciones = ["Love", 15, 30, 40];
  
//     for (const punto of secuencia) {
//       if (punto === "P1") {
//         puntuacion.P1++;
//       } else if (punto === "P2") {
//         puntuacion.P2++;
//       }
  
//       if (puntuacion.P1 >= 3 && puntuacion.P2 >= 3) {
//         if (puntuacion.P1 === puntuacion.P2) {
//           if (puntuacion.P1 === 3) {
//             console.log("Deuce");
//           } else {
//             console.log("Deuce");
//           }
//         } else if (puntuacion.P1 - puntuacion.P2 === 1) {
//           console.log("Ventaja P1");
//         } else if (puntuacion.P2 - puntuacion.P1 === 1) {
//           console.log("Ventaja P2");
//         } else if (puntuacion.P1 - puntuacion.P2 >= 2) {
//           console.log("Ha ganado el P1");
//           return;
//         } else if (puntuacion.P2 - puntuacion.P1 >= 2) {
//           console.log("Ha ganado el P2");
//           return;
//         }
//       } else {
//         const p1Score = puntuaciones[puntuacion.P1] || puntuaciones[0];
//         const p2Score = puntuaciones[puntuacion.P2] || puntuaciones[0];
//         console.log(`${p1Score} - ${p2Score}`);
//       }
//     }
//   }
  
//   const secuencia = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"];
//   jugarTenis(secuencia);

//   const secuencia2 = ["P1", "P1", "P2", "P2", "P1","P2", "P1", "P1", "P2", "P1"];
//   jugarTenis(secuencia2);

//   const secuencia3 = ["P1", "P1"];
//   jugarTenis(secuencia3);

//   const secuencia4 = ["P1", "P1","P1", "P1","P1", "P1"];
//   jugarTenis(secuencia4);