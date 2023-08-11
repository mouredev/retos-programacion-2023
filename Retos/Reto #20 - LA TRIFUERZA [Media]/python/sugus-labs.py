import math

def draw_triforce(num):
    
    num_triangles = 3
    num_rows = num
    step = 2
    big_row = (step * num) - 1
    num_list = [n for n in range(1, big_row + step, step)]
    #print(num_list)

    for iter in range(0, num_rows):
        padding_num = int((num_list[-1] - num_list[iter]) / 2)
        curr_num = num_list[iter]
        #print("Padding: ", padding_num)
        #print("Stars:   ", curr_num)
        padding_str = " " * (padding_num + num)
        stars_str = "*" * curr_num
        print(f"{padding_str}{stars_str}{padding_str}")
    for iter in range(0, num_rows):
        padding_num = int((num_list[-1] - num_list[iter]) / 2)
        curr_num = num_list[iter]
        #print("Padding: ", padding_num)
        #print("Stars:   ", curr_num)
        padding_str = " " * padding_num
        stars_str = "*" * curr_num
        print(f"{padding_str}{stars_str}{padding_str} {padding_str}{stars_str}{padding_str}")
            
if __name__ == "__main__":
    
    num = 4
    draw_triforce(num)

