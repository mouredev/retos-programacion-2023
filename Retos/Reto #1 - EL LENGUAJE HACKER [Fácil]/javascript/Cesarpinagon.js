//creacion de lenguaje hacker
function hackerLanguage(str) {
    var str = str.toUpperCase();
    str = str.replace(/A/g, "4");
    str = str.replace(/E/g, "3");
    str = str.replace(/I/g, "1");
    str = str.replace(/O/g, "0");
    str = str.replace(/S/g, "5");
    return str;
}