def trifuerza(rows:int)->None:
  for row in range(2*rows):
    if row<rows:
        asterisks = "*"*(1+row*2)
    else:
        asterisks = '*'*(2*(row-rows)+1)+' '*((2*rows-row)*2-1)+'*'*((row-rows)*2+1)
    print(' '*(2*rows-row-1)+asterisks)
    
def main(rows:int=2)->None:
    
    if isinstance(rows, int) and rows>0:
        trifuerza(rows)
    else:
        print('Number of rows must be positive integer')

if __name__=='__main__':
    main(10)