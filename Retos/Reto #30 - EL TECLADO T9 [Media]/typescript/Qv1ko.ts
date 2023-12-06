t9Translator("66-666-55-444-2")

function t9Translator(str: string) {

    let result: string = ""
    let keyboard = {"2":"A", "3":"D", "4":"G", "5":"J", "6":"M", "7":"P", "8":"T", "9":"W", "0":" ", "22":"B", "33":"E", "44":"H", "55":"K", "66":"N", "77":"Q", "88":"U", "99":"X", "222":"C", "333":"F", "444":"I", "555":"L", "666":"O", "777":"R", "888":"V", "999":"Y", "7777":"S", "9999":"Z"}

    str.split("-").forEach(number => {
        result += keyboard[number.toString()]
    })

    console.log(result)

}
