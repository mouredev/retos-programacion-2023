import re

hex_format=r'#[a-fA-F0-9]{6}'
rgb_format=r'r: [a-fA-F0-9]{1,2}, g: [a-fA-F0-9]{1,2}, b: [a-fA-F0-9]{1,2}'

def transform(input):
    if (re.fullmatch(rgb_format,input)):
        hex='#'
        for i in input.split(','):
            if len(i.split(' ')[len(i.split(' '))-1])<2:
                hex+= '0' + i.split(' ')[len(i.split(' '))-1]
            else:
                hex+=(i.split(' ')[len(i.split(' '))-1])
        return hex
    
    elif(re.fullmatch(hex_format,input)):
        return 'r: '+input[1:3]+', g: '+input[3:5]+', b: '+input[5:7]
    
    elif(re.fullmatch(r'#0{3}',input) or re.fullmatch(r'#[fF]{3}',input)):
        return 'r: '+input[1]+', g: '+input[2]+', b: '+input[3]
    
    else:
        return 'Wrong format'