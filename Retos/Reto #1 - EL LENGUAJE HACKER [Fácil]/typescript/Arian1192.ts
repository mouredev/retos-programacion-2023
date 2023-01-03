const mapper: object = {
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


const transformString = (frase: string):void => {
    frase = frase.toLowerCase()
    const arr = frase.split('')
    let newArr: string[] = []
    arr.map((letra: string) => {
        if (letra in mapper) {
            newArr.push(mapper[letra as keyof typeof mapper])
        } else if (letra === ' ') {
            newArr.push(letra)
        } else {
            newArr.push(letra)
        }
    })
    console.log(newArr.join(''))
}

transformString('Arian1192')