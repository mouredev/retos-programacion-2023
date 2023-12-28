function decodeAbacusNumber(arrayAbacusNumber) {
  
  let genericMessage = "the abacus number does not meet the structure conditions";

  if (arrayAbacusNumber.length < 7 || arrayAbacusNumber.length > 7) return genericMessage;

  const abacus = {
    "": 0,    O: 1,    OO: 2,
    OOO: 3,    OOOO: 4,    OOOOO: 5,
    OOOOOO: 6,    OOOOOOO: 7,    OOOOOOOO: 8,
    OOOOOOOOO: 9,
  };

  let messageNumber = "";
  let isTheStructureCorrect = true;

  for (let abacusNumber of arrayAbacusNumber) {
    
    if (abacusNumber.length > 12 || abacusNumber.length < 12){
      isTheStructureCorrect = false;
      break;
    }

    let newArray = abacusNumber.split("---");
    
    if (newArray.length < 2 || newArray.length > 2) {
      isTheStructureCorrect = false;
      break;
    }

    if ((typeof abacus[newArray[0]] === "undefined") || (typeof abacus[newArray[1]]=== "undefined")){
      isTheStructureCorrect = false;
      break;
    }
    
    messageNumber += abacus[newArray[0]];
  }

  if(!isTheStructureCorrect) return genericMessage;

  let number = parseInt(messageNumber);
  let formattedNumber = new Intl.NumberFormat("es-ES", {
    minimumFractionDigits: 0,
  }).format(number);

  return formattedNumber;
}

console.log(decodeAbacusNumber([
  "O---OOOOOOOO",
  "OOO---OOOOOO",
  "---OOOOOOOOO",
  "OO---OOOOOOO",
  "OOOOOOO---OO",
  "OOOOOOOOO---",
  "---OOOOOOOOO",
]));
