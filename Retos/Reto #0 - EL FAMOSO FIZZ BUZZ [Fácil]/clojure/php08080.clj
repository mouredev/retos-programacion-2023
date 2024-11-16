
 ; Escribe un programa que muestre por consola (con un print) los
 ; números de 1 a 100 (ambos incluidos y con un salto de línea entre
 ; cada impresión), sustituyendo los siguientes:
 ; - Múltiplos de 3 por la palabra "fizz".
 ; - Múltiplos de 5 por la palabra "buzz".
 ; - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 ;
 
(defn imprimir [lista]
  (doseq [n lista]
    (cond
      (zero? (mod n 15)) (println n "FizzBuzz")
      (zero? (mod n 3))  (println n "Fizz")
      (zero? (mod n 5))  (println n "Buzz")
      :else (println n))))

(imprimir (range 1 101))

 ;demaciado imperativo a mi gusto :c

