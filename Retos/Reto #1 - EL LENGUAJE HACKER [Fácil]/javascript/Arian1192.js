"use strict";
const mapper = {
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
    v: "\\/",
    w: "\\/\\/",
    x: "><",
    y: "`/",
    z: "2"
};
// crear una funcion que tranforme una palabra en un array de valores
const frase = 'mouredew';
const transformString = (frase) => {
    // paso la frase a minusculas
    frase = frase.toLowerCase();
    // la convierto en un array de caracteres separado por comas
    const arr = frase.split('');
    // creo un array donde voy a pushear el resultado
    let newArr = [];
    // recorro el array
    arr.map((letra) => {
        if (letra in mapper) {
            newArr.push(mapper[letra]);
        }
        else if (letra === ' ') {
            newArr.push(letra);
        }
        else {
            newArr.push(letra);
        }
    });
    console.log(newArr.join(''));
};
transformString(frase);