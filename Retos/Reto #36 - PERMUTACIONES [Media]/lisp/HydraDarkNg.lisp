;; Reto #36: Permutaciones
;;;; Dificultad: Media | Publicación: 04/09/23 | Corrección: 18/09/23

;;; Enunciado

;;
;; Crea un programa que sea capaz de generar e imprimir todas las
;; permutaciones disponibles formadas por las letras de una palabra.
;; - Las palabras generadas no tienen por qué existir.
;; - Deben usarse todas las letras en cada permutación.
;; - Ejemplo: sol, slo, ols, osl, los, lso
;;

(declaim (optimize (speed 3) (safety 0)))

(declaim (ftype (function (list &optional list) list) all-permutations))
(declaim (ftype (function (string) null) generate-permutation))

(defun all-permutations (list &optional (remain list))
  (cond ((null remain) nil)
        ((null (rest list)) (list list))
        (t (append
            (mapcar (lambda (l) (cons (first list) l))
                    (all-permutations (rest list)))
            (all-permutations (append (rest list) (list (first list))) (rest remain))))))

(defun generate-permutation (string)
  (format t "~{~{~a~}~%~}"
	  (all-permutations
	   (map 'list #'identity string))))

(generate-permutation "sol")
