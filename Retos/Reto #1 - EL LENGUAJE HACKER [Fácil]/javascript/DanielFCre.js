const text = "Daniel Fernandez";
const hackerText = transform(text);
console.log(hackerText); 

function transform(text) {

    const leetDictionary = {
      'a': '4',
      'b': '8',
      'c': '(',
      'd': '|)',
      'e': '3',
      'f': '|=',
      'g': '9',
      'h': '|-|',
      'i': '1',
      'j': '_|',
      'k': '|<',
      'l': '|_',
      'm': '|\/|',
      'n': '|\|',
      'o': '0',
      'p': '|>',
      'q': '0,',
      'r': '|2',
      's': '5',
      't': '7',
      'u': '|_|',
      'v': '\/',
      'w': '\/\/',
      'x': '}{',
      'y': '`/',
      'z': '2',
      '0': '0o',
      '1': '|',
      '2': '5',
      '3': '3',
      '4': '|_|',
      '5': '5',
      '6': '9',
      '7': '7',
      '8': '8',
      '9': '9'
    };
  
    let result = "";
  
    for (let letter of text) {

      if (letter.toLowerCase() in leetDictionary) {
        result += leetDictionary[letter.toLowerCase()];
      }
      else {
        result += letter;
      }
    }

    return result;
  }
  