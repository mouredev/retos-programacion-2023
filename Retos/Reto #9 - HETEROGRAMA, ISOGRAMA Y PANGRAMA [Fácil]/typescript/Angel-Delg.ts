const isHeterograma = (text: string): boolean =>{
   const splitText: string[] = text.toLowerCase().split('')
   const set: Set<string> = new Set<string>()

   for(let i: number = 0; i < text.length; i++){
      if(set.has(splitText[i])){
         return false
      }
      set.add(splitText[i])
   }

   return true
}

const isIsograma = (text: string):boolean => {
   const chars: string[] = text.toLowerCase().split("");
   const seen: Set<string> = new Set();

   for (const char of chars) {
      if (seen.has(char)) {
         return false;
      }
      seen.add(char);
   }

  return true;
}

const isPangrama = (text: string): boolean => {
   const setLetters = new Set<string>()

   for(let i = 0; i < text.length; i++){
      if(text[i] !== ' ' && text[i] !== '?' && text[i] !== '.' && text[i] !== ',' && !setLetters.has(text[i]) && text[i] !== '!'){
         setLetters.add(text[i])
      }
   }

   return (setLetters.size >= 14)
}

// console.log(isPangrama("Fabio me exige, sin tapujos, que añada cerveza al whisky"))
// console.log(isHeterograma("mango"))