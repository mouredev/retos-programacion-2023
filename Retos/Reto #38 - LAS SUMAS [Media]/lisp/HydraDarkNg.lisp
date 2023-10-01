;;;
;;; Crea una función que encuentre todas las combinaciones de los números
;;; de una lista que suman el valor objetivo.
;;; - La función recibirá una lista de números enteros positivos
;;;   y un valor objetivo.
;;; - Para obtener las combinaciones sólo se puede usar
;;;   una vez cada elemento de la lista (pero pueden existir
;;;   elementos repetidos en ella).
;;; - Ejemplo: Lista = [1, 5, 3, 2],  Objetivo = 6
;;;   Soluciones: [1, 5] y [1, 3, 2] (ambas combinaciones suman 6)
;;;   (Si no existen combinaciones, retornar una lista vacía)
;;;

(defun combinations-finder (numbers target)
  (labels ((combinations-helper (nums acc)
             (cond
               ((= (apply #'+ acc) target) (list acc))
               ((or (null nums) (> (apply #'+ acc) target)) nil)
               (t (append (combinations-helper (cdr nums) (append acc (list (car nums))))
                          (combinations-helper (cdr nums) acc))))))
    (combinations-helper numbers '())))

(combinations '(1 5 3 2) 12)
