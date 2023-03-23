//Reto realizado por Xousse
'use strict'

// [...Array(101).keys()] --> Crear un array de 0 a 100
// .slice(1) --> la corta del 1 en adelante para tener los numeros del 1 al 100
//.map permite ejecutar una operacion por valor en el array 
const deUnoACien = [...Array(101).keys()].slice(1).map(number =>{
    // Si el numero es multiplo de 3 y 5 guardo fizzbuzz ene el array
    if ((number % 3 === 0) && (number % 5 === 0)){
        return number = `fizzbuzz`;
    // Sino si el numero es multiplo de 3 guardo fizz en el array
    }else if (number % 3 === 0){
        return number = `fizz`;
    // Sino si el numero es multiplo de 5 guardo buzz en el array
    }else if(number % 5 === 0){
        return number = `buzz`;
    }else{
        // Sino se da ninguna condicion paso el numero a string para imprimirlo despues
        return number.toString();
    }
});

//Hago un map para hacer la operacion de imprimir por pantalla cada valor del array
deUnoACien.map(number => console.log(number));

//Si quieres ver el contenido del array, descomenta la siguiente linea
//console.log(deUnoACien);





