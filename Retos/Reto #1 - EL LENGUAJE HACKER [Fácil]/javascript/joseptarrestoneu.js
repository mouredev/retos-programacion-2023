function leetLanguage(data) {
    const diccionario = [
        {
            letra: 'A',
            subs: '4'

        },
        {
            letra: 'B',
            subs: 'I3'

        },
        {
            letra: 'C',
            subs: '['

        },
        {
            letra: 'D',
            subs: ')'

        },
        {
            letra: 'E',
            subs: '3'

        },
        {
            letra: 'F',
            subs: '|='

        },
        {
            letra: 'G',
            subs: '6'

        },
        {
            letra: 'H',
            subs: '#'

        },
        {
            letra: 'I',
            subs: '1'

        },
        {
            letra: 'J',
            subs: ',_|'

        }, {
            letra: 'K',
            subs: '>|'

        }, {
            letra: 'L',
            subs: '1'

        }, {
            letra: 'M',
            subs: '/\\/\\'

        }, {
            letra: 'N',
            subs: '^/'

        },
        {
            letra: 'O',
            subs: '0'

        },
        {
            letra: 'P',
            subs: '|*'

        },
        {
            letra: 'Q',
            subs: '(_,)'

        },
        {
            letra: 'R',
            subs: 'I2'

        },
        {
            letra: 'S',
            subs: '5'

        },
        {
            letra: 'T',
            subs: '7'

        },
        {
            letra: 'U',
            subs: '(_)'

        },
        {
            letra: 'V',
            subs: '\\/'

        },
        {
            letra: 'W',
            subs: '\\/\\/'

        },
        {
            letra: 'X',
            subs: '><'

        },
        {
            letra: 'Y',
            subs: 'j'

        },
        {
            letra: 'Z',
            subs: '2'

        },
        {
            letra: ' ',
            subs: ' '
        }
    ]

    let word = data.toUpperCase().split('')
    let newWord = ''

    newWord = word.map(element => {
        diccionario.map(elements => {
            if (elements.letra === element) {
                newWord = newWord + elements.subs
            }
            return newWord
        })
        return newWord
    })

    console.log(newWord[newWord.length - 1])
}

leetLanguage('mouredev')