function hacker_language(text) {

    //Convertimos el texto a minúsculas y creamos una variable vacia
    let textLowerCase = text.toLowerCase();
    let leet = '';

    //Recorremos el texto y según el caracter lo traducimos a "lenguaj hacker"
    for (let i = 0; i <= textLowerCase.length; i++) {
        switch (textLowerCase[i]) {
            case 'a':
                leet += '4';
                break;
            case 'b':
                leet += 'I3';
                break;
            case 'c':
                leet += '[';
                break;
            case 'd':
                leet += ')';
                break;
            case 'e':
                leet += '3';
                break;
            case 'f':
                leet += '|=';
                break;
            case 'g':
                leet += '&';
                break;
            case 'h':
                leet += '#';
                break;
            case 'i':
                leet += '1';
                break;
            case 'j':
                leet += ',_|';
                break;
            case 'k':
                leet += '>|';
                break;
            case 'l':
                leet += '|_';
                break;
            case 'm':
                leet += '\/\\/\\';
                break;
            case 'n':
                leet += '^/';
                break;
            case 'o':
                leet += '0';
                break;
            case 'p':
                leet += '|*';
                break;
            case 'q':
                leet += '(_,)';
                break;
            case 'r':
                leet += 'I2';
                break;
            case 's':
                leet += '5';
                break;
            case 't':
                leet += '+';
                break;
            case 'u':
                leet += '(_)';
                break;
            case 'v':
                leet += '\\\/';
                break;
            case 'w':
                leet += '\\\/\\\/';
                break;
            case 'x':
                leet += '><';
                break;
            case 'y':
                leet += 'j';
                break;
            case 'z':
                leet += '2';
                break;
            case '1':
                leet += 'L';
                break;
            case '2':
                leet += 'R';
                break;
            case '3':
                leet += 'E';
                break;
            case '4':
                leet += 'A';
                break;
            case '5':
                leet += 'S';
                break;
            case '6':
                leet += 'b';
                break;
            case '7':
                leet += 'T';
                break;
            case '8':
                leet += 'B';
                break;
            case '9':
                leet += 'g';
                break;
            case '0':
                leet += 'o';
                break;
        }
    }

    //Devolvemos el texto traducido
    return leet;
}

hacker_language('abcdefghikjlmnopqrstuvwxyz1234567890');
hacker_language('Hello World');