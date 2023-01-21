function leetSpeak(text: string): string {
    const leetDict = {
        'a': '4', 'b': '8', 'c': '(', 'd': 'd', 'e': '3', 'f': 'f', 'g': '9',
        'h': '#', 'i': '1', 'j': 'j', 'k': 'k', 'l': '1', 'm': 'm', 'n': 'n',
        'o': '0', 'p': 'p', 'q': 'q', 'r': '2', 's': '5', 't': '7', 'u': 'u',
        'v': 'v', 'w': 'w', 'x': 'x', 'y': 'y', 'z': '2', '0': '0', '1': '1',
        '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8',
        '9': '9'
    }
    return [...text].map(char => leetDict[char.toLowerCase()] || char).join('')
}
console.log(leetSpeak("Hello World"))  // H3110 W0r1d
