

function leetChange(text) {

        const leet = {"A": "4", "B": "I3", "C": "[", "D": "|)", "E": "3", "F": "ph", "G": "6", "H": "#", "I": "1", "J": "]", "K": "|<", "L": "1", "M": "/\\/\\", "N": "|\\|", "O": "0", "P": "|>", "Q": "0_", "R": "I2", "S": "5", "T": "7", "U": "(_)", "V": "\\/", "W": "\\/\\/", "X": "><", "Y": "j", "Z": "2", "1": "L", "2": "R", "3": "E", "4": "A", "5": "S", "6": "b", "7": "T", "8": "B", "9": "g", "0": "o"}
        
        return text.split('').map(e => leet[e.toUpperCase()]||e).join('');  
}

console.log(leetChange('nb beats superman'));







