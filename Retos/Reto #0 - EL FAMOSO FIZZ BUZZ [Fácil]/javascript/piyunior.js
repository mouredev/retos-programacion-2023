const fizzArray = async () => {
    const size = 100;
    for (let index = 1; index <= size; index++) {
        let three = (index % 3) == 0;
        let buzz = (index % 5) == 0;
        if (three && buzz) {
            console.log('fizzbuzz');
        } else {
            if (three == true) {
                console.log('fizz')
            } else if (buzz == true) {
                console.log('buzz')
            } else {
                console.log(index);
            }
        }
    }
}

fizzArray();