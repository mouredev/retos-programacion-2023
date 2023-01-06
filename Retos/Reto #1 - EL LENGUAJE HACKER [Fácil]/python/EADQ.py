
dato_ingresado = input('Ingrese Dato a convertir: ')

hacker_replace = (
    ('A' , '^'),
    ('B' , '!3'),
    ('C' , '['),
    ('D' , '!)'),
    ('E' , '&'),
    ('F' , '!='),
    ('G' , '(_+'),
    ('H' , '#'),
    ('I' , 'eye'),
    ('J' , ',_!'),
    ('K' , '>!'),
    ('L' , '!_'),
    ('M' , '^^'),
    ('N' , '^/'),
    ('O' , '<>'),
    ('P' , '!*'),
    ('Q' , '(_,)'),
    ('R' , '!?'),
    ('S' , 'ehs'),
    ('T' , '"]["'),
    ('U' , '(_)'),
    ('V' , '\/'),
    ('W' , 'NN'),
    ('X' , '>!<'),
    ('Y' , ';!'),
    ('Z' , '%'),
    ('a' , '(L'),
    ('b' , ')3'),
    ('c' , '{'),
    ('d' , 'T)'),
    ('e' , '[-'),
    ('f' , '/='),
    ('g' , '(?'),
    ('h' , '1-1'),
    ('i' , '3y3'),
    ('j' , '._]'),
    ('k' , '!{'),
    ('l' , '1'),
    ('m' , '<\/>'),
    ('n' , '{\}'),
    ('o' , 'oh'),
    ('p' , '!7'),
    ('q' , '<!'),
    ('r' , '!z'),
    ('s' , '2'),
    ('t' , '-!-'),
    ('u' , '{_-_}'),
    ('v' , '\__/'),
    ('w' , '\X/'),
    ('x' , '?'),
    ('y' , '7'),
    ('z' , '7_')

)

hacker_convert = dato_ingresado
for old, new in hacker_replace:
    hacker_convert = hacker_convert.replace(old, new)

print('El dato encriptado es: ' + hacker_convert)




















