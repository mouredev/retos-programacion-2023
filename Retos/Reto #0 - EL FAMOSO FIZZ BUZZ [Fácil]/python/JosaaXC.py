def main():
    for i in range(1, 101):
        if i % 3 == 0:
            print(f"{i} => fizz")
        if i % 5 == 0:
            print(f"{i} => buzz")
        if i % 15 == 0:
            print(f"{i} => fizzbuzz")
            
if __name__ == "__main__":
    main()
    
    