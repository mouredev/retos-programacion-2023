(ns jorgediazjr)

; Exercise 01:
; Write a program that will print to terminal the numbers
; 1 to 100 inclusive and an extra new line after each
; printed number, while substituting the following:
;   - Multiples of 3 replaced with "fizz"
;   - Multiples of 5 replaced with "buzz"
;   - Multiples of 3 & 5 replaced with "fizzbuzz"

(defn replace-with-fizzbuzz [number]
  (cond
    (and (= 0 (rem number 5)) (= 0 (rem number 3))) (str "fizzbuzz" "\n")
    (= 0 (rem number 3)) (str "fizz" "\n")
    (= 0 (rem number 5)) (str "buzz" "\n")
    :else (str number "\n")))

(defn print-fizz-buzz-sequence []
  (->>
    (range 1 101)
    (map replace-with-fizzbuzz)
    (run! println)))


(print-fizz-buzz-sequence)
