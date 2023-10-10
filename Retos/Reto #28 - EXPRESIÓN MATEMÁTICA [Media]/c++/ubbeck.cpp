/*
 * Crea una función que reciba una expresión matemática (String)
 * y compruebe si es correcta. Retornará true o false.
 * - Para que una expresión matemática sea correcta debe poseer
 *   un número, una operación y otro número separados por espacios.
 *   Tantos números y operaciones como queramos.
 * - Números positivos, negativos, enteros o decimales.
 * - Operaciones soportadas: + - * / % 
 *
 * Ejemplos:
 * "5 + 6 / 7 - 4" -> true
 * "5 a 6" -> false
 */

#include <iostream>
#include <string>
#include <algorithm>
#include <ctype.h>


bool mathExpression(std::string expression);
bool isOperator (char c);

int main(){

    std::cout << mathExpression("5 + 6 / 7 - 4") << std::endl; //Expected 1
    std::cout << mathExpression("5 a 6") << std::endl; //Expected 0
    std::cout << mathExpression("5 * 6 //") << std::endl; // 0
    std::cout << mathExpression("5+ 6 - 3+1 *7 /1") << std::endl; // 1
    std::cout << mathExpression("+ 6 - 3+1 *7") << std::endl; // 0

    return 0;
}

bool mathExpression(std::string expression){

    expression.erase(remove(expression.begin(), expression.end(), ' '), expression.end());

    if(!isdigit(expression[0]) || !isdigit(expression[expression.length() - 1])){
        return false;
    }

    for(int i = 2, j = 1; i < expression.length(); i += 2, j += 2){
        if(!isdigit(expression[i]) || !isOperator(expression[j])){
            return false;
        }
    }
    return true;
}

bool isOperator (char c){
    return c == '+' || c == '-' || c == '*' || c == '/' || c == '%';
}