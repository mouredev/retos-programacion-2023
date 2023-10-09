;; 
;; Crea una función que encuentre todos los triples pitagóricos
;; (ternas) menores o iguales a un número dado.
;; - Debes buscar información sobre qué es un triple pitagórico.
;; - La función únicamente recibe el número máximo que puede
;;   aparecer en el triple.
;; - Ejemplo: Los triples menores o iguales a 10 están
;;   formados por (3, 4, 5) y (6, 8, 10).
;; 

(defun calculate-pythagorean-triples (m n)
  "Calculate Pythagorean triples for given integers M and N."
  (list
   (- (expt m 2) (expt n 2))
   (* 2 m n)
   (+ (expt m 2) (expt n 2))))

(defun find-pythagorean-treplets-less-than (number)
  "Find Pythagorean triples with a sum less than the given number."
  (remove-if
   (lambda (x) (< number x))
   (loop for m from 2 to (isqrt number)
	 append (loop for n from 1 below m
		      collect (calculate-pythagorean-triples m n)))
   :key #'third))

(defun main (number)
  (format t "~{(~{~a~^, ~})~%~}"
	  (sort
	   (find-pythagorean-treplets-less-than number)
	   #'<		      
	   :key #'third)))

(main 100)
