const find_sums = (numeros, objetivo) => {

    const find_sum = (start, objetivo, combination) => {

        if (objetivo == 0) {
            result.push([...combination])
            return
        }

        if (objetivo < 0 || start == numeros.length) {
            return
        }

        for (let key = start; key < numeros.length; key++) {

            if (numeros[key] == numeros[key - 1]) {
                continue
            }

            combination.push(numeros[key])
            find_sum(key + 1, objetivo - numeros[key], combination)
            combination.pop()
        }
    }

    numeros.sort((a, b) => a - b)
    result = []
    find_sum(0, objetivo, [])
    console.log(result)
}
find_sums([2,1,5,3,4], 3)