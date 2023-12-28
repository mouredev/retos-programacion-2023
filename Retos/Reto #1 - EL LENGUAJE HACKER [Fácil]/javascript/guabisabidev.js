const diccionario = new Map();
diccionario.set('a','4');
diccionario.set('b','I3');
diccionario.set('c','[');
diccionario.set('d',')');
diccionario.set('e','3');
diccionario.set('f','|=');
diccionario.set('g','&');
diccionario.set('h','#');
diccionario.set('i','1');
diccionario.set('j',',_|');
diccionario.set('k','>|');
diccionario.set('l','1');
diccionario.set('m','/\\/\\');
diccionario.set('n','^/');
diccionario.set('o','0');
diccionario.set('p','|*');
diccionario.set('q','(_,)');
diccionario.set('r','I2');
diccionario.set('s','5');
diccionario.set('t','7');
diccionario.set('u','(_)');
diccionario.set('v','\/');
diccionario.set('w','\\/\\/');
diccionario.set('x','><');
diccionario.set('y','j');
diccionario.set('z','2');
diccionario.set(' ',' ');
diccionario.set('1', 'L');
diccionario.set('2', 'R');
diccionario.set('3', 'E');
diccionario.set('4', 'A');
diccionario.set('5', 'S');
diccionario.set('6', 'b');
diccionario.set('7', 'T');
diccionario.set('8', 'B');
diccionario.set('9', 'g');
diccionario.set('0', 'o');

function traductor(frase) {
    console.log("La frase original es: "+frase);
    let nuevaFrase ="";
    frase = frase.toLowerCase();
    for (let i=0; i<frase.length; i++) {
        nuevaFrase+=(diccionario.get(frase[i]));
    }
    console.log("La frase traducida es: "+nuevaFrase);
}

traductor("hola");
traductor("hola caracola");
traductor("FELIZ 2023");
traductor("1234");
