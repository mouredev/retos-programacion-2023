def fizz_buzz():
    for index in range(1, 101):
        output = ( "fizz" if index%3==0 else "" ) + ( "buzz" if index%5==0 else "" )
        print( output if output else index )

fizz_buzz();