const columna = "XFD";
const ASCII_LET_A = 'A'.charCodeAt();
const acc = (tot,act,idx) =>{
    let val = (act.charCodeAt() - ASCII_LET_A) + 1;
    val *= (26**idx);
    return tot+val;
};
const valorTotal = columna.toUpperCase().split('').reverse().reduce(acc,1);
console.log(`La columna ${columna} corresponde a ${valorTotal}`);