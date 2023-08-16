let a = ['0---00000000',
        '000---000000',
        '---000000000',
        '00---0000000',
        '0000000---00',
        '000000000---',
        '---000000000'];

console.log(`Result : ${getNumber(a)}`);

function getNumber(abacus) {
    if (abacus.length == 7) {
        let m = 1;
        let number = 0;

        for (let i = 6; i >= 0 ; i--) {
            let element = abacus[i];
            if (element.includes('---') && (element.length == 12) && (element.replace('---', '') == '000000000')) {
                number = number  + element.substring(0, element.indexOf("---")).length * m;
                m *= 10;
            } else {
                return "Abacus is incorrect";
            }
        }
       return number.toLocaleString();
    } else {
        return "Abacus is incorrect";
    }
}