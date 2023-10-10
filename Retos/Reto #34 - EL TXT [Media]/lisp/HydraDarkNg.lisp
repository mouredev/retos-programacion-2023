(defun main ()
  (let ((file-name "text.txt")
	(options
	  '("1. Continuar escribiendo"
	    "2. Borrar el contenido y escribir"
	    "3. Salir")))
    (loop
      (format t "Elige una opcion:~%~{~a~%~}" options)
      (force-output)
      (let ((option (read-line)))
	(cond
	  ((string= option "1" :end1 1)
	   (with-open-file (file file-name :direction :output :if-exists :append :if-does-not-exist :create)
	     (let ((line (read-line)))
	       (format file "~a~%" line))))
	  ((string= option "2" :end1 1)
	   (with-open-file (file file-name :direction :output :if-exists :append :if-does-not-exist :create)
	     (let ((line (read-line)))
	       (format file "~a~%" line))))
	  ((string= option "3" :end1 1)
	   (cl-user::quit)))))))

(main)
