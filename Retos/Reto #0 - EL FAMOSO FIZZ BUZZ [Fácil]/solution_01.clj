(ns solution-01)

(defn replace-with-fizzbuzz [number]
  (cond
    (and (= 0 (rem number 5)) (= 0 (rem number 3))) (str "fizzbuzz" "\n")
    (= 0 (rem number 3)) (str "fizz" "\n")
    (= 0 (rem number 5)) (str "buzz" "\n")
    :else (str number "\n")))

(defn get-fizz-buzz []
  (->>
    (range 1 101)
    (map replace-with-fizzbuzz)
    (run! println)))


(get-fizz-buzz)
