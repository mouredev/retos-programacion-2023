var n = 0;
for (var i = 1; i < 101; i++) {
    n += i;
    if (i % 5 == 0 && i % 3 == 0)
        console.log('fizzbuzz')
    else if (i % 3 == 0)
        console.log('fizz');
    else if (i % 5 == 0)
        console.log('buzz')
    else
        console.log(i);
}