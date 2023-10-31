(******************************************************************************)
(*                                                                            *)
(*   Want to run this challenge?                                              *)
(*   ---------------------------                                              *)
(*   1. Download the Ocaml tooling from https://ocaml.org/install.            *)
(*   2. Run either of these commands on the directory where this file is:     *)
(*     [ocaml luishendrix92.ml] or                                            *)
(*     [utop] and inside input [#use "luishendrix92.ml";;], then hit ENTER.   *)
(*   3. Alternatively you can check an online playground:                     *)
(*     https://replit.com/@luishendrix92/Reto43MoureDev#bin/main.ml           *)
(*                                                                            *)
(*   IMPORTANT: The minimum required version of Ocaml for this                *)
(*   challenge is 4.14.0 due to [Seq.iterate] being relatively new.           *)
(*   The profile I use for [.ocamlformat] is [janestreet].                    *)
(*                                                                            *)
(******************************************************************************)

let _ = Random.self_init ()

(** Prevents [n] from going < 0 or > 100, keeping it a valid percentage. *)
let percentage n = Int.max 0 (Int.min n 100)

(** Makes an infinite sequence representing a weather report, consists
    of daily predictions based on the previous values. *)
let weather_report initial_temp initial_rain_prob =
  let predict (temp, rain_prob) =
    let temp_change =
      (* Decide a 50/50 between -2 and +2 if and after a 10% chance *)
      (if Random.int 100 < 10 then 2 * if Random.bool () then 1 else -1 else 0)
      (* ... and then only reduce temperature by 1 if it rained the previous day. *)
      - Bool.to_int (rain_prob >= 100)
    in
    let rain_prob_change = if temp > 25 then 20 else if temp < 5 then -20 else 0 in
    temp + temp_change, percentage (rain_prob + rain_prob_change)
  in
  (initial_temp, percentage initial_rain_prob) |> Seq.iterate predict
;;

let initial_temp, initial_rain_prob, n_days =
  ( (print_string "Enter initial temperature: ";
     read_int ())
  , (print_string "Enter initial rain probability: ";
     read_int ())
  , (print_string "How many days?: ";
     read_int ()) )
in
let min_temp, max_temp, rainy_days =
  weather_report initial_temp initial_rain_prob
  |> Seq.take (max 1 n_days) (* Ensure there's at least 1 day to display. *)
  |> Seq.fold_lefti (* Compute the extreme temperatures and num. of rainy days. *)
       (fun (min_temp, max_temp, rainy_days) i (temp, prob) ->
         Printf.sprintf "Day %d | Temperature: %d°C | Rain odds: %d%%" i temp prob
         |> print_endline;
         min min_temp temp, max max_temp temp, rainy_days + Bool.to_int (prob >= 100))
       (max_int, min_int, 0)
in
print_endline "---------------------------------------------------";
Printf.sprintf
  "Min Temp: %d°C | Max Temp: %d°C | Rainy Days: %d."
  min_temp
  max_temp
  rainy_days
|> print_endline
