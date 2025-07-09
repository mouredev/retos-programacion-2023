function encryptCesar({ text, decifrar = false, desplazamiento = 3 }) {
  if (text.length === 0) {
    return "";
  }


  let alphabet = "abcdefghijklmnñopqrstuvwxyz";
  let cesar_code = "";
  

  for (const letter of text.toLowerCase()) {

  if (alphabet.includes(letter)) {
  
      let index = (alphabet.indexOf(letter) + (decifrar ? -desplazamiento : desplazamiento)) % alphabet.length;
      


      cesar_code += alphabet.at(index); 
    } else {
  
      cesar_code += letter;
    }
  }

  return cesar_code;
}

console.log(encryptCesar({ text: "Mi nombre es MoureDev." }));
console.log(encryptCesar({ text: "ol proeuh hv orxuhghy.", decifrar: true }));
