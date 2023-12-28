 let juego = new Array("P1","P1","P2","P1","P2","P2","P1","P2","P2","P2");

      function ganadorJuego(arr) {
        let jeuP1 = new Array("Love", "15", "30", "40", "Advantage");
        let jeuP2 = new Array("Love", "15", "30", "40", "Advantage");

        for (let i = 0, j = 0, k = 0; i < arr.length + 1; i++) {
          if (k == 3 && j == 3) {
            console.log("Deuce");
          } else if (k > 4 || (k == 4 && j < 3)) {
            console.log("Juego para J2");
            i = arr.length + 99;
          } else if ((k < 3 && j == 4) || j > 4) {
            console.log("Juego para J1");
            i = arr.length + 99;
          } else {
            console.log(jeuP1[j] + " - " + jeuP2[k]);
          }
          if (j == 4 && arr[i] == "P2") {
            j--;
          } else if (k == 4 && arr[i] == "P1") {
            k--;
          } else {
            if (arr[i] == "P1") {
              j++;
            } else if (arr[i] == "P2") {
              k++;
            }
          }
        }
      }
      juego.every(puntos);
      function puntos(punto) {
        return punto == "P1" || punto == "P2";
      }

      if (juego.every(puntos) == true) {
        ganadorJuego(juego);
      } else {
        console.log("Error en alguno de los puntos");
      }
