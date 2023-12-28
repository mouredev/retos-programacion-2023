;; 
;; Implementación usada: sbcl
;; Correr con: sbcl --load HydraDarkNg.lisp
;;

(defun exel-column-to-number (cell)
  (loop for chars across (reverse (string-upcase cell))
	for expt from 0
	for char = (- (char-code chars) 64)
	sum (* char (expt 26 expt))))


(print (exel-column-to-number "A"))
(print (exel-column-to-number "AC"))
(print (exel-column-to-number "CA"))
(print (exel-column-to-number "CZ"))
