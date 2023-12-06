class Staircase:
    def __init__(self, steps: int):
        self.steps = steps

    def draw(self):
        if self.steps > 0:
            for step in range(self.steps + 1):
                spaces = "  " * (self.steps - step)
                step_draw = "_" if step == 0 else "_|"
                print(f"{spaces}{step_draw}")
        elif self.steps < 0:
            for step in range(abs(self.steps) + 1):
                spaces = " " * ((step * 2) - 1)
                step_draw = "_" if step == 0 else "|_"
                print(f"{spaces}{step_draw}")
        else:
            print("__")
            
staircase1 = Staircase(0)
staircase2 = Staircase(4)
staircase3 = Staircase(20)
staircase4 = Staircase(-4)
staircase5 = Staircase(-20)

staircase1.draw()
staircase2.draw()
staircase3.draw()
staircase4.draw()
staircase5.draw()
