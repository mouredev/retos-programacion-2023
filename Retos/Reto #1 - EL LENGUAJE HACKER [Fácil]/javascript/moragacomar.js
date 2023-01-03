/* # Reto #1: EL "LENGUAJE HACKER"
 * #### Dificultad: Fácil | Publicación: 02/01/23 | Corrección: 09/01/23
 *
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */


const lang = { "a": "4", "b": "I3", "c": "[", "d": ")", "e": "3", "f": "|=", "g": "&", "h": "#", "i": "1", "j": ",_|", "k": ">|", "l": "1", "m": "/\\/\\", "n": "^/", "o": "0", "p": "|*", "q": "(_,)", "r": "I2", "s": "5", "t": "7", "u": "(_)", "v": "\\/", "w": "\\/\\/", "x": "><", "y": "j", "z": "2", "1": "L", "2": "R", "3": "E", "4": "A", "5": "S", "6": "b", "7": "T", "8": "B", "9": "g", "0": "o" }

const sustituir = (text) => text.toLowerCase().split("").map(el => lang[el]).join("");

const mensajeHacker = sustituir("abcdefghijklmnopqrstuvwxyz");

console.log(mensajeHacker);




// METODO ORIGINAL USADO EN LA WEB: https://www.gamehouse.com/blog/leet-speak-cheat-sheet/

function randomize(arr) {
    var random = 0;
    var length = arr.length;
    random = Math.floor((Math.random() * length) + 1);
    return random;
}

function leetIt(text, level) {
    // Basic
    if (level == 'option1') {
        text = text.replace(/a/gi, "4");
        text = text.replace(/e/gi, "3");
        text = text.replace(/i/gi, "1");
        text = text.replace(/o/gi, "0");
        text = text.replace(/u/gi, "(_)");
    }

    // Intermediate
    if (level == 'option2') {
        text = text.replace(/a/gi, "4");

        text = text.replace(/c/gi, "[");
        text = text.replace(/d/gi, "|)");
        text = text.replace(/e/gi, "3");

        text = text.replace(/g/gi, "6");
        text = text.replace(/h/gi, "#");
        text = text.replace(/i/gi, "1");
        text = text.replace(/j/gi, "]");
        text = text.replace(/k/gi, "|<");
        text = text.replace(/l/gi, "1");
        text = text.replace(/m/gi, "/V\\");
        text = text.replace(/n/gi, "|\\|");
        text = text.replace(/o/gi, "0");
        text = text.replace(/p/gi, "|>");
        text = text.replace(/q/gi, "0_");

        text = text.replace(/s/gi, "5");
        text = text.replace(/t/gi, "7");
        text = text.replace(/u/gi, "(_)");
        text = text.replace(/v/gi, "\\/");
        text = text.replace(/w/gi, "\\/\\/");
        text = text.replace(/x/gi, "><");

        text = text.replace(/z/gi, "2");

        text = text.replace(/f/gi, "ph");
        text = text.replace(/b/gi, "I3");
        text = text.replace(/r/gi, "I2");
        text = text.replace(/y/gi, "j");
    }

    // Option 3
    if (level == 'option3') {
        var rand = 0;

        var a = ["4", "@", "/\\"];
        rand = randomize(a) - 1;
        text = text.replace(/a/gi, a[rand]);

        var a = ["[", "{", "<"];
        rand = randomize(a) - 1;
        text = text.replace(/c/gi, a[rand]);

        var a = [")", "|)", "(|", "[)", "|>"];
        rand = randomize(a) - 1;
        text = text.replace(/d/gi, a[rand]);

        var a = ["3", "&", "ë"];
        rand = randomize(a) - 1;
        text = text.replace(/e/gi, a[rand]);

        var a = ["&", "6", "9", "(_+", "(?,", "[,", "{,"];
        rand = randomize(a) - 1;
        text = text.replace(/g/gi, a[rand]);

        var a = ["#", "/-/", "[-]", "]-[", ")-(,", "(-)", ":-:"];
        rand = randomize(a) - 1;
        text = text.replace(/h/gi, a[rand]);

        var a = ["1", "[]", "|", "!", "]["];
        rand = randomize(a) - 1;
        text = text.replace(/i/gi, a[rand]);

        var a = [",_|", "_|", "._|", "._]", "_]"];
        rand = randomize(a) - 1;
        text = text.replace(/j/gi, a[rand]);

        var a = [">|", "|<", "/<", "1<", "|(", "|{"];
        rand = randomize(a) - 1;
        text = text.replace(/k/gi, a[rand]);

        var a = ["1", "7", "|_", "|"];
        rand = randomize(a) - 1;
        text = text.replace(/l/gi, a[rand]);

        var a = ["^/", "|\\|", "/\\/", "[\\]", "<\\>", "{\\}"];
        rand = randomize(a) - 1;
        text = text.replace(/n/gi, a[rand]);

        var a = ["(0)", "()", "[]", "<>"];
        rand = randomize(a) - 1;
        text = text.replace(/o/gi, a[rand]);

        var a = ["|*", "|º", "|^", "|>", "|7"];
        rand = randomize(a) - 1;
        text = text.replace(/p/gi, a[rand]);

        var a = ["(_,)", "9", "()_", "2", "0_", "<|", "&"];
        rand = randomize(a) - 1;
        text = text.replace(/q/gi, a[rand]);

        var a = ["5", "$", "2"];
        rand = randomize(a) - 1;
        text = text.replace(/s/gi, a[rand]);

        var a = ["7", "+", "-|-", "']['", "~|~"];
        rand = randomize(a) - 1;
        text = text.replace(/t/gi, a[rand]);


        var a = ["\\/", "|/", "\\|"];
        rand = randomize(a) - 1;
        text = text.replace(/v/gi, a[rand]);

        var a = ["\\/\\/", "VV", "\\N", "'//", "\\\\'", "\\^/", "\\|/", "\\_|_/", "\\_:_/"];
        rand = randomize(a) - 1;
        text = text.replace(/w/gi, a[rand]);

        var a = ["><", "}{", ")(", "]["];
        rand = randomize(a) - 1;
        text = text.replace(/x/gi, a[rand]);

        var a = ["2", "7_", "-/_", "%"];
        rand = randomize(a) - 1;
        text = text.replace(/z/gi, a[rand]);

        var a = ["/\\/\\", "/V\\", "[V]", "[]V[]", "|\\/|", "^^", "<\\/>", "]\\/["];
        rand = randomize(a) - 1;
        text = text.replace(/m/gi, a[rand]);

        var a = ["ph", "|=_", "|#", "/="];
        rand = randomize(a) - 1;
        text = text.replace(/f/gi, a[rand]);

        var a = ["I3", "8", "13", "|3", "!3", "(3"];
        rand = randomize(a) - 1;
        text = text.replace(/b/gi, a[rand]);

        var a = ["I2", "2", "12", "|9", "|`", "/2"];
        rand = randomize(a) - 1;
        text = text.replace(/r/gi, a[rand]);

        var a = ["j", "'/'", "7", "\\|/", "\\//"];
        rand = randomize(a) - 1;
        text = text.replace(/y/gi, a[rand]);

        var a = ["(_)", "|_|", "V", "L|"];
        rand = randomize(a) - 1;
        text = text.replace(/u/gi, a[rand]);
    }

    // Option 4
    if (level == 'option4') {
        var rand = 0;

        var a = ["4", "@", "/\\", "Д"];
        rand = randomize(a) - 1;
        text = text.replace(/a/gi, a[rand]);

        var a = ["[", "{", "<", "©"];
        rand = randomize(a) - 1;
        text = text.replace(/c/gi, a[rand]);

        var a = [")", "|)", "(|", "[)", "|>", ">", "|]", "|}"];
        rand = randomize(a) - 1;
        text = text.replace(/d/gi, a[rand]);

        var a = ["3", "&", "ë", "£", "€", "[-", "|=-"];
        rand = randomize(a) - 1;
        text = text.replace(/e/gi, a[rand]);

        var a = ["&", "6", "9", "(_+", "(?,", "[,", "{,", "gee"];
        rand = randomize(a) - 1;
        text = text.replace(/g/gi, a[rand]);

        var a = ["#", "/-/", "[-]", "]-[", ")-(,", "(-)", ":-:", "1-1", "|+|"];
        rand = randomize(a) - 1;
        text = text.replace(/h/gi, a[rand]);

        var a = ["1", "[]", "|", "!", "][", "!"];
        rand = randomize(a) - 1;
        text = text.replace(/i/gi, a[rand]);

        var a = [",_|", "_|", "._|", "._]", "_]"];
        rand = randomize(a) - 1;
        text = text.replace(/j/gi, a[rand]);

        var a = [">|", "|<", "/<", "1<", "|(", "|{"];
        rand = randomize(a) - 1;
        text = text.replace(/k/gi, a[rand]);

        var a = ["1", "7", "|_", "|", "£"];
        rand = randomize(a) - 1;
        text = text.replace(/l/gi, a[rand]);

        var a = ["^/", "|\\|", "/\\/", "[\\]", "<\\>", "{\\}", "И", "ท"];
        rand = randomize(a) - 1;
        text = text.replace(/n/gi, a[rand]);

        var a = ["(0)", "()", "[]", "<>", "oh", "Ø"];
        rand = randomize(a) - 1;
        text = text.replace(/o/gi, a[rand]);

        var a = ["|*", "|º", "|^", "|>", "|7", "[]D"];
        rand = randomize(a) - 1;
        text = text.replace(/p/gi, a[rand]);

        var a = ["(_,)", "9", "()_", "2", "0_", "<|", "&"];
        rand = randomize(a) - 1;
        text = text.replace(/q/gi, a[rand]);

        var a = ["5", "$", "2", "§", "ehs", "es"];
        rand = randomize(a) - 1;
        text = text.replace(/s/gi, a[rand]);

        var a = ["7", "+", "-|-", "']['", "~|~", "†"];
        rand = randomize(a) - 1;
        text = text.replace(/t/gi, a[rand]);

        var a = ["\\/", "|/", "\\|"];
        rand = randomize(a) - 1;
        text = text.replace(/v/gi, a[rand]);

        var a = ["\\/\\/", "VV", "\\N", "'//", "\\\\'", "\\^/", "\\|/", "\\_|_/", "\\_:_/", "Ш", "Щ", "พ", "v²"];
        rand = randomize(a) - 1;
        text = text.replace(/w/gi, a[rand]);

        var a = ["><", "}{", ")(", "][", "×", "ecks"];
        rand = randomize(a) - 1;
        text = text.replace(/x/gi, a[rand]);

        var a = ["2", "7_", "-/_", "%"];
        rand = randomize(a) - 1;
        text = text.replace(/z/gi, a[rand]);

        var a = ["/\\/\\", "/V\\", "[V]", "[]V[]", "|\\/|", "^^", "<\\/>", "]\\/[", "nn", "|T|", "JTI"];
        rand = randomize(a) - 1;
        text = text.replace(/m/gi, a[rand]);

        var a = ["ph", "|=_", "|#", "/=", "v", "ƒ"];
        rand = randomize(a) - 1;
        text = text.replace(/f/gi, a[rand]);

        var a = ["I3", "8", "13", "|3", "!3", "(3", "j3"];
        rand = randomize(a) - 1;
        text = text.replace(/b/gi, a[rand]);

        var a = ["I2", "2", "12", "|9", "|`", "/2", "®", "[z", "Я"];
        rand = randomize(a) - 1;
        text = text.replace(/r/gi, a[rand]);

        var a = ["j", "'/'", "7", "\\|/", "\\//", "¥", "Ч"];
        rand = randomize(a) - 1;
        text = text.replace(/y/gi, a[rand]);

        var a = ["(_)", "|_|", "V", "L|", "µ", "บ"];
        rand = randomize(a) - 1;
        text = text.replace(/u/gi, a[rand]);
    }
    return text
}

console.log(leetIt("JUAN", "option1"))
