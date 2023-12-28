const getViernes13 = (date) => {
    const fecha = new Date(date)
    
    const dayNum = fecha.getDay()
    const dayOfMonth = fecha.getDate()

    if (dayOfMonth === 13 && dayNum === 5) return true
    else return false
}

getViernes13('1916/12/13') // false
getViernes13('2023/10/13') // true
getViernes13('2024/09/13') // true