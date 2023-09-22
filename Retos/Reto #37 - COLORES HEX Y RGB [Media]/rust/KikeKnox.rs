/*
 * Crea las funciones capaces de transformar colores HEX
 * a RGB y viceversa.
 * Ejemplos:
 * RGB a HEX: r: 0, g: 0, b: 0 -> #000000
 * HEX a RGB: hex: #000000 -> (r: 0, g: 0, b: 0)
 */

/* 
 * Nota del autor (sease, yo, KikeKnox, Aique_Knox)
 * Se que hay cosas mejorables, es mi primerito programa con Rust
 */

use std::io;    //Buenas practicas al parecer

fn encontrarCaracter(cadena: &str, caracter: char) -> i32 {
    /* Funcion para devolver numericamente la posicion de un caracter en una cadena
     * Entrada: la direccion de la cadena y el caracter a buscar
     * Salida: la posicion si se encuentra o -1 si no
     */
    if let Some(posicion) = cadena.find(caracter) {
        posicion as i32
    } else {
        -1
    }
}

fn entradaValida(entrada: &String) -> (bool, bool) {
    /* Funcion aparte para analizar si la entrada es valida de forma basica
     * Entrada: Direccion de la entrada de usuario
     * Salida: Tupla de dos booleanos (valida y RGB/HEX)
     */
    
    //Se comprueba si tiene las letras RGB y #
    let tieneR = entrada.contains('R');
    let tieneG = entrada.contains('G');
    let tieneB = entrada.contains('B');
    let hx = entrada.contains('#');

    //Valido si contiene RGB XOR (or excluyente) # del hexadecimal. No pueden ser los dos a la vez
    let valid = (tieneR & tieneG & tieneB) ^ hx;
    
    (valid,hx)
}

fn main(){
    let mut EXIT = false;   //Esta variable tiene que recordar el valor en cada ejecucion

    //Bucle de ejecuccion continua (Rust tiene loop, pero mantengo mi C++)
    while !EXIT {
        //Declaracion de variables mutables
        let mut color = String::new();
        let mut colorLimp = String::new();

        //Salida por pantalla inicial
        println!("Programa para convertir codigos de colores");
        println!("Para salir, introduzca la palabra EXIT\n");
        println!("Formatos de entrada:");
        println!("  - RGB: (r: XXX, g: XXX, b: XXX)");
        println!("  - HEX: #XXXXXX\n");
        println!("Introduce tu color:");

        //Lectura de entrada (y salida de programa si exigido)
        io::stdin().read_line(&mut color).expect("Ya vere que hacer con esto");
        colorLimp = color.trim().to_string().to_uppercase();   //Se limpia la entrada de espacios y se pone mayuscula
        EXIT = colorLimp == "EXIT"; //Booleano de control de ejecuccion
        if EXIT {break;}    //Pa que seguir con la ejecuccion

        //Lo guapo: comprobar que la entrada es valida
        let (esValida, esHEX) = entradaValida(&colorLimp);
        if !esValida {
            println!("La entrada no es valida, vuelve a intentarlo respetando el formato\n\n");
            continue;
        }
        
        //Bloque de conversion
        if esHEX {
            /*
             * La entrada es hexadecimal
             * #-XX-XX-XX
             */

            //Conversion por pares (empezamos en 1 porque 0 es #)
            let hxR = u32::from_str_radix(&colorLimp[1..3], 16).expect("Error al convertir a decimal la parte roja");
            let hxG = u32::from_str_radix(&colorLimp[3..5], 16).expect("Error al convertir a decimal la parte verde");
            let hxB = u32::from_str_radix(&colorLimp[5..], 16).expect("Error al convertir a decimal la parte azul");

            println!("Color en RGB: (r: {}, g: {}, b:{})\n\n",hxR,hxG,hxB);
        } else {
            /*
             * La entrada es RGB (decimal)
             * (r: xxx, g: xxx, b: xxx)
             */
            
            //Primero hay que estandarizar la entrada por si acaso. En teoria no hay espacios ni minusculas ya
            let colorStd: String = colorLimp.chars().filter(|c| c.is_alphanumeric()).collect(); //Se filtra y guarda los alfanumericos solamente
            
            //Posicion de las letras G y B (R esta en 0)
            let posG = encontrarCaracter(&colorStd,'G') as usize;
            let posB = encontrarCaracter(&colorStd,'B') as usize;

            //Fragmentacion a los componentes
            let hxR = &colorStd[1..posG];
            let hxG = &colorStd[posG+1..posB];
            let hxB = &colorStd[posB+1..];

            //Conversion a string otra vez
            let hxRs = hxR.to_string();
            let hxGs = hxG.to_string();
            let hxBs = hxB.to_string();

            //Conversion a u8
            let mut hxRu8 = 0;
            match hxRs.parse::<u8>() {
                Ok(Rs) => {
                    hxRu8 = Rs;
                },
                Err(e)=>{}
            }
            let mut hxGu8 = 0;
            match hxGs.parse::<u8>() {
                Ok(Gs) => {
                    hxGu8 = Gs;
                },
                Err(e)=>{}
            }
            let mut hxBu8 = 0;
            match hxBs.parse::<u8>() {
                Ok(Bs) => {
                    hxBu8 = Bs;
                },
                Err(e)=>{}
            }

            println!("Color en HEX: #{:02X}{:02X}{:02X}\n\n",hxRu8,hxGu8,hxBu8);
        }
    }

    //Mi madre crio a un ingeniero educado
    println!("Hasta pronto!\n\n");
}