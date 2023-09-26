let may=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
let min=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
let num=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
let esp=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "-", "=", ",", ".", "<", ">", "?", "/", ";", ":", "\'", "\"", "|", "\\", "{", "}", "[", "]", "`", "~"]


function passwordGenerator(mayuscula, numero, especial, n){
  let pwdString=""
  let char=""
  if((n!==undefined||n!==null)&&n<8||n>16){
    return 'Se requiere un minimo de 8 caracteres y maximo de 16'
  }
  if(n===undefined||n===null){
    n=Math.floor(Math.random() * (16 - 8) + 8)
  }
  let arr=[...min]
  mayuscula==1?arr.push(...may):arr
  numero==1?arr.push(...num):arr
  especial==1?arr.push(...esp):arr
  for(let i=0;i<n;i++){
    char=arr[Math.floor(Math.random()*arr.length)]
    pwdString+=char;
  }
  arr=[]
    return pwdString
}

//EL NUMERO DE CARACTERES ES OPCIONAL, CUANDO NO SE PONE, REGRESA UN STRING DE ENTRE 8 Y 16 CARACTERES
passwordGenerator(0,0,0);
passwordGenerator(1,0,0);
passwordGenerator(0,1,0);
passwordGenerator(0,0,1);

passwordGenerator(1,1,1);
passwordGenerator(0,1,1);
passwordGenerator(1,0,1);
passwordGenerator(1,1,0);

let numeroCaracteres=9
passwordGenerator(0,0,0,numeroCaracteres);
passwordGenerator(1,0,0,numeroCaracteres);
passwordGenerator(0,1,0,numeroCaracteres);
passwordGenerator(0,0,1,numeroCaracteres);

passwordGenerator(1,1,1,numeroCaracteres);
passwordGenerator(0,1,1,numeroCaracteres);
passwordGenerator(1,0,1,numeroCaracteres);
passwordGenerator(1,1,0,numeroCaracteres);

