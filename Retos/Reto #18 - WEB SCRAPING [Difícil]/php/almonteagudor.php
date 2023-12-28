<?php

$url = "https://holamundo.day/";
$text = "Agenda 8 de mayo";

$document = new DOMDocument();

$document->loadHTMLFile($url);

$elements = $document->getElementsByTagName("h1");

$element = searchElementByString($elements, $text);

if($element) {
    echo $element->textContent . "\n";

    while($element->nextElementSibling?->tagName === 'blockquote') {
        $element = $element->nextElementSibling;

        echo $element->textContent . "\n";
    }
} else {
    echo "No se ha encontrado: $text\n";
}

function searchElementByString(DOMNodeList $list, string $text): ?DOMElement
{
    foreach ($list as $element) {
        if(str_contains($element->textContent, $text)) {
            return $element;
        }
    }

    return null;
}
