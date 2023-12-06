function getAlphabet(){
    const alphabet = {
        a: 0,á: 0,b: 0,c: 0,d: 0,e: 0,é: 0,f: 0,g: 0,h: 0,
        i: 0,í: 0,j: 0,k: 0,l: 0,m: 0,n: 0,ñ: 0,o: 0,ó: 0,
        p: 0,q: 0,r: 0,s: 0,t: 0,u: 0,ú: 0,ü: 0,v: 0,w: 0,
        x: 0,y: 0,z: 0
      };
    return  alphabet;
 }

 function getNormalizedText(text){
    let regex = new RegExp(" ", "g");
    let normalizedText = text.toLowerCase().replace(regex, "");
    return  normalizedText;
 }

function heterogram(text) {
  let isHeterogram = true;  
  let alphabetCounter = getAlphabet();  
  let normalizedText = getNormalizedText(text);

  for (let letter of normalizedText) {
    alphabetCounter[letter] = alphabetCounter[letter] + 1;

    if (alphabetCounter[letter] > 1) {
      isHeterogram = false;
      break;
    }
  }
  return isHeterogram;
}

function isogram(text) {  
  let isIsogram = false;
  let alphabetCounter = getAlphabet();  
  let normalizedText = getNormalizedText(text);

  for (let letter of normalizedText) {
    alphabetCounter[letter] = alphabetCounter[letter] + 1;

    if (alphabetCounter[letter] > 1) {
      isIsogram = true;
      break;
    }
  }

  return isIsogram;
}

function pangram(text) {  
  let isPagram = true;
  let alphabetCounter = getAlphabet();  
  let normalizedText = getNormalizedText(text);
  let alphabet = Object.keys(alphabetCounter);
    
  for (let letter of normalizedText) {    
    alphabetCounter[letter] = alphabetCounter[letter] + 1;
  }
  
  for (let letter of alphabet) {    
    if (alphabetCounter[letter] == 0) {
        isPagram = false; 
        break;
    }
  }

  return isPagram;
}

let textHeterogram = "centrifugado xyz";
let textIsogram = "acondicionar acondicionar";
let textPangram = "Benjamín pidió una bebida de kiwi y fresa. Noé, sin vergüenza, la más exquisita champaña del menú";

console.log("Is Heterogram?", heterogram(textHeterogram));
console.log("Is Isogram?",isogram(textIsogram));
console.log("Is Pangram?",pangram(textPangram));