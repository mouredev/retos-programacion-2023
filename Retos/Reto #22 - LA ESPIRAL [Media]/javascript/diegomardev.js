//- Símbolos permitidos: ═ ║ ╗ ╔ ╝ ╚
function espiral(n) {
  /*
  (0,0),(0,1),(0,2),(0,3),(0,4)
  (1,0),(1,1),(1,2),(1,3),(1,4)
  (2,0),(2,1),(2,2),(2,3),(2,4)
  (3,0),(3,1),(3,2),(3,3),(3,4)
  (4,0),(4,1),(4,2),(4,3),(4,4)
  */
  let espiral_tramo="";
  for(let Y=0; Y<=n-1; Y++){
    /* let espiral_tramo=""; */
    let vertical=true;
    for(let X=0; X<=n-1; X++){
      if(X===Y-1 && Y<n/2){
        espiral_tramo = espiral_tramo+"╔"
        vertical=false;
      }
      else if(X+Y===n-1){
        if(Y<n/2){
          espiral_tramo = espiral_tramo+"╗"
          /*if(X<n-1){*/vertical=true/*}*/
        }
        else{
          espiral_tramo = espiral_tramo+"╚"
          vertical=false;
        }
      }
      else if(X===Y && Y>=n/2){
        espiral_tramo = espiral_tramo+"╝"
        vertical=true;
      }
      else if(Y===0){espiral_tramo = espiral_tramo+"═"}
      else if(vertical){espiral_tramo = espiral_tramo+"║"}
      else{
        espiral_tramo = espiral_tramo+"═"
        vertical=false;
      }
    }
    espiral_tramo = espiral_tramo+"\n"//ponemos retorno de carro para que pase a la siguiente fila
  }
  return espiral_tramo;
}
console.log(espiral(10));