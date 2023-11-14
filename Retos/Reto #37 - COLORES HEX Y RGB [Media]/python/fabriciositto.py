import re

hex_format=r'#[a-fA-F0-9]{6}'
rgb_format=r'r: (25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]|[0-9]), g: (25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]|[0-9]), b: (25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]|[0-9])'

def dec_to_hex(num):
    num1=str(int(num)//16)
    num2=str(int(num)%16)
    
    equiv={
        '10':'a',
        '11':'b',
        '12':'c',
        '13':'d',
        '14':'e',
        '15':'f'
    }
    
    if num1 in equiv:
        num1=equiv[num1]
    
    if num2 in equiv:
        num2=equiv[num2]

    return num1+num2

def transform(input):
    if (re.fullmatch(rgb_format,input)):
        hexa='#'
        for i in input.split(','):
            hexa+= dec_to_hex(i.split(' ')[len(i.split(' '))-1])
        return hexa
    
    elif(re.fullmatch(hex_format,input)):
        return 'r: '+str(int(input[1:3],16))+', g: '+str(int(input[3:5],16))+', b: '+str(int(input[5:7],16))
    
    else:
        return 'Wrong format'
    

