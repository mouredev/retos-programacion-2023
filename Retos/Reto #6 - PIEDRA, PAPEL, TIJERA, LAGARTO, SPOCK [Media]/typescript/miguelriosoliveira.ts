/*
 * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
 *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
 * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
 */

const TYPES = {
  ROCK: '🗿',
  PAPER: '📄',
  SCISSORS: '✂️',
  LIZARD: '🦎',
  SPOCK: '🖖',
} as const;

type Keys = keyof typeof TYPES;
type Type = (typeof TYPES)[keyof typeof TYPES];

const DOMINANCE = {
  [TYPES.ROCK]: [TYPES.SCISSORS, TYPES.LIZARD],
  [TYPES.PAPER]: [TYPES.ROCK, TYPES.SPOCK],
  [TYPES.SCISSORS]: [TYPES.PAPER, TYPES.LIZARD],
  [TYPES.LIZARD]: [TYPES.SPOCK, TYPES.PAPER],
  [TYPES.SPOCK]: [TYPES.SCISSORS, TYPES.ROCK],
};

type Match = [Type, Type];
type Winner = 'Player 1' | 'Player 2' | 'Tie';

function calculateWinner(matches: Match[]): Winner {
  const { p1: p1Count, p2: p2Count } = matches
    .map(([p1, p2]) => {
      if (DOMINANCE[p1].includes(p2 as never)) {
        return 'p1';
      }
      if (DOMINANCE[p2].includes(p1 as never)) {
        return 'p2';
      }
      return 'p0';
    })
    .reduce((acc, winner) => ({ ...acc, [winner]: acc[winner] + 1 }), {
      p0: 0,
      p1: 0,
      p2: 0,
    });

  return p1Count > p2Count ? 'Player 1' : p2Count > p1Count ? 'Player 2' : 'Tie';
}

function test() {
  const testCases: { input: Match[]; expected: Winner }[] = [
    {
      input: [
        ['🗿', '✂️'],
        ['✂️', '🗿'],
        ['📄', '✂️'],
      ],
      expected: 'Player 2',
    },
    {
      input: [
        ['🗿', '✂️'],
        ['✂️', '🗿'],
        ['📄', '✂️'],
        ['🦎', '📄'],
        ['🖖', '🗿'],
      ],
      expected: 'Player 1',
    },
    {
      input: [
        ['✂️', '🗿'],
        ['📄', '✂️'],
        ['🦎', '📄'],
        ['🖖', '🗿'],
      ],
      expected: 'Tie',
    },
  ];
  testCases.every(({ input, expected }) => {
    const received = calculateWinner(input);
    const hasPassed = received === expected;
    if (received === expected) {
      console.log('✅ PASSED');
    } else {
      console.log('❌ FAILED', { expected, received });
    }
    return hasPassed;
  });
}

test();
