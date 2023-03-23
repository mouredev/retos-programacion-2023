WITH RECURSIVE fizzbuzz(x) AS(
    SELECT 1
    UNION ALL
    SELECT x + 1
    FROM fizzbuzz
    LIMIT 100
)
SELECT x,
    CASE
        WHEN x % 3 = 0 AND x % 5 = 0 THEN "fizzbuzz"
        WHEN x % 3 = 0 THEN "fizz"
        WHEN x % 5 = 0 THEN "buzz"
        ELSE x
    END AS RESULT
FROM fizzbuzz;
