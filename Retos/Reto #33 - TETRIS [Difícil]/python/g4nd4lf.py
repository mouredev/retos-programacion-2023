def tetris():
    from enum import Enum
    import keyboard
    import os
    import copy

    pixel='🔲'
    pixel_busy='🔳'
    rotnum=0
    class Move(Enum):
        DOWN = 1
        RIGHT = 2
        LEFT = 3
        ROTATE = 4
    rotations=(
        ((0,2),(-1,1),(0,0),(1,-1)),
        ((2,0),(1,1),(0,0),(-1,-1)),
        ((0,-2),(1,-1),(0,0),(-1,1)),
        ((-1,0),(0,-1),(1,0),(2,1))
    )
    def move(piece,move: Move,rotnum):
        newpiece=copy.deepcopy(piece)
        match move:
            case Move.DOWN:
                for p in newpiece:
                    p[0]+=1
            case Move.RIGHT:
                for p in newpiece:
                    p[1]+=1
            case Move.LEFT:
                for p in newpiece:
                    p[1]-=1
            case Move.ROTATE:
                for i in range(4):
                    newpiece[i][0]+=rotations[rotnum][i][0]
                    newpiece[i][1]+=rotations[rotnum][i][1]
                rotnum+=1
                if rotnum==4:
                    rotnum=0
        rows=[p[0] for p in newpiece]
        cols=[p[1] for p in newpiece]                
        if max(rows)>9 or max(cols)>9 or min(cols)<0 or min(rows)<0:
            return (piece,rotnum)
        else:
            return (newpiece,rotnum)

    def print_screen(screen,piece):
        sc=copy.deepcopy(screen)
        for p in piece:
            sc[p[0]][p[1]]=pixel_busy
        for row in sc:
            print("".join(row))    

    row=[]
    for _ in range(10):
        row.append(pixel)
    screen=[]
    for _ in range(10):
        screen.append(row.copy())
    cleanScreen=screen.copy()
    tetris_piece=[[0,0],[1,0],[1,1],[1,2]]
    newpiece=tetris_piece
    while True:
        event = keyboard.read_event()
        if event.name == "esc":
            break
        elif event.event_type == keyboard.KEY_DOWN:
            if event.name == "left":
                (newpiece,rotnum)=move(newpiece,Move.LEFT,rotnum)
            if event.name == "right":
                (newpiece,rotnum)=move(newpiece,Move.RIGHT,rotnum)
            if event.name == "down":
                (newpiece,rotnum)=move(newpiece,Move.DOWN,rotnum)
            if event.name == "space":
                (newpiece,rotnum)=move(newpiece,Move.ROTATE,rotnum)
            os.system("clear")
            print_screen(cleanScreen,newpiece)
tetris()
