// 64$!( 1&&-|- :

function leet(array) { 

    const result = array.map(element => {

        if (element != '') {

            switch(element) {

                case 'a':
                    return '4';
                
                case 'b':
                    return '6';
                
                case 'c':
                    return '(';
                
                case 'd':
                    return '[)';
                
                case 'e':
                    return '&';
                
                case 'f':
                    return ']]=';

                case 'g':
                    return '(_+';
                
                case 'h':
                    return '#';
                
                case 'i':
                    return '!';
                
                case 'j':
                    return ',|';

                case 'k':
                    return ']{';
                
                case 'l':
                    return '1';
                
                case 'm':
                    return '(v)';
                
                case 'n':
                    return '//';

                case 'o':
                    return '()';
                
                case 'p':
                    return '[]|)';
                
                case 'q':
                    return '(,)';

                case 'r':
                    return '1²';

                case 's':
                    return '$';

                case 't':
                    return '-|-';
                
                case 'u':
                    return '(_)';

                case 'v':
                    return 'v';
                    
                case 'w':
                    return 'vv';
                
                case 'x':
                    return '%';

                case 'y':
                    return '°/';

                case 'z':
                    return '“/_';
            }
        }
    });

    return result.join('');
}

// test case:

let words = 'hola como estas';
words = words.split('');

console.log(leet(words));