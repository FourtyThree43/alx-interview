(** [min_operations n] returns the fewest number of operations needed to obtain
    exactly `n` 'H' characters using a while loop.

    The function iteratively calculates the minimum operations required to
    obtain `n` 'H' characters by finding divisors of `n` and incrementally
    updating the operations and `n` in a while loop.

    - [n] - The target number of 'H' characters.
    - Returns the fewest number of operations needed to reach `n`.
*)
let rec min_operations n =
  if n <= 1 then 0
  else
    let rec find_divisor d =
      if n mod d = 0 then min_operations (n / d) + d else find_divisor (d + 1)
    in
    find_divisor 2

(** Main function *)
let main () =
  let n = 9 in
  let result = min_operations n in
  Printf.printf "Minimum # operations to get %d 'H' characters: %d\n" n result

let () = main ()
