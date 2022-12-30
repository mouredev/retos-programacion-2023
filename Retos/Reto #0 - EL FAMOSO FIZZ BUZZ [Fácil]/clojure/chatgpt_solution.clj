(ns chatgpt-solution)

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

