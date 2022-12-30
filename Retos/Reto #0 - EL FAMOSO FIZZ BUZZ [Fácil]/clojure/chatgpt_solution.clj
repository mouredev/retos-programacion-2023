(ns chatgpt-solution)

; Write me a program in Clojure.
; These are the instructions:
; A program that prints out numbers 1 to 100
; on a newline while replacing numbers that
; are multiples of 3 with the string “fizz”,
; replacing numbers that are multiples of 5
; with the string “buzz”, and replacing the
; numbers that are multiple of both 3 & 5
; with the string “fizzbuzz”.

(defn fizzbuzz []
  (doseq [i (range 1 101)]
    (if (and (zero? (mod i 3)) (zero? (mod i 5)))
      (println "fizzbuzz")
      (if (zero? (mod i 3))
        (println "fizz")
        (if (zero? (mod i 5))
          (println "buzz")
          (println i))))))

(fizzbuzz)

