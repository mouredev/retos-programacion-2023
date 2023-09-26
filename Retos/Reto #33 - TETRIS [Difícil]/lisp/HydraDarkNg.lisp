;; 
;; Implementación: sbcl
;; Correr con: sbcl --script HydraDarkNg.lisp
;; 

(defvar *commands* (make-hash-table :test #'equal))
(defvar *board* (make-array '(10 10) :element-type 'character :initial-element #\⬛))
(defvar *x-pos* 0)
(defvar *y-pos* 0)
(defvar *rotate* 0)

(defparameter *piece-states*
  '(((0 0) (1 0) (1 1) (1 2))
    ((0 1) (0 0) (1 0) (2 0))
    ((0 0) (0 1) (0 2) (1 2))
    ((0 1) (1 1) (2 1) (2 0))))

(defun print-board ()
  (loop for y from 0 to 9 do
    (loop for x from 0 to 9 do
      (format t "~a" (aref *board* y x)))
	(format t "~%")))

(defun restart-board ()
  (loop for y from 0 to 9 do
    (loop for x from 0 to 9 do
      (setf (aref *board* y x) #\⬛))))

(defun print-state ()
  (loop for coordinates in (nth *rotate* *piece-states*)
	do (setf (aref *board*
		       (+ *y-pos* (first coordinates))
		       (+ *x-pos* (second coordinates)))
		 #\⬜)))

(defmacro add-command (command &body body)
  `(setf (gethash ,command *commands*)
	 (lambda ()
	   (restart-board)
	   ,@body
	   (print-state)
	   (print-board))))

(defmacro run-command (command)
  `(funcall (gethash ,command *commands*)))

(add-command "print" nil)

(add-command "reiniciar"
  (setf *x-pos* 0)
  (setf *y-pos* 0)
  (setf *rotate* 0))

(defun checkp (rotate-one rotate-two axis axis-value)
  (and
   (or (= rotate-one *rotate*)
       (= rotate-two *rotate*))
   (= axis axis-value)))

(defun rotatep ()
  (cond
    ((checkp 1 3 *x-pos* 8) nil)
    ((checkp 0 2 *y-pos* 8) nil)
    (t t)))

(add-command "rotar"
  (when (rotatep)
    (cond
      ((= *rotate* 3) (setf *rotate* 0))
      (t (incf *rotate*)))))

(defun downp ()
  (cond
    ((checkp 0 2 *y-pos* 8) nil)
    ((checkp 1 3 *y-pos* 7) nil)
    (t t)))

(add-command "abajo"
  (when (downp)
    (incf *y-pos*)))

(defun rightp ()
  (cond
    ((checkp 0 2 *x-pos* 7) nil)
    ((checkp 1 3 *x-pos* 8) nil)
    (t t)))

(add-command "derecha"
  (when (rightp)
    (incf *x-pos*)))

(add-command "izquierda"
  (unless (= *x-pos* 0)
    (decf *x-pos*)))

(add-command "exit"
  (cl-user::quit))

(defun command ()
  (let ((command (read-line)))
    (if (gethash command *commands*)
	(run-command command)
	(progn (format t "La acción ~a no existe, por favor ingrese otra.~%" command)
	       (force-output)
	       (print-board)))))

(defun main ()
  (print-state)
  (print-board)
  (loop
    (format t "Ingrese una acción(izquierda,derecha,abajo,rotar,reiniciar,exit): ")
    (force-output)
    (command)))

(main)
