<?php
/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

function is_prime(int $number): bool
{
	if($number > 1){
		for($i = 2; $i < $number; $i++){
			if ($number % $i == 0){
				return false;
			}
		}
		return true;
	}
	else {
		return false;
	}
}

function fibonacci(int $number): int
{
	if ($number == 0){
		return 0;
	}
	else if ($number == 1){
		return 1;
	} 
	else{
		return fibonacci($number-1) + fibonacci($number-2);
	}
}

function is_fibonacci(int $number): bool
{
	$sequence = array(fibonacci(0));
	$counter = 0;
	
	while($sequence[$counter] < $number){
		$counter++;
		array_push($sequence, fibonacci($counter));
	}
	
	if($sequence[$counter] == $number){
		return true;
	}

	return false;
}

function is_even(int $number): bool
{
	if($number % 2 == 0){
		return true;
	}
	return false;
}

function check_number(int $number)
{
	if($number > -1){
		echo $number;
		echo " is ";

		if(is_prime($number) == false){
			echo "not ";
		}

		echo "prime, ";

		if(is_fibonacci($number) == false){
			echo "is not ";
		}
		echo "fibonacci and is ";

		if(is_even($number)){
			echo "even";
		}
		else{
			echo "odd";
		}
	}
	else{
		echo "Negative number";
	}
	echo "\n";
}

check_number(2);
check_number(7);
check_number(8);
check_number(16);
check_number(17);
check_number(0);
check_number(89);
check_number(97);
check_number(100);
check_number(1);
check_number(-1);