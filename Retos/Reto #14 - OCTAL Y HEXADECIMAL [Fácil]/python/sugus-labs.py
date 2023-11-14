def convert_decimal_to_other_systems(num_dec):
        
    def octal(num_dec):
        octal_list = []
        quotient = None
        while quotient != 0:
            quotient = num_dec // 8
            remainder = num_dec % 8
            num_dec = quotient
            # print(quotient)
            octal_list.append(remainder)
        octal_list.reverse()
        num_octal = "".join(str(x) for x in octal_list)
        return num_octal 
    
    def hexa(num_dec):
        hexa_dict = {
            "10": "A" , "11": "B", "12": "C",
            "13": "D", "14": "E", "15": "F"            
        }
        hexa_list = []
        quotient = None
        while quotient != 0:
            quotient = num_dec // 16
            remainder = num_dec % 16
            num_dec = quotient
            # print(quotient)
            hexa_list.append(remainder)
        hexa_list.reverse()
        for num, x in enumerate(hexa_list):
            if x > 9:
                hexa_list[num] = hexa_dict[str(x)]
        num_hexa = "".join(str(x) for x in hexa_list)
        return num_hexa
    
    num_octal = octal(num_dec)
    num_hexa = hexa(num_dec)
    return num_octal, num_hexa
                                              
if __name__ == "__main__":

    num_dec = 1353535
    num_octal, num_hexa = convert_decimal_to_other_systems(num_dec)
    print(f"Decimal number '{num_dec}' is:\n - octal: '{num_octal}'\n - hexa: '{num_hexa}'")