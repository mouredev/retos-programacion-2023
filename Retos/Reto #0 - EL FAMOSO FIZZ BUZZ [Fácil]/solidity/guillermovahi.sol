//SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;

contract FizzBuzz {
    event Print(string); // The way to "log" in solidity ;)
    event PrintNumber(uint);

    function execute() public {
        for (uint i = 1; i <= 100; i++) {
            if (i % 3 == 0 && i % 5 == 0) {
                emit Print("FizzBuzz");
            } else if (i % 3 == 0) {
                emit Print("Fizz");
            } else if (i % 5 == 0) {
                emit Print("Buzz");
            } else {
                emit PrintNumber(i);
            }
        }
    }
}
