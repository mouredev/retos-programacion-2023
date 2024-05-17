function randomNumber() {
    const date = new Date()
    const ms = date.getTime().toString()
    return Math.round(ms.slice(ms.length - 3) / 10)
}

console.log(randomNumber())
