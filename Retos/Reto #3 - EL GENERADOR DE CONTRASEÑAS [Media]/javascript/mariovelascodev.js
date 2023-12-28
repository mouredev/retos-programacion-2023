"use strict";

//Función que genera un número aleatorio indicandole el número maximo del rango
function randomNumber(arg) {
    let aleatorio = Math.floor(Math.random() * (arg.length - 0) + 0);
    return aleatorio;
}

//Función que genera una contraseña, según los parametros indicados
function generaPass(longitud, mayusculas = false, numero = false, simbolo = false) {

    //Variables
    let alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
        "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"];
    let numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
    let simbolos = ["!", "#", "@", "$", "%", "&", "(", ")", ">", "<", "-", "?",
        "¿", "¡", "^", "+", "*"];
    let pass = "";
    let caracterAleatorio;


    /*Si la contraseña es mayor que 8 y menor o igual a 16 y se dejan el resto de argumentos por defecto
    se crea una contraseña con solo letras en minusculas*/
    if (longitud >= 8 && longitud <= 16 && mayusculas === false && numero === false && simbolo === false) {
        for (let i = 0; i < longitud; i++) {
            caracterAleatorio = alfabeto[randomNumber(alfabeto)];
            pass += caracterAleatorio;
        }
        /*Si la contraseña es mayor que 8 y menor o igual a 16 y solo se pide que lleve mayusculas, 
        se crea contraseña con letras minusculas y mayusculas*/
    } else if (longitud >= 8 && longitud <= 16 && mayusculas === true && numero === false && simbolo === false) {

        //Genera contraseña en minuscula
        for (let i = 0; i < longitud; i++) {
            caracterAleatorio = alfabeto[randomNumber(alfabeto)];
            pass += caracterAleatorio;
        }

        //Genera contraseña con mayusculas y minusculas
        for (let j = 0; j < pass.length; j++) {
            pass = pass.replace(pass[randomNumber(pass)], pass[randomNumber(pass)].toUpperCase());
        }

        /*Si la contraseña es mayor que 8 y menor o igual a 16 y solo se pide que lleve numeros, 
        se crea contraseña con letras minusculas y numeros*/
    } else if (longitud >= 8 && longitud <= 16 && mayusculas === false && numero === true && simbolo === false) {

        //Genera contraseña en minuscula
        for (let i = 0; i < longitud; i++) {
            caracterAleatorio = alfabeto[randomNumber(alfabeto)];
            pass += caracterAleatorio;
        }

        //Genera contraseña con numeros y letras en minuscula
        for (let j = 0; j < pass.length; j++) {
            pass = pass.replace(pass[randomNumber(pass)], numeros[randomNumber(numeros)]);
        }

        /*Si la contraseña es mayor que 8 y menor o igual a 16 y solo se pide que lleve simbolos, 
        se crea contraseña con letras minusculas y simbolos*/
    } else if (longitud >= 8 && longitud <= 16 && mayusculas === false && numero === false && simbolo === true) {

        //Genera contraseña en minuscula
        for (let i = 0; i < longitud; i++) {
            caracterAleatorio = alfabeto[randomNumber(alfabeto)];
            pass += caracterAleatorio;
        }

        //Genera contraseña con simbolos y letras en minusculas
        for (let j = 0; j < pass.length; j++) {
            pass = pass.replace(pass[randomNumber(pass)], simbolos[randomNumber(simbolos)]);
        }
        /*Si la contraseña es mayor que 8 y menor o igual a 16 y se indica que lleve mayusculas y numeros, 
        se crea contraseña con letras minusculas, mayusculas y numeros*/
    } else if (longitud >= 8 && longitud <= 16 && mayusculas === true && numero === true && simbolo === false) {

        //Genera contraseña en minuscula
        for (let i = 0; i < longitud; i++) {
            caracterAleatorio = alfabeto[randomNumber(alfabeto)];
            pass += caracterAleatorio;
        }

        //Genera contraseña con minusculas, mayusculas y numeros
        for (let j = 0; j < pass.length; j++) {
            pass = pass.replace(pass[randomNumber(pass)], pass[randomNumber(pass)].toUpperCase());
            pass = pass.replace(pass[randomNumber(pass)], numeros[randomNumber(numeros)]);
        }
    } else if (longitud >= 8 && longitud <= 16 && mayusculas === true && numero === false && simbolo === true) {

        //Genera contraseña en minuscula
        for (let i = 0; i < longitud; i++) {
            caracterAleatorio = alfabeto[randomNumber(alfabeto)];
            pass += caracterAleatorio;
        }

        //Genera contraseña con minusculas, mayusculas y simbolos
        for (let j = 0; j < pass.length; j++) {
            pass = pass.replace(pass[randomNumber(pass)], pass[randomNumber(pass)].toUpperCase());
            pass = pass.replace(pass[randomNumber(pass)], simbolos[randomNumber(simbolos)]);
        }
    } else if (longitud >= 8 && longitud <= 16 && mayusculas === false && numero === true && simbolo === true) {

        //Genera contraseña en minuscula
        for (let i = 0; i < longitud; i++) {
            caracterAleatorio = alfabeto[randomNumber(alfabeto)];
            pass += caracterAleatorio;
        }

        //Genera contraseña con minusculas, numeros y simbolos
        for (let j = 0; j < pass.length; j++) {
            pass = pass.replace(pass[randomNumber(pass)], numeros[randomNumber(numeros)]);
            pass = pass.replace(pass[randomNumber(pass)], simbolos[randomNumber(simbolos)]);
        }
    } else if (longitud >= 8 && longitud <= 16 && mayusculas === true && numero === true && simbolo === true) {

        //Genera contraseña en minuscula
        for (let i = 0; i < longitud; i++) {
            caracterAleatorio = alfabeto[randomNumber(alfabeto)];
            pass += caracterAleatorio;
        }

        //Genera contraseña con minusculas, mayusculas, numeros y simbolos
        for (let j = 0; j < pass.length; j++) {
            pass = pass.replace(pass[randomNumber(pass)], pass[randomNumber(pass)].toUpperCase())
                .replace(pass[randomNumber(pass)], numeros[randomNumber(numeros)])
                .replace(pass[randomNumber(pass)], simbolos[randomNumber(simbolos)]);
        }
    } else {
        console.log("La longitud de la contraseña tiene que ser entre 8 y 16 caracteres");
    }
    console.log(pass);
}

generaPass(9, true, true, true);
