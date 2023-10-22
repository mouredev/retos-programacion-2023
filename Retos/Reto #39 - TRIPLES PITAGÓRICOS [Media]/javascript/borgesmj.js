const triplesPitagoricos = (limite) => {
    if (isNaN(limite) || limite < 0){
      return 'invalid entry!'
    }
    // creamos el array de los resultados
    const result = [];
    // Creamos un array donde tendrá almacenado todos los
    // numeros al cuadrado
    const numSquare = [];
    for (i = 1; i <= limite; i++){
      numSquare.push(Math.pow(i, 2));
    }
    // Evaluamos en cada item del arreglo contenga la suma de dos de sus elementos
    numSquare.forEach((item, index) => {
      for (let i = index + 1; i < numSquare.length; i++){
        if (numSquare.includes(item + numSquare[i])){
          let a = Math.sqrt(item);
          let b = Math.sqrt(numSquare[i]);
          let c = Math.sqrt(item + numSquare[i]);
          result.push([a, b, c]);
        }
      }
    });
    return  result;
  };
  
  console.log(triplesPitagoricos(10));