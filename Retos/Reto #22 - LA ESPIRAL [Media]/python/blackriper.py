from dataclasses import dataclass
import math

@dataclass
class Spiral:
    l:int
    
    def print_spiral(self):
        uplad = (math.ceil(self.l / 2))
        
        for i in range(uplad):
            if (i == 0):
                print(("═"*(self.l-1)) + "╗")
            else:
                print(("║"*(i-1)+ "╔" + "═"*(self.l - (2*i)-1)) + "╗" + "║"*i)
        
        for i in range(uplad, self.l):
            print("║"*(self.l-i-1)+ "╚" + "═"*((2*i)-self.l) + "╝" + "║"*(self.l-i-1))


def main():
    lad= int(input("Introduce un numero de lados de la espiral "))
    sp= Spiral(lad)
    sp.print_spiral()
    

if __name__ == "__main__":
    main()    
