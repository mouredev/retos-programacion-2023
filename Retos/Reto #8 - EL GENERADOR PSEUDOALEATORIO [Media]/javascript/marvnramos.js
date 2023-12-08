/**
 * Generates a random number between min and max (inclusive).
 * @param {number} min - The minimum number in the range.
 * @param {number} max - The maximum number in the range.
 * @returns {number} - A random number between min and max.
 */
const getRandomNumber = (min, max) =>{
    
    // Get the last 3 digits of the current timestamp
    const lastThreeDigits = Date.now().toString().slice(-3);

    // Convert the last three digits to a number and divide by 10, rounding it
    let randomNumber = Math.round(Number(lastThreeDigits) / 10);


    // Ensure the random number is within the specified range
    if (randomNumber < min) {
        randomNumber = min;
    } else if (randomNumber > max) {
        randomNumber = max;
    }

    return randomNumber;
}

console.log(getRandomNumber(0, 100));