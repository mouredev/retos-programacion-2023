 //Escribe un programa que reciba un texto y transforme lenguaje natural a
 //"lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 //se caracteriza por sustituir caracteres alfanuméricos.
//Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 //con el alfabeto y los números en "leet".
 //(Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 
 interface IKeys {
    [key: string]: string;
 }

 const KEYS:IKeys = {
        a: "4",
        b: "l3",
        c: "[",
        d: ")",
        e: "3",
        f: "|=",
        g: "&",
        h: "#",
        i: "1",
        j: ",_l",
        k: ">|",
        l: "1",
        m: "/\\/\\",
        n: "^/",
        o: "0",
        p: "|*",
        q: "(_,)",
        r: "l2",
        s: "5",
        t: "7",
        u: "|_|",
        v: "\/",
        w: "\/\/",
        x: "><",
        y: "`/",
        z: "2" 
}

const hackWord = (word:string):string => {
    const rgx_keys = new RegExp(/[a-z]/gi);
    return word.replace(rgx_keys, (letter:string) => KEYS[letter.toLowerCase()]);
}

console.log(hackWord('leet')); //1337