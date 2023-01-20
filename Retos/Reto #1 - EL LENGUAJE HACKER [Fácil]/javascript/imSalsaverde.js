/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337").
 */

const diccionario = {
    a: "4",
    b: "I3",
    c: "[",
    d: ")",
    e: "3",
    f: "|=",
    g: "&",
    h: "#",
    i: "1",
    j: ",_|",
    k: ">|",
    l: "1",
    m: "/\\/\\",
    n: "^/",
    o: "0",
    p: "|*",
    q: "(_,)",
    r: "12",
    s: "5",
    t: "7",
    u: "(_)",
    v: "\\/",
    w: "\\/\\/",
    x: "><",
    y: "j",
    z: "2",

    1: "L",
    2: "R",
    3: "E",
    4: "A",
    5: "S",
    6: "b",
    7: "T",
    8: "B",
    9: "g",
    0: "o",
};

function leet(texto){
  let t=texto.toLowerCase()
    let resultado='';
    for(i=0;i<t.length;i++){
        if(diccionario[t[i]]){
            resultado+=diccionario[t[i]];
        }
      else{
        resultado+=t[i]
      }
    }
        
    return resultado;
};

/*
La parte de los test la vi en la solucion de test0n3 y la "tomé prestada" porque me gustó
y no se me habia ocurrido hacer así los test jaja
 */

const tests = {
    input: [
      "soy el diluvio",
      "TE LLORE UN RIO",
      "LiTtL3 pIeCe 0f He4vEn",
      "#L1Fe_W@5tEr.",
    ],
    output: [
      "50j 31 )11(_)\\/10",
      "73 110123 (_)^/ 1210",
      "11771E |*13[3 o|= #3A\\/3^/",
      "#1L|=3_\\/\\/@S7312.!!", //Este falla a proposito
    ],
  };
  
  let errors = 0;
  tests.input.forEach((test, index) => {
    let resp = leet(test);
    let expected = tests.output[index];
    if (resp != expected) {
      errors += 1;
      console.log(`Test ${index}: Not Hot Dog`)
      console.log("\noriginal: ", test);
      console.log("Resultado:\n",resp);
      console.log("Respuesta:\n", expected);
      
    }else{
      //console.log("Resultado:", resp);
      //console.log("Respuesta:", expected);
      console.log(`Test ${index}: Hot Dog`)
    }
  });
  
  console.log(`${errors != 0 ? " Test incompletos " : "Test completos"}, ${errors} errores`);