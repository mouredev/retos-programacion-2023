$LeetMap = @{[char]'a' = '4';[char]'b' = '|3';[char]'c' = '[';[char]'d' = ')';[char]'e' = '3';[char]'f' = '|=';[char]'g' = '&';[char]'h' = '#';[char]'i' = '1';[char]'j' = ',_|';[char]'k' = '>|';[char]'l' = '1';[char]'m' = '/\/\\';[char]'n' = '^/';[char]'o' = '0';[char]'p' = '|*';[char]'q' = '(_,)';[char]'r' = '|2';[char]'s' = '5';[char]'t' = '7';[char]'u' = '(_)';[char]'v' = '\/';[char]'w' = '\/\/';[char]'x' = '><';[char]'y' = 'j';[char]'z' = '2';[char]'1' = 'L';[char]'2' = 'R';[char]'3' = 'E';[char]'4' = 'A';[char]'5' = 'S';[char]'6' = 'b';[char]'7' = 'T';[char]'8' = 'B';[char]'9' = 'g';[char]'0' = 'o'}

$InputString =  Read-Host -Prompt 'Input string to be translated'
$TranslatedString = ''

$InputString.ToCharArray() | ForEach-Object { $TranslatedString += if ($LeetMap.ContainsKey($_)) {$LeetMap[$_]} else {$_} }
Write-Host "`nTranslation: $TranslatedString"
