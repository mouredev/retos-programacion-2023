import time

def my_random():
   seed = int(time.time())
   seed = (seed * 6364136223846793005 + 1) & 0xFFFFFFFFFFFFFFFF
   random_number = (seed % 101)
   return random_number

print(my_random())
