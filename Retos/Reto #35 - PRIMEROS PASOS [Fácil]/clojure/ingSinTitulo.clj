;; Punto 1: Hola, mundo!
(println "Hola, mundo!")

;; Punto 2: Crea una variable de texto o string
(def miTexto "¡Hola desde Clojure!")

;; Punto 3: Crea una variable de número entero
(def miEntero 42)

;; Punto 4: Crea una variable de número con decimales
(def miDecimal 3.14)

;; Punto 5: Crea una variable de tipo booleano
(def miBooleano true)

;; Punto 6: Crea una constante (en Clojure, las constantes se definen con def)
(def MI_CONSTANTE 10)

;; Punto 7: Usa un if, else if y else
(if (> miEntero 50)
  (println "El número es mayor que 50")
  (if (< miEntero 50)
    (println "El número es menor que 50")
    (println "El número es igual a 50")))

;; Punto 8: Crea un vector
(def miVector [1 2 3 4 5])

;; Punto 9: Crea una lista
(def miLista '("Manzana" "Banana" "Naranja"))

;; Punto 10: Crea una tupla (no aplicable en Clojure)

;; Punto 11: Crea un set
(def miSet #{ "Rojo" "Verde" "Azul" })

;; Punto 12: Crea un diccionario (map en Clojure)
(def miMapa { :clave1 "valor1" :clave2 "valor2" })

;; Punto 13: Usa un ciclo for (no es común en Clojure, se prefiere el uso de funciones de alto nivel)
(doseq [x miVector]
  (println x))

;; Punto 14: Usa un ciclo foreach (no es común en Clojure, se prefiere el uso de funciones de alto nivel)
(doseq [elemento miLista]
  (println elemento))

;; Punto 15: Usa un ciclo while (no es común en Clojure, se prefiere el uso de funciones de alto nivel)
(defn loop-ciclo [contador]
  (if (< contador 3)
    (do
      (println (str "Contador: " contador))
      (recur (inc contador)))))

(loop-ciclo 0)

;; Punto 16: Crea una función sin parámetros que no retorne nada
(defn funcion-sin-parametros []
  (println "Función sin parámetros"))

;; Punto 17: Crea una función con parámetros que no retorne nada
(defn funcion-con-parametros [param1 param2]
  (println (str "Parámetro 1: " param1))
  (println (str "Parámetro 2: " param2)))

;; Punto 18: Crea una función con parámetros que retorne valor
(defn funcion-con-retorno [a b]
  (+ a b))

;; Punto 19: Crea una clase (en Clojure se trabaja mayormente con estructuras de datos inmutables)
(defrecord Persona [nombre edad])

;; Punto 20: Muestra control de excepciones (se manejan con try y catch)
(try
  (/ miEntero 0)
  (catch Exception e
    (println (str "Error: " (.getMessage e)))))
