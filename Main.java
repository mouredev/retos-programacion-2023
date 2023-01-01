package com.company;

public class Main {

    public static void main(String[] args) {
        int num;
	for(num=1;num<=100;num++){
        if(num % 3==0 && num %5 ==0 ){
            System.out.println("fizzbuzz");
        }else if (num %3==0){
            System.out.println("fizz");
        } else if(num%5==0){
            System.out.println("buzz");
        }else {
            System.out.println(num);
        }
    }
    }
}
