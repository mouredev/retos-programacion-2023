function find_sums(numbers, target) {
    // Sort numbers and filter in case we have negative numbers
    let sortedAndFilteredNumbers = numbers.sort().filter((number) => {
        return number > 0
    })
    if (sortedAndFilteredNumbers.length === 0) return []

    function find_sum(start, target, combination) {
        // find solution
        if (target === 0) {
            result.push([...combination])
        }

        // backtracking
        for (let i = start; i < sortedAndFilteredNumbers.length; i++) {
            if (i > start && sortedAndFilteredNumbers[i] === sortedAndFilteredNumbers[i - 1]) {
                continue
            }

            combination.push(sortedAndFilteredNumbers[i]);
            find_sum(i + 1, target - sortedAndFilteredNumbers[i], combination);
            combination.pop();
        }
    }

    let result = []
    find_sum(0, target, [])
    return result
}

console.log(find_sums([1, 5, 2, 2, 1, 1], 6))