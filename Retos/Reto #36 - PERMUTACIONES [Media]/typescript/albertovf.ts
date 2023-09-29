const reto = (input: string):string[] => {
    const result: string[] = [];

    function permute(str: string, prefix: string = "") {
        const len = str.length;
        if (len === 0) {
            result.push(prefix);
        } else {
            for (let i = 0; i < len; i++) {
                const rest = str.slice(0, i) + str.slice(i + 1);
                permute(rest, prefix + str[i]);
            }
        }
    }

    permute(input);
    console.log(result);

    return result;

}

reto('casa')