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

(defun split (string)
  (loop for i = 0 then (1+ j)
	as j = (position #\, string :start i)
        collect (subseq string i j)
        while j))

(defun rgb->hex (rgb)  
  (let ((rgb (loop for i in (split rgb)
		   collect (parse-integer i :start 3 :junk-allowed t))))
    (format t "#~{~2,'0x~}~&"
	    rgb)))

(defun main ()
  (hex->rgb "#ffff00")
  (rgb->hex "r: 255, g: 255, b: 1"))

(main)
