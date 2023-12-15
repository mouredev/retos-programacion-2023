var isHeterograma = function (text) {
    var splitText = text.split('');
    var set = new Set();
    for (var i = 0; i < text.length; i++) {
        if (set.has(splitText[i])) {
            return false;
        }
        set.add(splitText[i]);
    }
    return true;
};
var isIsograma = function (text) {
};
var isPangrama = function (text) {
    var setLetters = new Set();
    for (var i = 0; i < text.length; i++) {
        if (text[i] !== ' ' && text[i] !== '?' && text[i] !== '.' && text[i] !== ',' && !setLetters.has(text[i]) && text[i] !== '!') {
            setLetters.add(text[i]);
        }
    }
    return (setLetters.size >= 14);
};
// console.log(isPangrama("Fabio me exige, sin tapujos, que añada cerveza al whisky"))
// console.log(isHeterograma("mango"))
