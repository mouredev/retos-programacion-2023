import math

def draw_spiral(n):
    half = math.ceil(n / 2)
    
    for i in range(half):
        if i == 0:
            print('═' * (n - 1)  + '╗')
        
        else:
            print('║' * (i - 1) + '╔' + '═' * (n - 2 * i - 1) + '╗' + '║' * i)
    
    for i in range(n - half):
        print('║' * (n - half - i - 1) + '╚' + '═' * ((n % 2) + 2 * i) + '╝' + '║' * (n - half - i - 1))


draw_spiral(2)
draw_spiral(5)
draw_spiral(8)
draw_spiral(11)
