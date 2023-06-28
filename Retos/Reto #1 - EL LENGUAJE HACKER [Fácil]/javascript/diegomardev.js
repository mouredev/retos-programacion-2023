const leet_conversion = {
"A": "4", "B": "I3", 
"C": "[", "D": ")", 
"E": "3", "F": "|=", 
"G": "6", "H": "#", 
"I": "1", "J": ",_|", 
"K": ">|", "L": "1", 
"M": "/\\/\\", "N": " ^/", 
"O": "0", "P": " |*", 
"Q": "(_,)", "R": "I2", 
"S": "5", "T": "7", 
"U": "(_)", "V": "\\/", 
"W": "\\/\\/", "X": "><", 
"Y": "j", "Z": "2",
"1": "L", "2": "R", 
"3": "E", "4": "A", 
"5": "S", "6": "b", 
"7": "T", "8": "B", 
"9": "g", "0": "o"
}
function leet_speak(text) { //HACKER SPEAK
  const text_UpperCase = text.toUpperCase()
  let conversion_text = ""
  for (let i = 0; i < text_UpperCase.length; i++) {
    if(leet_conversion[(text_UpperCase[i])]===undefined){
      conversion_text += text_UpperCase[i]
    }
    else{
      conversion_text += leet_conversion[(text_UpperCase[i])]
    }
  }
  return conversion_text
}
console.log(leet_speak("Hola mundo!!!"));