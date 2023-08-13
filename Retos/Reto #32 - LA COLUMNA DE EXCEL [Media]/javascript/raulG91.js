function column_number(column) {

    let value = 0;
    column = column.toLowerCase()
    let alphabet = "abcdefghijklmnopqrstuvwxyz"

    if (column.length == 1) {

        value = alphabet.indexOf(column) + 1;
    }

    else {

        value = 26;
        for (let i = 0; i < column.length; i++) {

            if (i == column.length - 1) {
                value = value + alphabet.indexOf(column[i]) + 1;
            }
            else {
                value = value + 26 * alphabet.indexOf(column[i]);
            }
        }
    }

    return value;
}
console.log(column_number("Z"));
console.log(column_number("AA"));
console.log(column_number("CA"));
console.log(column_number("HA"));