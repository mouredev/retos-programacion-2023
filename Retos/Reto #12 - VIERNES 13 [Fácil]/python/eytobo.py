from datetime import date

def get_valid_inputs(log, valid_inputs):
  text_input = int(input(log))
  if text_input in valid_inputs:
    return text_input
  else:
    print("You had introduced a wrong input. Please retry.")
    get_valid_inputs(log, valid_inputs)

def main():
    year = get_valid_inputs("Insert the year: ", range(9999))
    month = get_valid_inputs("Insert the month: ", range(13))
    DAY = 13
    
    dow = date(year, month, DAY).weekday() + 1
    
    if dow == 5:
        print(f'Indeed, month {month} of year the {year} has a Friday the 13th')
    else:
        print(f'No, month {month} of year the {year} does not have a Friday the 13th')
        
    def get_other(valid_inputs, text_other):
        promp = get_valid_inputs(text_other, valid_inputs)
        if promp == 1:
            main()
        elif promp == 2:
            print("Thanks for use the program. See you soon.")
          
    get_other([1,2], "Do you want to review other date? \n1: True \n2: No\n")
    
main()
