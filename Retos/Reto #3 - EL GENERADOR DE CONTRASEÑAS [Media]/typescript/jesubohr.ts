interface PasswordOptions {
  length: number
  uppercase: boolean
  numbers: boolean
  symbols: boolean
}

const CHARACTERS = {
  lowercase: 'abcdefghijklmnopqrstuvwxyz',
  uppercase: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
  numbers: '0123456789',
  symbols: '&/\\^=?!@#$%*+.,:;|()[]{}<>-_'
}

const getRandomChar = (str: string) =>
  str.charAt(Math.floor(Math.random() * str.length))

type IncludedSet = keyof typeof CHARACTERS
function generatePassword({ length = 8, ...included }: PasswordOptions) {
  if (length < 8 || length > 16) console.error('Length must be between 8 and 16 characters')
  let password = ''

  // Define the allowed characters
  const allowedChars = Object
    .entries(CHARACTERS)
    .filter(([set, _]) => included[set] || set === 'lowercase')
    .map(([_, chars]) => chars)

  // Generate the password
  for (let i = 0; i < length; i++) {
    const setIndex = Math.floor(Math.random() * allowedChars.length)
    const set = allowedChars[setIndex]
    password += getRandomChar(set)
  }

  return password
}

// Test
for (let i = 0; i < 10; i++) {
  const randomLength = Math.floor(Math.random() * 8) + 8
  console.log(
    generatePassword({
      length: randomLength,
      uppercase: true,
      numbers: true,
      symbols: true
    })
  )
}

