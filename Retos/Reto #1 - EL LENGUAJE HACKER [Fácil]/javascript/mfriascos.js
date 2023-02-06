function hackerLenguage(text) {
    let leet = {
        'A':'4',
        'B':'I3',
        'C':'[',
        'D':')',
        'E':'3',
        'F':'|=',
        'G':'&',
        'H':'#',
        'I':'1',
        'J':',_|',
        'K':'>|',
        'L':'1',
        'M':'/\/|',
        'N':'^/',
        'O':'0',
        'P':'|*',
        'Q':'(_,)',
        'R':'I2',
        'S':'5',
        'T':'7',
        'U':'(_)',
        'V':'\/',
        'W':'\/\/',
        'X':'><',
        'Y':'j',
        'Z':'2'
    }

    let array = text
                    .toUpperCase()
                    .split('');

    let newArray = [];

    array.forEach(element => {
        if(element in leet){
            newArray.push(leet[element]);
        }
        else newArray.push(element);
    });

    console.log(newArray.join(''));
}

hackerLenguage('hola mundo');