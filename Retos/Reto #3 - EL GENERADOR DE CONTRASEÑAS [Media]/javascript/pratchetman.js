<!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <title>Reto 3 - Mouredev</title>
    <script>
    
      let generarPass = (length, ifMinMay, ifNum, ifSymbol) => {
        let pass= "";

        let text0 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"];

        let text1 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"];

        let text2 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "!", '"', "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "\\", "]", "^", "_", "`", "{", "|", "}"];

        let text3 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "!", '"', "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "\\", "]", "^", "_", "`", "{", "|", "}"];

        if (length <= 16 && length >= 8){
          for (let i = 0; i < length; i++){
          
          if (ifNum == false && ifSymbol == false){
            pass += text0[Math.floor(Math.random() * ((text0.length - 1) - 0 + 1) + 0)]
            
            
          }
          else if (ifNum == true && ifSymbol == false){
            pass += text1[Math.floor(Math.random() * ((text1.length - 1) - 0 + 1) + 0)]
            

          }
          else if (ifNum == true && ifSymbol == true){
            pass += text2[Math.floor(Math.random() * ((text2.length - 1) - 0 + 1) + 0)]
            
          }
          else if (ifNum == false && ifSymbol == true){
            pass += text3[Math.floor(Math.random() * ((text3.length - 1) - 0 + 1) + 0)]
           
          }
         
    }
        }
        else{
          pass = "La longitud del password es incorrecta";
        }
       
    return ifMinMay ? pass : pass.toLowerCase();
  }

let longitud = 13;
let mayus = false;
let numbers = true;
let symbols = false;
console.log(generarPass(longitud, mayus, numbers, symbols));

    </script>
  </head>
  <body>
    
  </body>
</html>
