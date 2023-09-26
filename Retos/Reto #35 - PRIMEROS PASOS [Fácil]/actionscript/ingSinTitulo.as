package {
    import flash.display.Sprite;
    
    public class MiPrograma extends Sprite {
        
        public function MiPrograma() {
            // Punto 1: Hola, mundo!
            trace("Hola, mundo!");
            
            // Punto 2: Crea una variable de texto o string
            var miTexto:String = "¡Hola desde ActionScript!";
            
            // Punto 3: Crea una variable de número entero
            var miNumeroEntero:int = 42;
            
            // Punto 4: Crea una variable de número con decimales
            var miNumeroDecimal:Number = 3.14;
            
            // Punto 5: Crea una variable de tipo booleano
            var miBooleano:Boolean = true;
            
            // Punto 6: Crea una constante
            const MI_CONSTANTE:String = "Valor constante";
            
            // Punto 7: Usa un if, else if y else
            if (miNumeroEntero > 50) {
                trace("El número es mayor que 50");
            } else if (miNumeroEntero < 50) {
                trace("El número es menor que 50");
            } else {
                trace("El número es igual a 50");
            }
            
            // Punto 8: Crea un Array
            var miArray:Array = [1, 2, 3, 4, 5];
            
            // Punto 9: Crea una lista (Array en ActionScript)
            var miLista:Array = ["Manzana", "Banana", "Naranja"];
            
            // Punto 10: Crea una tupla (no aplicable en ActionScript)
            
            // Punto 11: Crea un set (no aplicable en ActionScript)
            
            // Punto 12: Crea un diccionario (Object en ActionScript)
            var miDiccionario:Object = { "clave1": "valor1", "clave2": "valor2" };
            
            // Punto 13: Usa un ciclo for
            for (var i:int = 0; i < miArray.length; i++) {
                trace(miArray[i]);
            }
            
            // Punto 14: Usa un ciclo foreach (for-in)
            for each (var elemento:String in miLista) {
                trace(elemento);
            }
            
            // Punto 15: Usa un ciclo while
            var contador:int = 0;
            while (contador < 3) {
                trace("Contador: " + contador);
                contador++;
            }
            
            // Punto 16: Crea una función sin parámetros que no retorne nada
            function funcionSinParametros():void {
                trace("Función sin parámetros");
            }
            
            // Punto 17: Crea una función con parámetros que no retorne nada
            function funcionConParametros(param1:int, param2:String):void {
                trace("Parámetro 1: " + param1);
                trace("Parámetro 2: " + param2);
            }
            
            // Punto 18: Crea una función con parámetros que retorne valor
            function funcionConRetorno(a:int, b:int):int {
                return a + b;
            }
            
            // Punto 19: Crea una clase
            var miPersona:Persona = new Persona("Juan", 30);
            
            // Punto 20: Muestra control de excepciones
            try {
                var resultado:Number = miNumeroEntero / 0;
            } catch (error:Error) {
                trace("Error: " + error.message);
            }
        }
    }
}

class Persona {
    public var nombre:String;
    public var edad:int;
    
    public function Persona(nombre:String, edad:int) {
        this.nombre = nombre;
        this.edad = edad;
    }
}
