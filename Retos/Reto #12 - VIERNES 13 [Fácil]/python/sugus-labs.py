from datetime import date

def friday_13th_exists(year, month):
    
    dt = date(
        year = int(year), 
        month = int(month), 
        day = 13)
    is_friday = (dt.weekday == 4)
        
    return dt, is_friday

                                              
if __name__ == "__main__":

    year = "2023"
    month = "09"
    dt, is_friday = friday_13th_exists(year, month)
    print(f"{dt} is friday?: {is_friday}")
    #print(params_values)