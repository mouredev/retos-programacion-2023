const reto = (operacion: string): boolean => {
    let v = false;
    try {
        let resultado = eval(operacion);
        v = true;
    } catch (error) {
        v = false;
    }
    console.log(`${operacion} -> ${v}`);
    return v;
};

reto("5 + 6 / 7 - 4");
reto("5 a 6");
