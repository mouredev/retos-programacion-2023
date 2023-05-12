<?php
class TextAnalyzer
{
    private int $totalWords = 0;
    private int $totalWordsLength = 0;
    private int $totalSentences = 0;
    private string $longestWord = '';

    public function analyze(string $text): array
    {
        $totalLength = mb_strlen($text);
        $currentWord = '';
        $i = 0;

        while ($i < $totalLength) {
            $char = mb_substr($text, $i, 1);
            $i++;
            if ($this->isChar($char)) {
                $currentWord .= $char;
                continue;
            }

            if ('' !== $currentWord) {
                $this->increaseTotalWordsAndTotalWordsLength($currentWord);
                $this->saveAsLongestWordIfProceeds($currentWord);
                if ('.' === $char) {
                    $this->totalSentences++;
                }
            }

            $currentWord = '';
        }

        return [
                'totalWords' => $this->totalWords,
                'averageWordLength' => $this->calculateAverageWordLength(),
                'totalSentences' => $this->totalSentences,
                'longestWord' => $this->longestWord,
        ];
    }

    private function isChar($char): bool
    {
        return preg_match('/^[\p{L}\p{Mn}\p{Mc}ñÑçÇ\'\-]$/u', $char);
    }

    private function increaseTotalWordsAndTotalWordsLength(string $currentWord): void
    {
        $this->totalWords++;
        $this->totalWordsLength += mb_strlen($currentWord);
    }

    private function saveAsLongestWordIfProceeds(string $currentWord): void
    {
        if (mb_strlen($currentWord) > mb_strlen($this->longestWord)) {
            $this->longestWord = $currentWord;
        }
    }

    private function calculateAverageWordLength(): float
    {
        return ($this->totalWords > 0)
            ? $this->totalWordsLength / $this->totalWords
            : 0;
    }
}

$text = "Crea un programa que analice texto y obtenga: Número total de palabras. Longitud media de las palabras. Número de oraciones del texto (cada vez que aparecen un punto). Encuentre la palabra más larga. Todo esto utilizando un único bucle.";
$analyzer = new TextAnalyzer();
$result = $analyzer->analyze($text);

printf('Total words: %d' . PHP_EOL, $result['totalWords']);
printf('Average word length: %f' . PHP_EOL, $result['averageWordLength']);
printf('Total sentences: %d' . PHP_EOL, $result['totalSentences']);
printf('Longest word: %s' . PHP_EOL, $result['longestWord']);