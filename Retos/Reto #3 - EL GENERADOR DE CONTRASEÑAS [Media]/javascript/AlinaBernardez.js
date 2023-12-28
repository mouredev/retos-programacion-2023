// program to generate random Password

const characters ='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!"·$%&/()=?';

function generateString(length) {
    let randomPassword = ' ';
    const passLength = characters.length;
    for ( let i = 0; i < length; i++ ) {
        randomPassword += characters.charAt(Math.floor(Math.random() *  passLength));
    }
    return randomPassword;
}

function getPassLength() {
    let randomLength;
    do {
        randomLength = Math.round(Math.random() * 10);
    }
    while (randomLength < 8 && randomLength <= 16);

    return randomLength;
}

generateString(getPassLength());
