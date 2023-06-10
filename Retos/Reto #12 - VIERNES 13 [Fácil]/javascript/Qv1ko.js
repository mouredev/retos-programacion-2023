isFridayThirteenth(3,2023)

function isFridayThirteenth(month, year) {
    return new Date(year, month - 1, 13).getDay() === 5;
}
