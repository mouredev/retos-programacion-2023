<?php

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

class PPTLS {
    const ROLES = [
        [
            'letter' => 'R', // Rock
            'lose' => ['P', 'S'], // Le gana 'P'apel y Spock
            'name' => 'piedra',
            'index' => 0,
        ],
        [
            'letter' => 'P',
            'lose' => ['T', 'L'], // Le gana 'T'ijeras y Lagarto
            'name' => 'papel',
            'index' => 1,
        ],
        [
            'letter' => 'T',
            'lose' => ['R', 'S'], // Rock y Spock
            'name' => 'tijera',
            'index' => 2,
        ],
        [
            'letter' => 'L',
            'lose' => ['R', 'T'], // Le gana 'R'ock y 'T'ijeras
            'name' => 'lagarto',
            'index' => 3,
        ],
        [
            'letter' => 'S',
            'lose' => ['L', 'P'], // Largarto y papel
            'name' => 'spock',
            'index' => 4,
        ]
    ];

    private $letters=[];
    private $scores =[];
    private $players=2;
    private $rounds=5;

    public function __construct($players=2)
    {
        $this->players = $players;
    }
    
    public function init() {
        
        $scores = [
            'players' => [],
            'rounds'  => [],
        ];
        // Inicializamos marcadores
        for($i=0;$i<$this->players;$i++) {
            $scores['players'][$i] = 0;
        }
        $this->scores = $scores;
        $letters = [];
        foreach(self::ROLES as $role) {
            $letters [] = $role['letter'];
        }
        $this->letters = $letters;
    }

    public function getPlayers(): int
    {
        return $this->players;
    }

    public function setPlayers($players): self
    {
        $this->players = $players;

        return $this;
    }

    public function getRounds(): int
    {
        return $this->rounds;
    }

    public function setRounds($rounds): self
    {
        $this->rounds = $rounds;

        return $this;
    }

    public function checkRound($round): string
    {
        // $roles es un array con los movimientos ($index) de caja jugador
        $pX = self::ROLES[$round[0]];
        $pY = self::ROLES[$round[1]];
        $this->scores['rounds'][] = $round;
        $winner = $loser = null;
        $winnerText = "";
        if ($pX!=$pY) {
            if (array_search($pX['letter'], $pY['lose'])) {
                $winner = $pX;
                $loser = $pY;
                $this->scores['players'][0]++;
                $winnerText = "P1";
            } else {
                $winner = $pY;
                $loser = $pX;
                $this->scores['players'][1]++;
                $winnerText = "P2";
            }
            $resultText = "Ronda ganada por $winnerText";
        } else {
            $resultText = $winnerText = "Ronda con empate";
            $winner = $loser = $pX;
        }
        printf("%s (%s vs %s)\n", $resultText, $winner['name'], $loser['name']);

        return $winnerText;
    }

    public function playGame($playings=null) {
        $this->init();
        if (null==$playings) {
            // Generar jugadas aleatorias
            
        } else {
            // Recoger array con letras
            foreach($playings as $playing) {
                $round = []; // Recogemos el indice de caja jugador
                // Buscamos el jugador 1 y asignamos el índice de la jugada
                foreach (self::ROLES as $role) {
                    if ($role['letter'] == $playing[0]) {
                        $round[0] = $role['index'];
                        break;
                    }
                }
                // Buscamos el jugador 2 y asignamos el índice de la jugada
                foreach (self::ROLES as $role) {
                    if ($role['letter'] == $playing[1]) {
                        $round[1] = $role['index'];
                        break;
                    }
                }
                if (!count($round)) {
                    print "Alguna de las letras no es correcta\n";
                } else {
                    $this->checkRound($round);
                }
            }
        }

        // Recuento
        printf("Resultado final: P1(%d) - P2(%d)\n", $this->scores['players'][0], $this->scores['players'][1]);
        if ($this->scores['players'][0]>$this->scores['players'][1]) {
            $resultText = "Vencedor(a): P1";
        } else {
            $resultText = "Ha habido empate";
            if ($this->scores['players'][1]>$this->scores['players'][0]) {
                $resultText = "Vencedor(a): P2";
            }
        }
        print "$resultText\n";
    }
}

$test = new PPTLS();
$rounds=[
    ['R', 'S'],
    ['R', 'S'],
    ['L', 'P'],
    ['R', 'T'],
    ['P', 'S'],
];
$test->playGame($rounds);
$rounds=[
    ['S', 'S'],
    ['R', 'S'],
    ['L', 'P'],
    ['R', 'T'],
    ['P', 'S'],
];
$test->playGame($rounds);
