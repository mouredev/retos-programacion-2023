;;;
;;; Crea las funciones capaces de transformar colores HEX
;;; a RGB y viceversa.
;;; Ejemplos:
;;; RGB a HEX: r: 0, g: 0, b: 0 -> #000000
;;; HEX a RGB: hex: #000000 -> (r: 0, g: 0, b: 0)
;;;

(defun hex->rgb (hex)
  (let ((r (parse-integer (subseq hex 1 3) :radix 16))
	(g (parse-integer (subseq hex 3 5) :radix 16))
	(b (parse-integer (subseq hex 5 7) :radix 16)))
    (format t "r: ~a, g: ~a, b: ~a~&" r g b)))

(defun position-rgb (string letter &optional end)
  (subseq string
	  (+ 3 letter)
	  (unless end
	    (+ 6 letter))))

(defun rgb->hex (rgb)  
  (let ((r (position #\r rgb))
	(g (position #\g rgb))
	(b (position #\b rgb)))
    (format t "#~x~x~x~&"
	    (parse-integer (position-rgb rgb r))
	    (parse-integer (position-rgb rgb g))
	    (parse-integer (position-rgb rgb b t)))))

(defun main ()
  (hex->rgb "#ffff00")
  (rgb->hex "r: 255, g: 255, b: 1"))

(main)
