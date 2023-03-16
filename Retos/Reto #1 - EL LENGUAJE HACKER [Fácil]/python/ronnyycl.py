# Hacker Language

def hacker_language(text):
    hacker_txt = ''
    for character in list(text):
        match character:
            case ' ':
                hacker_txt += ' '
            case 'a' | 'A':
                hacker_txt += '4'
            case 'b' | 'B':
                hacker_txt += 'l3'
            case 'c' | 'C':
                hacker_txt += '['
            case 'd' | 'D':
                hacker_txt += ')'
            case 'e' | 'E':
                hacker_txt += '3'
            case 'f' | 'F':
                hacker_txt += '|='
            case 'g' | 'G':
                hacker_txt += '&'
            case 'h' | 'H':
                hacker_txt += '#'
            case 'i' | 'I':
                hacker_txt += '1'
            case 'j' | 'J':
                hacker_txt += ',_|'
            case 'k' | 'K':
                hacker_txt += '>|'
            case 'l' | 'L':
                hacker_txt += '1'
            case 'm' | 'M':
                hacker_txt += 'JVI'
            case 'n' | 'N':
                hacker_txt += '^/'
            case 'o' | 'O':
                hacker_txt += '0'
            case 'p' | 'P':
                hacker_txt += '|*'
            case 'q' | 'Q':
                hacker_txt += '(_,)'
            case 'r' | 'R':
                hacker_txt += 'l2'
            case 's' | 'S':
                hacker_txt += '5'
            case 't' | 'T':
                hacker_txt += '7'
            case 'u' | 'U':
                hacker_txt += '(_)'
            case 'v' | 'V':
                hacker_txt += '\/'
            case 'w' | 'W':
                hacker_txt += '\/\/'
            case 'x' | 'X':
                hacker_txt += '><'
            case 'y' | 'Y':
                hacker_txt += 'j'
            case 'z' | 'Z':
                hacker_txt += '2'
            case '1':
                hacker_txt += 'L'
            case '2':
                hacker_txt += 'R'
            case '3':
                hacker_txt += 'E'
            case '4':
                hacker_txt += 'A'
            case '5':
                hacker_txt += 'S'
            case '6':
                hacker_txt += 'b'
            case '7':
                hacker_txt += 'T'
            case '8':
                hacker_txt += 'B'
            case '9':
                hacker_txt += 'g'
            case '0':
                hacker_txt += 'o'
            case _:
                hacker_txt += character
    print(hacker_txt)


hacker_language("Hello world!2")
