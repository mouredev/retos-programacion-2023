
def steps(num):
    result = ""

    if num==0:
        result = '__'
    else:
        level = num
        if (num > 0):
            result = ("  " * (num+1)) + "_\n"
            while level>0:
                result = result + ("  " * level) + "_|\n"
                level-=1
        else:
            result = "_\n";
            while level<0:
                result = result + " " + ("  " * (level-num)) + "|_\n"
                level+=1

    return result


answer = 's'

while answer == 's':
    stepnum = input('Pon número de escalones: ')
    print(steps(int(stepnum)) + "\n\n")
    answer = input("¿Otra ronda (s/n) ")
