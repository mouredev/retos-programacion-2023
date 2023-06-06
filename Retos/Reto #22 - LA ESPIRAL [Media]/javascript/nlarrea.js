/*
 * Crea una función que dibuje una espiral como la del ejemplo.
 * - Únicamente se indica de forma dinámica el tamaño del lado.
 * - Símbolos permitidos: ═ ║ ╗ ╔ ╝ ╚
 *
 * Ejemplo espiral de lado 5 (5 filas y 5 columnas):
 * ════╗
 * ╔══╗║
 * ║╔╗║║
 * ║╚═╝║
 * ╚═══╝
 */

const symbols = {
    horizontal: '═',
    vertical: '║',
    cornerUpRight: '╗',
    cornerUpLeft: '╔',
    cornerDownRight: '╝',
    cornerDownLeft: '╚'
};


function drawSpiral(side) {
    if (side < 2) {
        console.log(`Can't draw a ${side}x${side} spiral.`);
    } else {
        const spiral = generateSpiral(side);
    
        let spiralStr = '';
        for (let row of spiral) {
            spiralStr += row.join('');
            spiralStr += '\n';
        }
    
        console.log(`${side}x${side} spiral:\n` + spiralStr);
    }
}


function generateSpiral(side) {
    const halfSpiral = parseInt(side / 2);


    const generateHalfSpiral = (cornerLeft, cornerRight, isDown=false) => {
        let spiral = [];

        for (let row=0; row<halfSpiral; row++) {
            let rowTable = [];
            for (let col=0; col<side; col++) {
                if (row === 0) {
                    if (isDown && col === 0) rowTable.push(cornerLeft);
                    else if (col === side-1) rowTable.push(cornerRight);
                    else rowTable.push(symbols.horizontal);
                } else {
                    if ((spiral[row-1][col] === symbols.horizontal) &&
                        (spiral[row-1][col-1] === cornerLeft ||
                            spiral[row-1][col-1] === undefined)) {
                        rowTable.push(cornerLeft);
                    } else {
                        rowTable.push(symbols.vertical);
                    }
    
                    if (spiral[row-1][col] === cornerRight) {
                        rowTable[col-1] = cornerRight;
                    }
                }
            }
    
            if (rowTable.find(item => item === cornerLeft)) {
                const start = rowTable.findIndex(item => item === cornerLeft) + 1;
                const end = rowTable.findIndex(item => item === cornerRight);
                rowTable.splice(start, end-start, ...symbols.horizontal.repeat(end-start));
            }
    
            spiral.push(rowTable);
        }

        return spiral;
    }


    // generate: upper half spiral

    const spiral = generateHalfSpiral(symbols.cornerUpLeft, symbols.cornerUpRight);

    // generate: middle row (only if side is odd)

    if (side % 2 !== 0) {
        let rowTable = [];

        rowTable.push(...symbols.vertical.repeat(spiral.length-1));
        rowTable.push(symbols.cornerUpLeft);
        rowTable.push(symbols.cornerUpRight);
        rowTable.push(...symbols.vertical.repeat(side-rowTable.length));

        spiral.push(rowTable);
    }

    // generate: down half spiral

    const downSpiral = generateHalfSpiral(symbols.cornerDownLeft, symbols.cornerDownRight, true);
    downSpiral.reverse();

    // completed spiral

    spiral.push(...downSpiral);

    return spiral;
}


drawSpiral(1);
drawSpiral(5);
drawSpiral(10);