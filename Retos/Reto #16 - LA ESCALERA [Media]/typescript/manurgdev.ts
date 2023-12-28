const createStairs = (n: number): string => {
    if (n === 0) return '__';

    let stairs = '';
    const isAscending = n > 0;
    const steps = Math.abs(n);
    let spaces = '  '.repeat(steps);

    stairs = isAscending ? `${spaces}_\n` : '_\n';
    spaces = isAscending ? spaces.slice(0, -2) : ' ';

    [...Array(steps)].forEach(() => {
        stairs += isAscending ? `${spaces}_|\n` : `${spaces}|_\n`;
        spaces = isAscending ? spaces.slice(0, -2) : `${spaces}  `;
    });

    return stairs;
}

console.log(createStairs(6));
console.log(createStairs(0));
console.log(createStairs(-10));
