(define (find-combinations nums target)
  (define (helper nums target path)
    (cond
      ((= target 0) (list path))
      ((or (< target 0) (null? nums)) '())
      (else (append (helper (cdr nums) (- target (car nums)) (cons (car nums) path))
                    (helper (cdr nums) target path)))))
  (helper nums target '()))

(display (find-combinations '(1 5 3 2) 6))
