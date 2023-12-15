const GenerateNumbers = () =>{
   return Math.round(new Date().getMilliseconds() / 10)
}

console.log(GenerateNumbers())