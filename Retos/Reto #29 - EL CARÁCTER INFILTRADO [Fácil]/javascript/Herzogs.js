const obtainInfiltrateCharacter = (cad1, cad2) => {
  let arrayCharacters = [];
  if(cad1.length !== cad2.length){
    throw new Error("Cadenas Desiguales");
  }
  cad1.split('').forEach((el,ix) =>{
    if(el != cad2[ix]){
      arrayCharacters.push(cad2[ix]);
    }
  })

  return arrayCharacters;
};

console.log(obtainInfiltrateCharacter("Me llamo mouredev",
                                      "Me llemo mouredov"));

console.log(obtainInfiltrateCharacter("Me llamo.Brais Moure",
                                      "Me llamo brais moure"));

console.log(obtainInfiltrateCharacter("Me llamoBrais Moure",
                                      "Me llamo brais moure"));

console.log(obtainInfiltrateCharacter("Me llamo Brais Moure",
                                      "Me llamo Brais Moure"));
