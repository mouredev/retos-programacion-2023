'use strict';

const AUREBESH = {
  a: 'Aurek', b: 'Besh', c: 'Cresh', d: 'Dorn', e: 'Esk', f: 'Forn',
  g: 'Grek', h: 'Herf', i: 'Isk', j: 'Jenth', k: 'Krill', l: 'Leth',
  m: 'Mern', n: 'Nern', o: 'Osk', p: 'Peth', q: 'Qek', r: 'Resh',
  s: 'Senth', t: 'Trill', u: 'Usk', v: 'Vev', w: 'Wesk', x: 'Xesh',
  y: 'Yirt', z: 'Zerek'
};
const SPANISH = Object.fromEntries(Object.entries(AUREBESH).map(([letter, word]) => [word.toLowerCase(), letter]));

function toAurebesh(text) {
  return [...String(text)].map(character => {
    if (/\s/.test(character)) return '/';
    const translated = AUREBESH[character.toLowerCase()];
    if (!translated) return character;
    return character === character.toUpperCase() ? translated.toUpperCase() : translated;
  }).join(' ');
}

function fromAurebesh(text) {
  return String(text).split(/\s+/).map(token => {
    if (token === '/') return ' ';
    const punctuation = token.match(/^([^A-Za-z]*)([A-Za-z]+)([^A-Za-z]*)$/);
    if (!punctuation) return token;
    const translated = SPANISH[punctuation[2].toLowerCase()];
    if (!translated) return token;
    const letter = punctuation[2] === punctuation[2].toUpperCase() ? translated.toUpperCase() : translated;
    return punctuation[1] + letter + punctuation[3];
  }).join('');
}

module.exports = { toAurebesh, fromAurebesh };

if (require.main === module) {
  const translated = toAurebesh(process.argv.slice(2).join(' ') || 'Star Wars');
  console.log(translated);
  console.log(fromAurebesh(translated));
}
