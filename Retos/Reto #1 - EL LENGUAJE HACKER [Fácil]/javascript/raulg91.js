const sustitution = {

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
    'l': '1',
    'm':'\/\\\/\\',
    'n':'^/',
    'o':'0',
    'p':'|*',   
    'q': '(_,)',
    'r': 'I2',
    's': '5',
    't': '7',
    'u': '(_)',
    'v': '\\\/',
    'w': '\\\/\\\/',
    'x': '><',
    'y': 'j',
    'z': '2'

};
const prompt = require('prompt-sync')();
//
// get input from the user.
//
let cadena = prompt('Enter string to transform ');

 cadena = cadena.toLowerCase();

 for(let i of cadena){

    cadena=cadena.replace(i,sustitution[i]);
 }

 console.log(cadena);