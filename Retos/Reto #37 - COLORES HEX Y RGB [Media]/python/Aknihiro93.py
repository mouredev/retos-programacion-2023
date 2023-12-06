def converter_rgb(r:int, g:int, b:int) -> str:
    if r > 255 or g > 255 or b > 255:
        print("Error")
        return ""
    result = "#"
    for i in [r, g, b]:
        temp = i
        i = hex(i)[2:]
        if temp < 16:
            i = i.zfill(2)    
        i = i.upper()
        result = result + i
    return result

def converter_hex (HEX:str):
    return f"(r: {int(HEX[1:3].lower(), 16)}, g: {int(HEX[3:5].lower(), 16)}, b: {int(HEX[5:7].lower(), 16)}"

print(converter_rgb(255, 200, 33))
print(converter_hex("#08C821"))
