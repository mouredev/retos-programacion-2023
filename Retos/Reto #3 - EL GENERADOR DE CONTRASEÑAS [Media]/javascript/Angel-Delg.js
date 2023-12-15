const GeneratePassword = () => {

   const ascii = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "#", "$", "/", ".", "@","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "w", "x", "y", "z",1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,0]
   const password = []

   for(let i = 0; i < Math.round(Math.random() * (16 - 8 + 1) + 8); i++){
      password.push(ascii[ Math.round(Math.random() * ascii.length) ])      
   }

   return password.join('')
}

console.log(GeneratePassword())