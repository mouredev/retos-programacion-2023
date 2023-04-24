const leet_dict = {
    'a': '4',
    'b': 'I3',
    'c': '[',
    'd': ')',
    'e': '3',
    'f': '|=',
    'g': '&',
    'h': '#',
    'i': '1',
    'j': ',_|',
    'k': '>|',
    'l': '|',
    'm': '/\/\\',
    'n': '^/',
    'o': '0',
    'p': '|*',
    'q': '(_,)',
    'r': 'I2',
    's': '5',
    't': '7',
    'u': '(_)',
    'v': '\/',
    'w': '\/\/',
    'x': '><',
    'y': 'j',
    'z': '2'
  };
  
  while (true) {
    const text = prompt("Ingresa el texto a convertir a leet: ");
    const leet_text = text.toLowerCase().split('').map(char => leet_dict[char] || char).join('');
    console.log(`Texto en leet: ${leet_text}`);
  }
  