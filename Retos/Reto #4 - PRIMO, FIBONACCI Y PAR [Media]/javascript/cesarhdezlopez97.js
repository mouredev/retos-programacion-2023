function par(numero) {
    return numero % 2 === 0
  }
  
  function primo(numero) {
    let k = 2
    while (k <= Math.sqrt(numero)) {
      if (numero % k === 0) {
        return false
      }
      k++
    }
    return true
  }
  
  function fibonacci(numero) {
    return (Math.sqrt(5 * numero * numero + 4) % 1 === 0 ||
            Math.sqrt(5 * numero * numero - 4) % 1 === 0)
  }
  
  function comprobarNumero(numero){
      var resultado = ''
       if(primo(numero)){
      resultado +='es primo, '
      }else
      resultado +='no es primo, '
      if(fibonacci(numero)){
      resultado +='es fibonacci '
      }else
      resultado +='no es fibonacci '
      if (par(numero)){
      resultado += 'y es par'
      }else
      resultado +='y es impar'
      return numero +' '+ resultado
      
  }
  
  console.log(comprobarNumero(2))  // 2 es primo, es fibonacci y es par
  console.log(comprobarNumero(7))  // 7 es primo, no es fibonacci y es impar