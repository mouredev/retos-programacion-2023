const hackerLanguage = (payload) => {
  const letterLibrary = {
    a: '@',
    b: ')3',
    c: '©',
    d: 'T)',
    e: '&',
    f: 'ph',
    g: 'gee',
    h: '#',
    i: '1',
    j: ']',
    k: '>|',
    l: '7',
    m: '^^',
    n: '||',
    o: '0',
    p: '9',
    q: '0_',
    r: 'I2',
    s: '5',
    t: '+',
    u: '(_)',
    v: '|/',
    w: 'N',
    x: 'Ж',
    y: 'Ч',
    z: '7_',
    0: '()',
    1: 'L',
    2: 'R',
    3: 'E',
    4: 'A',
    5: 's',
    6: 'b',
    7: 'T',
    8: 'B',
    9: 'g',
  };

  let wordGenerate = '';

  for (const key of payload.toLowerCase()) {
    wordGenerate += key in letterLibrary ? letterLibrary[key] : key;
  }
  return `The word hacker is: ${wordGenerate}`;
};

console.log(hackerLanguage('Hello Peruvian'));
