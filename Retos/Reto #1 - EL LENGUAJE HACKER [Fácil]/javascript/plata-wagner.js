function leetHack(message){
    let msg="";
    for (var i = 0; i < message.length; i++) {
        switch (message[i]) {
            case 'a':
            msg += '4';
            break;
            case 'b':
            msg += 'I3';
            break;
            case 'c':
            msg += '[';
            break;
            case 'd':
            msg += ')';
            break;
            case 'e':
            msg += '3';
            break;
            case 'f':
            msg += '|=';
            break;
            case 'g':
            msg += '&';
            break;
            case 'h':
            msg += '#';
            break;
            case 'i':
            msg += '1';
            break;
            case 'j':
            msg += ',_|';
            break;
            case 'k':
            msg += '>|';
            break;
            case 'l':
            msg += '1';
            break;
            case 'm':
            msg += '/\\/\\';
            break;
            case 'n':
            msg += '^/';
            break;
            case 'ñ':
            msg += '¬^/';
            break;
            case 'o':
            msg += '0';
            break;
            case 'p':
            msg += '|*';
            break;
            case 'q':
            msg += '(,_)';
            break;
            case 'r':
            msg += '12';
            break;
            case 's':
            msg += '5';
            break;
            case 't':
            msg += '7';
            break;
            case 'u':
            msg += '(_)';
            break;
            case 'v':
            msg += '\\/';
            break;
            case 'w':
            msg += '\\/\\/';
            break;
            case 'x':
            msg += '><';
            break;
            case 'y':
            msg += 'j';
            break;
            case 'z':
            msg += '2';
            break;
            default:
            msg += message[i];
        }
    }
    return msg;
}
console.log(leetHack("abcdefghijklmnñopqrstuvwxyz"));