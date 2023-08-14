from datetime import datetime

def random() -> int:
    time_st = str(int(datetime.timestamp(datetime.now()) * 1000000))
  
    time_1 = int(time_st[: int(len(time_st) / 2)])
    time_2 = int(time_st[int(len(time_st) / 2) :])
    return int((time_1 * time_2) % 101)

print(random())