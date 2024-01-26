let traductor = (texto) => {
    let diccionario = {
        A:"4",
        B:"I3", 
        C:"[",
        D:")",
        E:"3",
        F:"|=",
        G:"&",
        H:"#",
        I:"1",
        J:",_|",
        K:">|",
        L:"1",
        M:"/\\/\\",
        N:"^/",
        O:"0",
        P:"|*",
        Q:"(_,)",
        R:"I2",
        S:"5",
        T:"7",
        U:"(_)",
        V:"\/",
        W:"\/\/",
        X:"><",
        Y:"j",
        Z:"2",
        0:"o",
        1:"L",
        2:"R",
        3:"E",
        4:"A",
        5:"S",
        6:"b",
        7:"T",
        8:"B",
        9:"g",
    };
    let traducido = "";
    for (let caracter of texto.toUpperCase()){
        if (caracter in diccionario){
            traducido += diccionario[caracter]
        } else {
            traducido += caracter
        }
    }
    console.log(traducido)
}
traductor("El Iram chupa Penes")

