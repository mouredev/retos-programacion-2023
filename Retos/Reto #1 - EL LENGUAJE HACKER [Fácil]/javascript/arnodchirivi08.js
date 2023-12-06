const letters =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];
const letterLeet=['4','I3','[', ')','3', '|=','&','#','1',',_|','>|','£','JVI', '^/', '0','|*','(_,)','I2','5','7','(_)','\/','VV','><','j','2' ]

const text = 'GitHub';

function converToLeet(text, letters, letterLeet){
    const value = text.toLowerCase().split('');
    let arrayLeets = [];
    value.some((item) => {
        letters.some((itemLetter, indexLetter) => {
            if(itemLetter === item){
                arrayLeets += letterLeet[indexLetter]
            }
        })
    });

    return arrayLeets;
}

console.log(converToLeet(text,letters, letterLeet));