def create_stair_to(floor):
    if floor == 0:
        print("__")
    elif floor > 0:
        s = " " * ((floor + 1) * 2)
        print(f"{s}_")
        for num in range(floor, 0, -1):
            s = " " * (num * 2)
            print(f"{s}_|")  
    else:
        print(f"_")
        for num in range(0, -floor):
            s = " " * ((num * 2) + 1)
            print(f"{s}|_")
            
if __name__ == "__main__":
    
    floor = -4
    create_stair_to(floor)