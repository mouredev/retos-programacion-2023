function leet(text) {
    
    const leetDictionary = { 
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
    l: "£",
    m: "/\\/\\",
    n: "^/",
    o: "0",
    p: "|*",
    q: "(_,)",
    r: "I2",
    s: "5",
    t: "7",
    u: "(_)",
    v: "\\/",
    w: "\\/\\/",
    x: "><",
    y: "j",
    z: "2",
    " ": " ",
    };

    let translate = ""; 

    for (let letter of text.toLowerCase()) {
        translate += letter in leetDictionary ? leetDictionary[letter] : letter; 
}
console.log(translate);
    
}

leet("Sos un sorete");
