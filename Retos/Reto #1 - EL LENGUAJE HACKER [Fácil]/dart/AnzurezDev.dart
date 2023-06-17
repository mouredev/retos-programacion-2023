const Map<String, String> alphabet = {
    "A": "4",
    "B": "I3",
    "C": "[",
    "D": ")",
    "E": "3",
    "F": "|=",
    "G": "&",
    "H": "#",
    "I": "1",
    "J": ",_|",
    "K": ">|",
    "L": "1",
    "M": "/\\/\\",
    "N": "^/",
    "O": "0",
    "P": "|*",
    "Q": "(_,)",
    "R": "I2",
    "S": "5",
    "T": "7",
    "U": "(_)",
    "V": "\\/",
    "W": "\\/\\/",
    "X": "><",
    "Y": "j",
    "Z": "2",
    "1": "L",
    "2": "R",
    "3": "E",
    "4": "A",
    "5": "S",
    "6": "b",
    "7": "T",
    "8": "B",
    "9": "g",
    "0": "o"
};



void leetLang( dynamic objText ) {
  String text   = objText.toString().toUpperCase();
  String output = "";

  for ( int index=0; index<text.length; index++ )
    output += alphabet.containsKey( text[index] ) ? alphabet[ text[index] ].toString() : text[ index ];

  print( output );
}

void main() {
  leetLang( "This is the hacker language" );
}