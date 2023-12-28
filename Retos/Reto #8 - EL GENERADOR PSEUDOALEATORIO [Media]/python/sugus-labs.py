import datetime
import platform

def generate_pseudorandom_number():
    dt_now = datetime.datetime.now()
    year = dt_now.year
    first_num = int(str(year)[:2])
    sec_num = int(str(year)[2:])
    month = dt_now.month
    third_num = int(month)
    day = dt_now.day
    fourth_num = int(day)
    hour = dt_now.hour
    fiveth_num = int(hour)
    minute = dt_now.minute
    sixth_num = int(minute)
    second = dt_now.second
    seventh_num = int(second)
    microsec = dt_now.microsecond
    heighth_num = int(str(microsec)[:2])
    nineth_num = int(str(microsec)[2:4])
    try:
        tenth_num = int(str(microsec)[4:])
    except:
        tenth_num = 0       
    #print(dt_now)
    #print(year, month, day, hour, minute, second, microsec)
    #print(
    #    first_num, sec_num, third_num, fourth_num, 
    #    fiveth_num, sixth_num, seventh_num, heighth_num,
    #    nineth_num, tenth_num)
    vers = platform.uname().version
    vers_num = 0
    for c in vers:
        if c.isdigit():
            vers_num = vers_num + int(c)
    if vers_num > 101:
        vers_num % 101    
    #print(vers_num)
    date_num = (first_num + sec_num + third_num + fourth_num 
        + fiveth_num + sixth_num + seventh_num + heighth_num
        + nineth_num + tenth_num) % 101
    #print(date_num)
    final_num = int((vers_num + date_num) / 2)
    return final_num
                                              
if __name__ == "__main__":

    num = generate_pseudorandom_number()
    print(num)