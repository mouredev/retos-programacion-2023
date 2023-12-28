! RETO # 01 - FIZZBUZZ

program fizzbuzz
    implicit none

    integer :: numbers_array(100)
    integer :: i, number
    integer :: n

n = 100
numbers_array = [(i, i = 1, n)] 

do number = 1, n
    if ( mod(number,15) == 0 ) then
        print *, "FizzBuzz"
    else if ( mod(number,3) == 0 ) then
        print *, "Fizz"
    else if ( mod(number,5) == 0 ) then
        print *, "Buzz"
    else
        print *, numbers_array(number)
    end if
end do

end program fizzbuzz

