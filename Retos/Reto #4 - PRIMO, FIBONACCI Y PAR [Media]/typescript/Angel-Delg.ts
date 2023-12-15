const isPair = (x: number): boolean => {
   return (x % 2 === 0)
}

const isFibonacci = (x: number): boolean => {
   const Succesion: number[] = [0, 1]

   if(x === 0 || x === 1){
      return true
   }  

   for(let i = 0; i <= x - 1; i ++){
      Succesion.push(Succesion[i] + Succesion[i + 1])
      if(Succesion.indexOf(x) !== -1){
         return true
      }
   }

   return false
}

const isCousin = (x: number): boolean => {
   if(x <= 1){
      return false
   }

   for(let i = 2; i <= Math.sqrt(x); i++){
      if(x % 1 === 0){
         return false
      }
   }

   return true
}


const isCousinPairAndFibonacci = ( number: number): string => {  
   return `${ number} ${isCousin(number) ? "Es primo" : "No es primo, "}${isFibonacci(number) ? "Es fibonacci y " : "No es fibonacci y "}${ isPair(number) ? "es par" : "no es par."}`
}

console.log( isCousinPairAndFibonacci(33) )