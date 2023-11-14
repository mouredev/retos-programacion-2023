/*
 Crea una función que sea capaz de transformar Español al lenguaje básico del universo
 Star Wars: el "Aurebesh".
 - Puedes dejar sin transformar los caracteres que no existan en "Aurebesh".
 - También tiene que ser capaz de traducir en sentido contrario.
   
 ¿Lo has conseguido? Nómbrame en twitter.com/mouredev y escríbeme algo en Aurebesh.
 
 ¡Que la fuerza os acompañe!
*/

function starWars(frase, traduccion) {
  const español_a_aurebesh = {
    a: "q",
    b: "b",
    c: "c",
    d: "d",
    e: "e",
    f: "f",
    g: "g",
    h: "h",
    i: "i",
    j: "j",
    k: "k",
    l: "l",
    m: "m",
    n: "n",
    ñ: "ñ",
    o: "o",
    p: "p",
    q: "r",
    r: "s",
    s: "t",
    t: "u",
    u: "v",
    v: "w",
    w: "x",
    x: "y",
    y: "z",
    z: "a",
  };

  const aurebesh_a_español = {
    q: "a",
    b: "b",
    c: "c",
    d: "d",
    e: "e",
    f: "f",
    g: "g",
    h: "h",
    i: "i",
    j: "j",
    k: "k",
    l: "l",
    m: "m",
    n: "n",
    ñ: "ñ",
    o: "o",
    p: "p",
    r: "q",
    s: "r",
    t: "s",
    u: "t",
    v: "u",
    w: "v",
    x: "w",
    y: "x",
    z: "y",
    a: "z",
  };

  let texto_traducido = "";
  const texto = frase.toLowerCase();

  if (traduccion === "aurebesh") {
    for (let i = 0; i < texto.length; i++) {
      const letra = texto[i];
      if (español_a_aurebesh[letra]) { 
        texto_traducido = texto_traducido + español_a_aurebesh[letra];
      } else {
        texto_traducido = texto_traducido + letra;
      }
    }
  } else if(traduccion === "español") {
    for (let i = 0; i < texto.length; i++) {
      const letra = texto[i];
      if (aurebesh_a_español[letra]) {
        texto_traducido = texto_traducido + aurebesh_a_español[letra];
      } else {
        texto_traducido = texto_traducido + letra;
      }
    }
  }else{
    texto_traducido = "traduccion no valida";
  }

  return texto_traducido;
}

console.log(starWars("¡Que la fuerza os acompañe!","aurebesh")); // ¡rve lq fvesaq ot qcompqñe!
console.log(starWars("¡rve lq fvesaq ot qcompqñe!","español")); // ¡Que la fuerza os acompañe!
