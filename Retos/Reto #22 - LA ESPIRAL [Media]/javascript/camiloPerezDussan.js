let espiral = size => {
    let espiral = '═'.repeat(size - 1) + '╗'
    for (let row = 1; row < size; row++) {
        espiral += row < size / 2 ?
            `\n${'║'.repeat(row - 1)}╔${'═'.repeat(size - (row * 2 + 1))}╗${'║'.repeat(row)}` :
            `\n${'║'.repeat(size - row - 1)}╚${'═'.repeat(row * 2 - size)}╝${'║'.repeat(size - row - 1)}`
    }
    console.log(espiral)
};

espiral(1)
espiral(3)
espiral(5)
espiral(7)
espiral(10)
espiral(20)