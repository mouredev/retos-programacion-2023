/*
 * Crea un programa que analice texto y obtenga:
 * - Número total de palabras.
 * - Longitud media de las palabras.
 * - Número de oraciones del texto (cada vez que aparecen un punto).
 * - Encuentre la palabra más larga.
 *
 * Todo esto utilizando un único bucle.  
 */
fun main() {
    analiceTexto("Los discos son dispositivos formados por componentes electromagnéticos que permiten un acceso rápido a bloques físicos  de  datos. La información se registra en la superficie del disco y se accede a ella por medio de cabezas de lectura/escritura que se mueven sobre la superficie.")
}

class analiceTexto(var texto: String){
    var listaPalabra : List<String>
    
    init{
        println("\n$texto\n\nResultado")
        listaPalabra = texto.split(" ")
        
        numeroTotalPalabras()
        mediaLogitud()
        numeroOracions()
        palabraLarga()
    }
    
    private fun numeroTotalPalabras(){
        println("Número total de palabras: ${listaPalabra.size}")
    }
    
    private fun mediaLogitud(){
        var totalSize = 0
        
        listaPalabra.map{ it ->
            totalSize += it.length
        }
        
        println("Longitud media de las palabras: ${totalSize/listaPalabra.size}")
    }
    
    private fun numeroOracions(){
        var numeroParafo = 0
        
        listaPalabra.map{ it ->
            
            if(it.contains('.')) 
               numeroParafo++
        }
        
        println("Número de oraciones del texto $numeroParafo")
    }
    
    private fun palabraLarga(){
        //Encuentre la palabra más larga.
        var palabraLarga = ""
        var numero = 0
        
        listaPalabra.map{ it ->
          
            if(numero < it.length){
                numero = it.length
                palabraLarga = it
            } 
        }
        
        println("La palabra más larga es : $palabraLarga")
    }
}
