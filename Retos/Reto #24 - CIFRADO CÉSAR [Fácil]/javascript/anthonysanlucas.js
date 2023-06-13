const alphabet = 'abcdefghijklmnñopqrstuvwxyz'

const cipher = (message, key) => {
  if (typeof message !== 'string' || !/^[a-zA-Z]+$/.test(message)) {
    throw new Error('El mensaje debe ser una cadena de texto que contenga solo letras.')
  }

  if (typeof key !== 'number' || !Number.isInteger(key)) {
    throw new Error('La llave debe ser un número entero.')
  }

  let messageToEncrypt = ''
  let newArr = message.split('')
  let keyToEncrypt = ((key % 27) + 27) % 27

  newArr.forEach(letter => {
    let capitalize = capitalizationChecker(letter)
    letter = letter.toLowerCase()
    if (alphabet.includes(letter)) {
      let newLetter = alphabet[(alphabet.indexOf(letter) + keyToEncrypt) % 27]
      messageToEncrypt += isCapitalized(capitalize, newLetter)
    } else {
      messageToEncrypt += letter
    }
  })

  return messageToEncrypt
}

const decipher = (message, key) => {
  if (typeof message !== 'string' || !/^[a-zA-Z]+$/.test(message)) {
    throw new Error('El mensaje debe ser una cadena de texto que contenga solo letras.')
  }

  if (typeof key !== 'number' || !Number.isInteger(key)) {
    throw new Error('La llave debe ser un número entero.')
  }

  let messageToDecrypt = ''
  let newArr = message.split('')
  let keyToDecrypt = ((key % 27) - 27) % 27

  newArr.forEach(letter => {
    let capitalize = capitalizationChecker(letter)
    letter = letter.toLowerCase()
    if (alphabet.includes(letter)) {
      let newLetter = alphabet[(alphabet.indexOf(letter) - keyToDecrypt) % 27]
      messageToDecrypt += isCapitalized(capitalize, newLetter)
    } else {
      messageToDecrypt += letter
    }
  })

  return messageToDecrypt
}

function capitalizationChecker(letter) {
  return letter === letter.toUpperCase()
}

function isCapitalized(capitalize, letter) {
  return capitalize ? letter.toUpperCase() : letter
}

let menuOption

do {
  menuOption = prompt('Menú:\n1. Cipher Text\n2. Decipher Text\n3. Quit')

  switch (menuOption) {
    case '1':
      let messageToEncrypt = prompt('Ingresa el mensaje a cifrar')
      let keyToEncrypt = Number(prompt('Ingresa la llave'))

      try {
        alert(cipher(messageToEncrypt, keyToEncrypt))
      } catch (error) {
        alert('Error: ' + error.message)
      }
      break

    case '2':
      let messageToDecrypt = prompt('Ingresa el mensaje a descifrar')
      let keyToDecrypt = Number(prompt('Ingresa la llave'))

      try {
        alert(decipher(messageToDecrypt, keyToDecrypt))
      } catch (error) {
        alert('Error: ' + error.message)
      }
      break

    case '3':
      console.log('Never forget the key...')
      break

    default:
      console.log('Opción inválida. Selecciona una opción del menú.')
      break
  }
} while (menuOption !== '3')
