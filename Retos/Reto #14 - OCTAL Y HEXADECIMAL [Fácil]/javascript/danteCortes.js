/**
 * Elementos HTML
 * 
 * <input type="text" placeholder="Número" id="txtNumber">
 * <button id="btnConvertOctal">Convertir Octal</button>
 * <button id="btnConvertHexadecimal">Convertir Hexadecimal</button>
 * <br>
 * <label id="lblResponse"></label>
 * 
 */

let btnConvertOctal = document.getElementById("btnConvertOctal");
let btnConvertHexadecimal = document.getElementById("btnConvertHexadecimal");
let txtNumber = document.getElementById("txtNumber");
let lblResponse = document.getElementById("lblResponse");

btnConvertOctal.addEventListener('click', function(){

    let convertir = new Convertir(new SistemaOctal);
    lblResponse.innerText = `Numeración en base octal: ${convertir.convert(txtNumber.value)}`;
});

btnConvertHexadecimal.addEventListener('click', function(){

    let convertir = new Convertir(new SistemaHexadecimal);
    lblResponse.innerText = `Numeración en base hexadecimal: ${convertir.convert(txtNumber.value)}`;
});

class SistemaInterface
{
    convertir()
    {
        throw new Error('El método convertir debe ser implementado por las subclases.');
    }
}

class SistemaOctal extends SistemaInterface
{
    convertir = (number) => {
        let resto = number % 8;
        number = Math.floor(number / 8);
        if(number < 8){
            return Math.floor(`${number}${resto}`);
        }else{
            return `${this.convertir(number)}${resto}`;
        }
    }
}

class SistemaHexadecimal extends SistemaInterface
{
    convertir = (number) => {
        let resto = number % 16;
        number = Math.floor(number/16);
        if(number < 16){
            return `${this.evaluate(number)}${this.evaluate(resto)}`;
        }else{
            return this.convertir(number).this.evaluate(resto);
        }
    }

    evaluate = (number) => {
        if(number > 9){
            return String.fromCharCode(number + 55);
        }
        return number;
    }
}

class Convertir
{
    constructor(sistemaInterface)
    {
        this.sistemaInterface = sistemaInterface;
    }

    convert(number)
    {
        return this.sistemaInterface.convertir(number);
    }
}