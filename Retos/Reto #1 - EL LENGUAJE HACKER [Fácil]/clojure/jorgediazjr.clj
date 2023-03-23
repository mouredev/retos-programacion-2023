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
  (let [msg-chars (-> message char-array seq)
        leet-mappings (leet-maps leet-type)
        replace-char #(leet-mappings (str/lower-case %) %)
        leet-msg (->> msg-chars (map replace-char) (str/join ""))]
    (println leet-msg)))

(get-leet-message "demo" "intermediate")  ; |)3/\/\0
(get-leet-message "leet" "basic")         ; l33t
(get-leet-message "lamer" "basic")        ; l4m3r
(get-leet-message "noob" "basic")         ; n00b
(get-leet-message "hacker" "advanced")    ; ]-[/\{|(ë12
(get-leet-message "fear" "intermediate")  ; ph34I2
(get-leet-message "fun" "intermediate")   ; ph(_)|\|
