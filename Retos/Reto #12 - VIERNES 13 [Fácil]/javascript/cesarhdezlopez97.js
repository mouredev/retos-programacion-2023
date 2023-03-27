function comprobarViernes13(mes, anyo) {
    const date = new Date(anyo + '-' + mes + '-' + '13');
    if (date.getDay() == 5) {
        return true
    } else
        return false
}

console.log(comprobarViernes13(1, 2023))
console.log(comprobarViernes13(2, 2023))