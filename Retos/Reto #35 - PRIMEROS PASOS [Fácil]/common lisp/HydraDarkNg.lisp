;;; Funciones
;; Sin parametros
(defun imprimir-separacion ()
  (format t "~20@{~a~:*~}~%" "**"))

(defun imprimir-separacion-personalizada (separacion)
  (format t "~20@{~a~:*~}~%" separacion))

;;; Hola Mundo.
(format t "Hola Mundo.~%")

(imprimir-separacion)

;;; Variables
;; Variable de tipo string.
(defparameter mi-string "Hola Mundo")

;; Variables numéricas, hay muchas: enteros,decimales,racionales y complejos.
;; Variable de tipo entero.
(defparameter mi-entero 10)

;; Variable de tipo decimales.
(defparameter mi-decimal 1.2)

;; Variable de tipo booleano.
(defparameter mi-booleano t)

;;; Constante
(defconstant e 2.71828d0
  "Número e")

;;; Comprobación de casos
;; if y else
(if (< 1 2)
    (format t "Este número es menor a 2.~%")
    (format t "Este número no es menor a 2.~%"))

;; Cond comprueba cual es el primero en en ser cierto, por eso solo ejecuta que 0 es menor que uno
(cond 
  ((< 2 2) (format t "Este es un numero menor a dos.~%"))
  ((< 0 1) (format t "Este numero es menor a uno.~%"))
  ((< -1 0) (format t "Este numero es menor a uno.~%")))

(imprimir-separacion)

;;; Estructuras
;; Array
(defparameter mi-array #(1 2 3))

;; Listas o sets, en common lisp son básicamente lo mismo
(defparameter mi-lista '(1 2 3 4))
(defparameter mi-conjunto '(4 5 6 7))

(format t "Mi union de listas o conjuntos ~a.~%"
	(union mi-lista mi-conjunto))

(format t "Mi intersección de listas o conjuntos ~a.~%"
	(intersection mi-lista mi-conjunto))

;; Diccionario
(defparameter mi-diccionario (make-hash-table))

;; Tupla en common lisp no existe este tipo de dato

(imprimir-separacion)

;;; Bucles
;; for
(loop for i from 0 to 10
      do (format t "~a~%" i))

(imprimir-separacion)

;; for each
(loop for i in mi-lista
      do (format t "~a~%" i))

(imprimir-separacion)

;; While
(defparameter x 0)
(loop while (< x 20)
      do (format t "~a~%" x) (incf x))

(imprimir-separacion-personalizada "++")

;;; Clases
(defclass persona ()
  ((nombre :initarg :nombre
	   :accessor nombre)
   (edad :initarg :edad
	 :accessor edad)))

(defmethod saludar ((persona persona))
  (format t "Hola, mi nombre es ~a y mi edad es ~a.~%"
	  (nombre persona)
	  (edad persona)))

(defparameter mi-persona (make-instance 'persona
					:nombre "Mouredev"
					:edad 22))

(saludar mi-persona)

(imprimir-separacion-personalizada "++")
;;; Control de excepciones.
(handler-case (/ 1 0)
  (division-by-zero ()
    (format t "No se pude dividir entre cero~%")))
