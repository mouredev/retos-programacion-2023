const fibonacci_of = (n) =>{
  if (n < 2) {
    return n
  }
  else{
    return fibonacci_of(n-1) + fibonacci_of(n-2)
  }

}




const eval_fibo = (n) =>{
  var fibolist = []
  for (var i = 0; i < n; i++){
  fibolist.push(fibonacci_of(i))
  }

  return true ? fibolist.includes(n) : false

}



const is_prime = (n) =>{
  if (n > 2){
    for (var i = 2; i < n; i++){
      return false ? (n%i == 0) : true    
    }
  }else{
    return false
  }
}


const is_par = (n) =>{
  return true ? (n%2 === 0) : false
}

const evaluation = () =>{
  var n = parseInt(prompt("introduzca un numero: "))
  
  if (typeof n === 'number'){
    
    if(eval_fibo(n)){
      console.log(`${n} es Fibonnacci`)
    }else{
      console.log(`${n} no es Fibonnacci`)
    }
    if(is_prime(n)){
      console.log(`${n} es primo`)
    }else{
      console.log(`${n} no es primo`)
    }
    if(is_par(n)){
      console.log(`${n} es par`)
    }else{
      console.log(`${n} no es par`)
    }
    
    
    

  }else{
    alert("intrdujo un dato valido")
  }
}
 
evaluation()
