const t9ToText = (keystrokes: string): string => {
  const t9Mappings = {
    '2': 'ABC',
    '3': 'DEF',
    '4': 'GHI',
    '5': 'JKL',
    '6': 'MNO',
    '7': 'PQRS',
    '8': 'TUV',
    '9': 'WXYZ',
  }

  return keystrokes
    .split('-')
    .map(block => t9Mappings[block[0]][block.length - 1])
    .join('')
}
