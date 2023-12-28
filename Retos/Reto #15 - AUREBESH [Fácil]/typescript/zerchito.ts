/*
 * Crea una función que sea capaz de transformar Español al lenguaje básico del universo
 * Star Wars: el "Aurebesh".
 * - Puedes dejar sin transformar los caracteres que no existan en "Aurebesh".
 * - También tiene que ser capaz de traducir en sentido contrario.
 *  
 * ¿Lo has conseguido? Nómbrame en twitter.com/mouredev y escríbeme algo en Aurebesh.
 *
 * ¡Que la fuerza os acompañe!
 */
{
  const spanishToAurebesh = {
    a: "aurek",
    b: "besh",
    c: "cresh",
    d: "dorn",
    e: "esseles",
    f: "forn",
    g: "grek",
    h: "herf",
    i: "isk",
    j: "jenth",
    k: "krill",
    l: "leth",
    m: "mern",
    n: "nern",
    ñ: "nerf",
    o: "osk",
    p: "pei",
    q: "qek",
    r: "resh",
    s: "senth",
    t: "trill",
    u: "ujeb",
    v: "vev",
    w: "wirch",
    x: "xesh",
    y: "yirt",
    z: "zerek",
    ch: "cherek",
    ae: "enth",
    eo: "onith",
    kh: "krenth",
    ng: "nen",
    oo: "orenth",
    sh: "shen",
    th: "thesh",
  };


  function translateToAurebesh(spanishStr: string) {
    // Initialize an empty output string
    let aurebeshStr = '';
    let index = 0;
    while(index < spanishStr.length) {
      let key = spanishStr.slice(index, index + 2);
      let step = 2;
      if (!spanishToAurebesh[key]) {
        step = 1;
        key = key.charAt(0)
      }
      const aurebeshC = spanishToAurebesh[key] || key;
      aurebeshStr += aurebeshC;
      index += step;
    }
    return aurebeshStr;
  }

  console.log(translateToAurebesh('Hummm I am the passeger and I ride and I ride'));
}