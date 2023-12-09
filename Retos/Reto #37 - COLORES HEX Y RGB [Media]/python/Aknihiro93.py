

def converter_rgb(r:int, g:int, b:int) -> str:
    if r > 255 or g > 255 or b > 255:
        print("Error")
        return ""
    list_result = list()

    for i in [r, g, b]:
        if i < 9:
            i = hex(i)
            i = i[2:].zfill(2)
        else:
            i = hex(i)
            i = i[2:].upper()
        list_result.append(i)
    return "#" + f"{list_result[0]}{list_result[1]}{list_result[2]}"

def converter_hex (HEX:str):
    return f"(r: {int(HEX[1:3].lower(), 16)}, g: {int(HEX[3:5].lower(), 16)}, b: {int(HEX[5:7].lower(), 16)}"

print(converter_rgb(8, 200, 33))
print(converter_hex("#08C821"))