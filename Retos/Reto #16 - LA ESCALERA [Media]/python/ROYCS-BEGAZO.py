def stair(steps):
    if steps > 0:
        for step in range(steps+1):
            spaces = "  " * (steps - step)
            step_draw  = "_" if step == 0 else "_|"
            print(f'{spaces}{step_draw}')
    elif steps < 0:
        for step in range(abs(steps)+1):
            spaces = " " * ((step * 2) -1)
            step_draw  = "_" if step == 0 else "|_"
            print(f'{spaces}{step_draw}')
    else:
        print('__')

stair(4)