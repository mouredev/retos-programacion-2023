const RGBToHEX = (r, g, b) => {
    return "#" + componentToHex(r) + componentToHex(g) + componentToHex(b)
}

const componentToHex = (component) => {
    let hexa = component.toString(16)

    return hexa.lenght == 1 ? "0" + hexa : hexa
}

const hexToRgb = (hexa) => {
    let result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hexa)

    return result ? {
        r: parseInt(result[1], 16),
        g: parseInt(result[2], 16),
        b: parseInt(result[3], 16)
    } : null
}

console.log(RGBToHEX(153, 18, 66)) // '#991242'
console.log(hexToRgb("#0033ff")) // { r: 0, g: 51, b: 255 }

