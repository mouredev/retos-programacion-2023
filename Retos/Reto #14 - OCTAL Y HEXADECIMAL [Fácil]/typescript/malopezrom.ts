/*
 * Crea una función que reciba un número decimal y lo trasforme a Octal
 * y Hexadecimal.
 * - No está permitido usar funciones propias del lenguaje de programación que
 * realicen esas operaciones directamente.
 */



import { readFileSync } from "fs";

/**
 * Funciones de extension para los numeros
 */
declare global {
    interface Number {
        /**
         * Funcion de extension que convierte un numero decimal a octal
         */
        toOctal(): number;

        /**
         * Funcion de extension que convierte un numero decimal a hexadecimal
         */
        toHexadecimal(): string;
    }
}

/**
 * Funcion de extension que convierte un numero decimal a octal
 */
Number.prototype.toOctal = function (): number {
    let octal = 0;
    let decimal = Math.floor(this.valueOf());
    let i = 1;
    while (decimal !== 0) {
        octal += (decimal % 8) * i;
        decimal = Math.floor(decimal / 8);
        i *= 10;
    }
    return octal;
};

/**
 * Funcion de extension que convierte un numero decimal a hexadecimal
 */
Number.prototype.toHexadecimal = function (): string {
    let hexadecimal = "";
    let decimal = Math.floor(this.valueOf());
    while (decimal !== 0) {
        const value = decimal % 16;
        if (value < 10) {
            hexadecimal = `${value}${hexadecimal}`;
        } else {
            hexadecimal = `${String.fromCharCode(value + 55)}${hexadecimal}`;
        }
        decimal = Math.floor(decimal / 16);
    }
    return hexadecimal;
}


const value:number = 255
console.log(`Octal : ${value.toOctal()}`)
console.log(`Hexadecimal ${value.toHexadecimal()}`)
