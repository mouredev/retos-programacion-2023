;;; 
;;; Crea un programa que sea capaz de solicitarte un número y se
;;; encargue de imprimir su tabla de multiplicar entre el 1 y el 10.
;;; - Debe visualizarse qué operación se realiza y su resultado.
;;;   Ej: 1 x 1 = 1
;;;       1 x 2 = 2
;;;       1 x 3 = 3
;;;       ... 
;;;

(defun main ()
  (format t "Ingresa un número: ")
  (force-output)
  (let ((number (parse-integer (read-line))))
    (loop for i from 1 to 10 do
      (format t "~a x ~2,' d = ~a~%" number i (* number i)))))

(main)
