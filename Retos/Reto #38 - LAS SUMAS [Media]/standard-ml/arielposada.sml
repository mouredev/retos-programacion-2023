fun findCombinations nums target =
    let
        fun helper (nums, target, path, acc) =
            if target = 0 then
                path :: acc
            else if target < 0 orelse null nums then
                acc
            else
                helper (tl nums, target - hd nums, hd nums :: path, acc) @
                helper (tl nums, target, path, acc)
    in
        helper (nums, target, [], [])
    end

val nums = [1, 5, 3, 2]
val target = 6
val result = findCombinations nums target
