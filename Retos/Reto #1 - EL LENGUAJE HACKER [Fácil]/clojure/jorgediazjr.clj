(ns jorgediazjr)
(require '[clojure.string :as str])

;; Exercise 02:
;;
;; replace characters using leet alphabet
;; https://www.gamehouse.com/blog/leet-speak-cheat-sheet/

(def basic-leet-map {"a" "4"
                     "e" "3"
                     "i" "1"
                     "o" "0"
                     "u" "0"})

(def intermediate-leet-map {"a" "4"
                            "b" "I3"
                            "c" "["
                            "d" "|)"
                            "e" "3"
                            "f" "ph"
                            "g" "6"
                            "h" "#"
                            "i" "1"
                            "j" "]"
                            "k" "|<"
                            "l" "1"
                            "m" "/\\/\\"
                            "n" "|\\|"
                            "o" "0"
                            "p" "|>"
                            "q" "0_"
                            "r" "I2"
                            "s" "5"
                            "t" "7"
                            "u" "(_)"
                            "v" "\\/"
                            "w" "\\/\\/"
                            "x" "><"
                            "y" "j"
                            "z" "2"})

(def advanced-leet-map {"a" "/\\"
                        "b" "I3"
                        "c" "{"
                        "d" "|>"
                        "e" "ë"
                        "f" "/="
                        "g" "9"
                        "h" "]-["
                        "i" "]["
                        "j" "._]"
                        "k" "|("
                        "l" "1"
                        "m" "[V]"
                        "n" "<\\>"
                        "o" "<>"
                        "p" "|*"
                        "q" "9"
                        "r" "12"
                        "s" "5"
                        "t" "7"
                        "u" "|_|"
                        "v" "\\|"
                        "w" "VV"
                        "x" ")("
                        "y" "'/'"
                        "z" "7_"})

(def leet-maps {"basic" basic-leet-map
                "intermediate" intermediate-leet-map
                "advanced" advanced-leet-map})

(defn get-leet-message [message leet-type]
  (letfn [(replace-chars-with-leet [message-char]
            (let [m-char (str/lower-case message-char)
                  chosen-leet-map (get leet-maps leet-type)]
              (cond
                (contains? chosen-leet-map m-char) (get chosen-leet-map m-char)
                :else message-char)))]
    (str/join "" (map replace-chars-with-leet (seq (char-array message))))))

(get-leet-message "demo" "intermediate")
(get-leet-message "leet" "basic")
(get-leet-message "lamer" "basic")
(get-leet-message "noob" "basic")
(get-leet-message "hacker" "advanced")
(get-leet-message "fear" "intermediate")
