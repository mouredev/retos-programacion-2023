void main() {
  var text = 'hola a todos';
  print(leet(text));
}

String leet(String text) {
  var letters = {
    'a': "4",
    "b": "I3",
    "c": "[",
    "d": ")",
    "e": "3",
    "f": "|=",
    "g": "&",
    "h": "#",
    "i": "1",
    "j": ",_|",
    "k": ">|",
    "l": "1",
    "m": "/\\/\\",
    "n": "^/",
    "o": "0",
    "p": "|*",
    "q": "(_,)",
    "r": "I2",
    "s": "5",
    "t": "7",
    "u": "(_)",
    "v": "\\/",
    "w": "\\/\\/",
    "x": "><",
    "y": "j",
    "z": "2"
  };

  var newText = "";

  for (var i = 0; i < text.length; i++) {
    if (letters.containsKey(text[i].toLowerCase())) {
      newText += letters[text[i].toLowerCase()]!;
    } else {
      newText += text[i];
    }
  }

  return newText;
}