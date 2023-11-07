let myArray = [];

for (let i = 1; i <= 100; i++) { 

    // agrego al array los numeros del 1 al 100
    myArray.push(i);    
}

// funcion que muestra los numeros
function mostrarNumeros() {
    
    myArray.forEach(element => {
        
       if (element % 3 == 0 && element % 5 == 0) {
           console.log("fizzbuzz" + "\n");
       }
       else if (element % 3 == 0) {
           console.log("fizz" + "\n");
       }
       else if (element % 5 == 0) {
           console.log("buzz" + "\n");
       }
       else {
           console.log(element);
       }
    });
}

// llamo a la funcion
mostrarNumeros();
