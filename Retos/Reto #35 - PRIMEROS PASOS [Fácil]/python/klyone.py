#!/usr/bin/env python3

# Example 1: Hello world
def run_hello_world():
    print("Hello world!")

# Example 2: Constants
CONSTANT1 = "Hello"
CONSTANT2 = 3.14

# Example 3: Variable & Types
var1 = "Variable1"
var2 = 3
var3 = 5.17
var4 = True

# Example 4: Data structs
# Array can be considered a sub-type of list
# Set can be considered a sub-type of Dictionary
# You can also use third-party libraries to import specific imolementations
list1 = [1,2,3,4]
tuple1 = (1,2)
dict1 = {
    "Property1" : 3.2
}

# Example 5: if/else
def run_if_else():
    if True:
        print("Run if statement")

    if False:
        pass
    else:
        print("Run else statement")

    if False:
        pass
    elif True:
        print("Run elsd if statement")

# Example 6: Loops
def run_loops():
    # For int loop
    print("For int loop")
    for i in range(10):
        print(i)

    print("Foreach (in list1)")
    for a in list1:
        print(a)

    print("While False until cnt == 10")
    cnt = 0
    while cnt < 10:
        print(cnt)
        cnt = cnt + 1

# Example 7: functions
def run_func_noargs_noret():
    print("Func no args no ret")
def run_func_noargs_ret():
    print("Func no args ret")
    return "Return val"
def run_func_args_ret(arg1, arg2):
    print("Func args ret")
    print(arg1)
    print(arg2)
    return 3.16

# Example 8: Class
class Myclass:
    def __init__(self, arg1):
        self.a1 = arg1
    def dump(self):
        print("Myclass dump: "+str(self.a1))

# Example 9: Exceptions
def run_exceptions():
    print("Try without exception")
    try:
        run_func_noargs_noret()
    except Exception:
        print("Exception occurs!")

    print("Try with exception")
    try:
        raise Exception()
    except Exception:
        print("Exception occurs!")

# Entry point to run all examples
if __name__ == "__main__":
    run_hello_world()

    print("CONSTANT1: "+CONSTANT1)
    print("CONSTANT2: "+str(CONSTANT2))

    print("String var: "+var1)
    print("Int var: "+str(var2))
    print("Float var: "+str(var3))
    print("Boolean var: "+str(var4))

    print("List1: "+str(list1))
    print("Tuple1: "+str(tuple1))
    print("Dict1: "+str(dict1))

    run_if_else()
    run_loops()

    run_func_noargs_noret()
    print(run_func_noargs_ret())
    print(run_func_args_ret("Arg1", 5))

    mc1 = Myclass(10)
    mc1.dump()

    run_exceptions()
