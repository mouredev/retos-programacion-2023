const alphabet = [
  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
  'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
];

const leet = [
  '4', 'I3', '[', ')', '3', '|=', '&', '#', '1', ',_|', '>|', '1', '/\\/\\',
  '^/', '0', '|*', '(_,)', 'I2', '5', '7', '(_)', '\/', '\/\/', '><', 'j', '2'
];

function characterConverter(character) {
const index = alphabet.indexOf(character.toUpperCase());
if (index !== -1) {
  return leet[index];
} else {
  return character;
}
}

function textConverter(text) {
let convertedText = "";
for (let i = 0; i < text.length; i++) {
  convertedText += characterConverter(text[i]);
}
return convertedText;
}

console.log(textConverter("Estoy cansado jefe"));
