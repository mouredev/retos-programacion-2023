//Escribe un programa que muestre por consola (con un print) los números de 1 a 100 
//(ambos incluidos y con un salto de línea entre cada impresión), sustituyendo los siguientes:
// - Múltiplos de 3 por la palabra "fizz".
// - Múltiplos de 5 por la palabra "buzz".
// - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".


//Se crea la variable 'numero'.
int numero=0;

//Inicia Void Setup().
void setup(){
  
  //Especificamos la velocidad de transmisión de el puerto serie.
  Serial.begin(9600);
  
  //Hacemos el for para el ejercicio
  for(numero=0; numero<=100; numero++){  // for(inicializa la variable en 0; condición; incrementa la variable).
  
    if((numero%3==0)&&(numero%5==0)){    //Realiza la condición que se le dice, Si el residuo de numero/3 es 
                                         //igual a 0 y el residuo de numero/5 es  igual a 0  entonces:

        Serial.print("Fizzbuzz");        //Imprime 'Fizzbuzz'.
    }
    else if(numero%3==0){      //Si el residuo de numero/3 es  igual a 0 entonces:

        Serial.print("Fizz");  //Imprime 'Fizz'.
    }
    else if(numero%5==0){      //Si el residuo de numero/5 es  igual a 0 entonces:
    
        Serial.print("Buzz");  //Imprime 'Buzz'.
    }
    else if((numero%3!=0)&&(numero%5!=0)){ //Y si el residuo de numero/3 es distinto a 0 y el residuo de 
                                           //numero/5 es distinto a 0  entonces:

        Serial.print(numero);  //Imprime el número.
    }
  Serial.print("\n"); //Aquí se hace un salto de línea para que no esten pegados los números.
  }

}

//El void loop() no lo usamos para nada. 
void loop(){

}
