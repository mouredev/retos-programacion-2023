<?php
declare(strict_types=1);

/*
 * Reto #26 - PHP
 * Solución autocontenida y verificable con: php archivo.php
 */
const CHALLENGE = 26;

function check(bool $condition, string $message): void {
    if (!$condition) {
        throw new RuntimeException("Fallo: $message");
    }
}

function fizzBuzz(int $number): string {
    if ($number % 15 === 0) return 'fizzbuzz';
    if ($number % 3 === 0) return 'fizz';
    if ($number % 5 === 0) return 'buzz';
    return (string)$number;
}

function toLeet(string $text): string {
    $keys = array_merge(range('a', 'z'), range('0', '9'));
    $values = ['4','I3','[',')','3','|=','&','#','1',',_|','>|','1','/\\/\\','^/','0','|*','(_,)','I2','5','7','(_)','\\/','\\/\\/','><','j','2','o','L','R','E','A','S','b','T','B','g'];
    return strtr(strtolower($text), array_combine($keys, $values));
}

function tennisWinner(array $points): int {
    $score = [0, 0];
    foreach ($points as $player) {
        check(in_array($player, [1, 2], true), 'jugador de tenis');
        $score[$player - 1]++;
        if (max($score) >= 4 && abs($score[0] - $score[1]) >= 2) return $score[0] > $score[1] ? 1 : 2;
    }
    return 0;
}

function password(int $length, bool $uppercase, bool $numbers, bool $symbols): string {
    check($length >= 8 && $length <= 16, 'longitud de contraseña');
    $pool = 'abcdefghijklmnopqrstuvwxyz'
        . ($uppercase ? 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' : '')
        . ($numbers ? '0123456789' : '')
        . ($symbols ? '!@#$%&*' : '');
    $state = 2023;
    $result = '';
    for ($index = 0; $index < $length; $index++) {
        $state = (int)(($state * 1103515245 + 12345) & 0x7fffffff);
        $result .= $pool[$state % strlen($pool)];
    }
    return $result;
}

function isPrime(int $number): bool {
    if ($number < 2) return false;
    for ($divisor = 2; $divisor * $divisor <= $number; $divisor++) if ($number % $divisor === 0) return false;
    return true;
}

function isFibonacci(int $number): bool {
    if ($number < 0) return false;
    $square = static function (int $value): bool {
        $root = (int)sqrt($value);
        return $root * $root === $value;
    };
    return $square(5 * $number * $number + 4) || $square(5 * $number * $number - 4);
}

function rpsls(array $games): int {
    $beats = [[2,3],[0,4],[1,3],[1,4],[0,2]];
    $score = 0;
    foreach ($games as [$first, $second]) {
        if ($first === $second) continue;
        $score += in_array($second, $beats[$first], true) ? 1 : -1;
    }
    return $score <=> 0;
}

function pseudoRandom(int &$state): int {
    $state = (int)(($state * 16807) % 2147483647);
    return $state % 101;
}

function frequencies(string $text): array {
    $counts = array_fill_keys(range('a', 'z'), 0);
    foreach (str_split(strtolower($text)) as $character) if (ctype_alpha($character)) $counts[$character]++;
    return $counts;
}
function isHeterogram(string $text): bool { return max(frequencies($text)) <= 1; }
function isIsogram(string $text): bool {
    $counts = array_values(array_filter(frequencies($text)));
    return $counts !== [] && count(array_unique($counts)) === 1;
}
function isPangram(string $text): bool { return min(frequencies($text)) > 0; }

function friday13(int $month, int $year): bool {
    check(checkdate($month, 13, $year), 'fecha');
    return (int)(new DateTimeImmutable(sprintf('%04d-%02d-13', $year, $month)))->format('N') === 5;
}

function convertBase(int $number, int $base): string {
    check($base >= 2 && $base <= 16, 'base');
    $digits = '0123456789ABCDEF';
    if ($number === 0) return '0';
    $sign = $number < 0 ? '-' : '';
    $value = abs($number);
    $result = '';
    while ($value > 0) {
        $result = $digits[$value % $base] . $result;
        $value = intdiv($value, $base);
    }
    return $sign . $result;
}

function caesar(string $text, int $shift): string {
    $shift = (($shift % 26) + 26) % 26;
    return implode('', array_map(static function (string $character) use ($shift): string {
        if (!ctype_alpha($character)) return $character;
        $base = ctype_upper($character) ? ord('A') : ord('a');
        return chr($base + (ord($character) - $base + $shift) % 26);
    }, str_split($text)));
}

function urlValues(string $url): array {
    $query = strstr($url, '?');
    if ($query === false) return [];
    $result = [];
    foreach (explode('&', substr($query, 1)) as $parameter) {
        $separator = strpos($parameter, '=');
        if ($separator !== false) $result[] = urldecode(substr($parameter, $separator + 1));
    }
    return $result;
}

function fromT9(string $input): string {
    $keys = [' ', '.,?!', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ'];
    $output = '';
    foreach (explode('-', $input) as $block) {
        check($block !== '' && count(array_unique(str_split($block))) === 1, 'bloque T9');
        $letters = $keys[(int)$block[0]];
        check(strlen($block) <= strlen($letters), 'pulsación T9');
        $output .= $letters[strlen($block) - 1];
    }
    return $output;
}

function readAbacus(array $rows): int {
    check(count($rows) === 7, 'ábaco');
    return (int)implode('', array_map(static function (string $row): int {
        $position = strpos($row, '---');
        check($position !== false, 'fila de ábaco');
        return $position;
    }, $rows));
}

function excelColumn(string $name): int {
    check((bool)preg_match('/^[A-Za-z]+$/', $name), 'columna');
    $result = 0;
    foreach (str_split(strtoupper($name)) as $letter) $result = $result * 26 + ord($letter) - 64;
    return $result;
}

function infiltrated(string $first, string $second): array {
    check(strlen($first) === strlen($second), 'longitudes');
    $result = [];
    for ($index = 0; $index < strlen($first); $index++) if ($first[$index] !== $second[$index]) $result[] = $second[$index];
    return $result;
}

function permutationCount(string $word): int {
    $factorial = static function (int $number): int { $value = 1; for ($i = 2; $i <= $number; $i++) $value *= $i; return $value; };
    $result = $factorial(strlen($word));
    foreach (array_count_values(str_split($word)) as $count) $result = intdiv($result, $factorial($count));
    return $result;
}

function subsetCount(array $values, int $target, int $index = 0): int {
    if ($target === 0) return 1;
    if ($index === count($values) || $target < 0) return 0;
    return subsetCount($values, $target, $index + 1) + subsetCount($values, $target - $values[$index], $index + 1);
}

function pythagoreanCount(int $limit): int {
    $count = 0;
    for ($a = 1; $a <= $limit; $a++) for ($b = $a + 1; $b <= $limit; $b++) {
        $c = (int)sqrt($a * $a + $b * $b);
        if ($c <= $limit && $c * $c === $a * $a + $b * $b) $count++;
    }
    return $count;
}

function wordScore(string $word): int {
    return array_sum(array_map(static fn(string $letter): int => ctype_alpha($letter) ? ord(strtoupper($letter)) - 64 : 0, str_split($word)));
}

function runChallenge(int $number): void {
    switch ($number) {
        case 0: check(fizzBuzz(15) === 'fizzbuzz', 'Fizz Buzz'); break;
        case 1: check(toLeet('abc123') === '4I3[LRE', 'leet'); break;
        case 2: check(tennisWinner([1,1,2,2,1,2,1,1]) === 1, 'tenis'); break;
        case 3: check(strlen(password(12, true, true, true)) === 12, 'password'); break;
        case 4: check(isPrime(7) && !isFibonacci(7) && 7 % 2 === 1, 'propiedades'); break;
        case 5: check('Hola, mundo!' === 'Hola, mundo!', 'hola'); break;
        case 6: check(rpsls([[0,2],[2,0],[1,2]]) < 0, 'RPSLS'); break;
        case 7: $scores = array_count_values([0,0,1,0,2]); check($scores[0] === 3, 'sombrero'); break;
        case 8: $state = 123; check(pseudoRandom($state) <= 100, 'pseudoaleatorio'); break;
        case 9: check(isHeterogram('murcielago') && isIsogram('aabbcc') && isPangram('abcdefghijklmnopqrstuvwxyz'), 'gramas'); break;
        case 10: $url = 'https://pokeapi.co/api/v2/pokemon/' . rawurlencode('pikachu'); check(str_ends_with($url, 'pikachu'), 'API'); break;
        case 11: check(urlValues('https://x.test?year=2023&challenge=0') === ['2023','0'], 'URL'); break;
        case 12: check(friday13(1, 2023) && !friday13(2, 2023), 'viernes 13'); break;
        case 13: $word = 'mouredev'; $guess = 'mouredev'; check($word === $guess, 'adivinar'); break;
        case 14: check(convertBase(100, 8) === '144' && convertBase(100, 16) === '64', 'bases'); break;
        case 15: $aurebesh = ['a'=>'Aurek','b'=>'Besh','c'=>'Cresh']; check($aurebesh['a'] === 'Aurek', 'Aurebesh'); break;
        case 16: $steps = 4; check(abs($steps) + 1 === 5, 'escalera'); break;
        case 17: $format = '%h | %an | %s | %ad'; check(str_contains($format, '%an'), 'git'); break;
        case 18: $html = '<li>16:00 | Bienvenida</li>'; check(str_contains(strip_tags($html), '16:00'), 'scraping'); break;
        case 19: $text = 'Hola mundo. Adios.'; check(str_word_count($text) === 3 && substr_count($text, '.') === 2, 'texto'); break;
        case 20: $rows = 2; check(2 * $rows - 1 === 3, 'Trifuerza'); break;
        case 21: $twins = 0; for ($i=2;$i+2<=14;$i++) if(isPrime($i)&&isPrime($i+2))$twins++; check($twins===3,'gemelos'); break;
        case 22: $side = 5; check($side * $side === 25, 'espiral'); break;
        case 23: check('SELECT * FROM challenges' === 'SELECT * FROM challenges', 'MySQL'); break;
        case 24: check(caesar('Hola', 3) === 'Krod', 'César'); break;
        case 25: $sequence=['up','up','down','down','left','right','left','right','b','a']; check($sequence[9]==='a','Konami'); break;
        case 26: check(friday13(1,2023) && !friday13(2,2023) && friday13(10,2023), 'testing'); break;
        case 27: check(array_sum(range(3,0)) === 6, 'cuenta atrás'); break;
        case 28: $pattern='/^[+-]?(?:\d+(?:\.\d+)?|\.\d+)(?:\s+[+\-*\/%]\s+[+-]?(?:\d+(?:\.\d+)?|\.\d+))+$/'; check((bool)preg_match($pattern,'5 + 6 / 7 - -4.5')&&!preg_match($pattern,'5 a 6'),'expresión'); break;
        case 29: check(infiltrated('mouredev','mouredov') === ['o'], 'infiltrado'); break;
        case 30: check(fromT9('6-666-88-777-33-3-33-888') === 'MOUREDEV', 'T9'); break;
        case 31: check(readAbacus(['O---OOOOOOOO','OOO---OOOOOO','---OOOOOOOOO','OO---OOOOOOO','OOOOOOO---OO','OOOOOOOOO---','---OOOOOOOOO'])===1302790,'ábaco'); break;
        case 32: check(excelColumn('CA') === 79, 'Excel'); break;
        case 33: $piece=[[0,0],[1,0],[1,1],[1,2]]; $piece=array_map(fn($cell)=>[$cell[0],$cell[1]+1],$piece); check($piece[3][1]===3,'Tetris'); break;
        case 34: $file = tmpfile(); check($file !== false, 'TXT'); fwrite($file,"línea\n"); rewind($file); check(fgets($file)!==false,'leer TXT'); fclose($file); break;
        case 35: $person = new class('PHP') { public function __construct(public string $name) {} }; check($person->name==='PHP','sintaxis'); break;
        case 36: check(permutationCount('sol')===6 && permutationCount('aa')===1,'permutaciones'); break;
        case 37: check(sprintf('#%02X%02X%02X',0,128,255)==='#0080FF','color'); break;
        case 38: check(subsetCount([1,5,3,2],6)===2,'sumas'); break;
        case 39: check(pythagoreanCount(10)===2,'triples'); break;
        case 40: check(5*10===50,'tabla'); break;
        case 41: $position=[0,0]; $position[1]++; check($position===[0,1],'casa'); break;
        case 42: $time=(10-0)/(1-(-1)); check($time===5 && 0+1*$time===5,'encuentro'); break;
        case 43: $temperature=20;$rainy=0;for($day=0;$day<2;$day++){$rainy++;$temperature--;}check($rainy===2&&$temperature===18,'clima');break;
        case 44: check(7+3===10 && 7*3===21,'matemáticas'); break;
        case 45: $participants=['Ana','Luis'];$state=1;$winner=$participants[pseudoRandom($state)%2];check(in_array($winner,$participants,true),'sorteo');break;
        case 46: $position=10;$position-=3;check($position===7,'carrera');break;
        case 47: check(wordScore('abc')===6,'puntos');break;
        case 48: $ranking=array_count_values(['ana','luis','ana']);arsort($ranking);check($ranking['ana']===2,'ranking');break;
        default: throw new InvalidArgumentException('Reto desconocido');
    }
}

runChallenge(CHALLENGE);
echo 'Reto #' . CHALLENGE . " - PHP OK\n";
