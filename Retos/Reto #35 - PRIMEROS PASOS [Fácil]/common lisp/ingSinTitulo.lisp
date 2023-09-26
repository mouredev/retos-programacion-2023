;; Punto 1: Hola, mundo!
(format t "Hola, mundo!~%")

;; Punto 2: Crea una variable de texto o string
(defparameter mi-texto "¡Hola desde Lisp!")

;; Punto 3: Crea una variable de número entero
(defparameter mi-entero 42)

;; Punto 4: Crea una variable de número con decimales
(defparameter mi-decimal 3.14)

;; Punto 5: Crea una variable de tipo booleano
(defparameter mi-booleano t)

;; Punto 6: Crea una constante
(defconstant mi-constante 10)

;; Punto 7: Usa un if, else if y else
(defun ejemplo-if (x)
  (if (> x 50)
      "El número es mayor que 50"
      (if (< x 50)
          "El número es menor que 50"
          "El número es igual a 50")))

;; Punto 8: Crea un Array (vector en Lisp)
(defparameter mi-array #(1 2 3 4 5))

;; Punto 9: Crea una lista (lista en Lisp)
(defparameter mi-lista '("Manzana" "Banana" "Naranja"))

;; Punto 10: Crea una tupla (no aplicable en Lisp)

;; Punto 11: Crea un set (no aplicable en Lisp)

;; Punto 12: Crea un diccionario (no aplicable en Lisp)

;; Punto 13: Usa un ciclo for (no es común en Lisp, se prefieren funciones recursivas)
;; Punto 14: Usa un ciclo foreach (no es común en Lisp, se prefieren funciones recursivas)

;; Punto 15: Usa un ciclo while (no es común en Lisp, se prefieren funciones recursivas)

;; Punto 16: Crea una función sin parámetros que no retorne nada
(defun funcion-sin-parametros ()
  (format t "Función sin parámetros~%"))

;; Punto 17: Crea una función con parámetros que no retorne nada
(defun funcion-con-parametros (param1 param2)
  (format t "Parámetro 1: ~a~%" param1)
  (format t "Parámetro 2: ~a~%" param2))

;; Punto 18: Crea una función con parámetros que retorne valor
(defun funcion-con-retorno (a b)
  (+ a b))

;; Punto 19: Crea una clase (no hay clases en Lisp, se usan estructuras y tipos definidos por el usuario)

;; Punto 20: Muestra control de excepciones (no es común en Lisp, se prefieren valores de retorno para errores)
